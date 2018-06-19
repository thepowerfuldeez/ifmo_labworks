import entities
import socket
import struct


# pyxbgen -u Channel.xsd -m channel
# pyxbgen -u Entities.xsd -m entities


def send(xml, guid):
    """
    - Дано в качестве аргумента скрипту: guid, являющийся значением тэга по паттерну session-id.
    - Получить: все сообщения, имеющие такой же thread-id, как хотя бы одно,
    имеющее заданный session-id в пределах того же источника.
    """
    pass
    order = entities.CreateFromDocument(xml.read())

    # print('%s is sending %s %d thing(s):' % (order.billTo.name, order.shipTo.name, len(order.items.item)))
    print(f"{order.billTo.name} is sending {order.shipTo.name} {len(order.items.item)} thing(s):")
    for item in order.items.item:
        # print('  Quantity %d of %s at $%s' % (item.quantity, item.productName, item.USPrice))
        print(f"  Quantity {item.quantity} of {item.productName} at {item.USPrice}")


def send_xml(bytes):
    TCP_IP = '5.19.208.160'
    TCP_PORT = 2111
    BUFFER_SIZE = 1024
    dataLength = len(bytes)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.setblocking(1)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    header = bytearray()
    header.append(0xE8)
    header.append(0x07)
    s.send(header)
    s.send(struct.pack(">I", len(bytes))[::-1])
    s.sendall(bytes)

    print("sent ", len(bytes) + 6, " bytes")

    h_sig = s.recv(2)
    h_len = s.recv(4)
    bytesCount = struct.unpack(">I", h_len[::-1])[0]
    print(bytesCount)
    bytes_recv = s.recv(bytesCount)
    s.close()

    xml = bytes_recv.decode("utf-8")

    print("received ", bytesCount + 6, " data:", xml)
    return xml


def parse_xml(xml):
    pass


def main():
    guid = 123
    pattern = f"""<?xml version="1.0" encoding="utf-8" ?>
<RpcCommand xmlns="EventsGraphNavigator.Interaction.Entities">
    <Call CallId="123">
        <RemoteInstanceId>
            <Value>keyvaluestr</Value>
        </RemoteInstanceId>
        <MethodId DeclaringTypeName="asdf" MetadataToken="3" MethodName="asdf"/>
        <Arguments>
            <Value>
                <Instance xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="LogMessagesCustomQueryInfoType"
                          Name="myquery">
                    <IncludeObsoleteSources>true</IncludeObsoleteSources>
                    <Model>
                        <All>
                            <MessageHasTagInstance>
                                <Where>
                                    <PatternNameContains>
                                        <Text MatchWholeWord="true" MatchCase="false" MatchingMode="String">
                                            <Pattern>session-id</Pattern>
                                        </Text>
                                    </PatternNameContains>
                                </Where>
                            </MessageHasTagInstance>
                            <MessageHasTagInstance>
                                <Where>
                                    <TagInstanceHasKey>
                                        <Where>
                                            <ValueContains>
                                                <Text MatchWholeWord="true" MatchCase="false" MatchingMode="String">
                                                    <Pattern>{guid}</Pattern>
                                                </Text>
                                            </ValueContains>
                                        </Where>
                                    </TagInstanceHasKey>
                                </Where>
                            </MessageHasTagInstance>
                        </All>
                    </Model>
                </Instance>
            </Value>
            <Value>
                <String>sdf</String>
            </Value>
        </Arguments>
    </Call>
</RpcCommand>"""
    # bytes = bytes(pattern)

    bytes = open("in.xml", 'rb').read()
    send_xml(bytes)
    # a = entities.CreateFromDocument(open("XMLFILE1.xml", "rb").read())


if __name__ == '__main__':
    main()

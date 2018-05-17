import entities.py as entities
import requests
import socket
import xmlrpc.client as client
import time


# pyxbgen -u Channel.xsd -m channel
# pyxbgen -u Entities.xsd -m entities

# with open("<filename>") as xml:
#     # xml = open('po1.xml').read()
#     order = entities.CreateFromDocument(xml.read())
#
#     # print('%s is sending %s %d thing(s):' % (order.billTo.name, order.shipTo.name, len(order.items.item)))
#     print(f"{order.billTo.name} is sending {order.shipTo.name} {len(order.items.item)} thing(s):")
#     for item in order.items.item:
#         # print('  Quantity %d of %s at $%s' % (item.quantity, item.productName, item.USPrice))
#         print(f"  Quantity {item.quantity} of {item.productName} at {item.USPrice}")


def send(xml, guid):
    """
    - Дано в качестве аргумента скрипту: guid, являющийся значением тэга по паттерну session-id.
     - Получить: все сообщения, имеющие такой же thread-id, как хотя бы одно, имеющее заданный session-id в пределах того же источника.
    """
    pass
    order = entities.CreateFromDocument(xml.read())

    # print('%s is sending %s %d thing(s):' % (order.billTo.name, order.shipTo.name, len(order.items.item)))
    print(f"{order.billTo.name} is sending {order.shipTo.name} {len(order.items.item)} thing(s):")
    for item in order.items.item:
        # print('  Quantity %d of %s at $%s' % (item.quantity, item.productName, item.USPrice))
        print(f"  Quantity {item.quantity} of {item.productName} at {item.USPrice}")


if __name__ == '__main__':
    command = '<xml version="1.0" encoding="UTF-8"><header/><body><code><body/>'

    # conn = client()

    ip, port = '5.19.208.160', 2111
    # requests.get()
    print('init')
    # conn = socket.socket()
    # print('connecting...')
    # conn.connect((ip, port))
    # conn.send(b"Hello! \n")
    # data = b""
    #
    # tmp = conn.recv(1024)
    # while tmp:
    #     data += tmp
    #     tmp = conn.recv(1024)
    #
    # print(data.decode("utf-8"))
    # conn.close()

    # callCmd = {
    #     "Item": {
    #         "_type": "Call",
    #         "CallId": callId,
    #         "RemoteInstanceId": {"Value": "" + objId},
    #         "MethodId": {
    #             "DeclaringTypeName": declaringTypeName,
    #             "MethodName": methodName,
    #             "GenericSignatureTypes": genericParams
    #         },
    #         "Arguments": {"Items": args}
    #     }
    # }

    query = {
        "Item": {
            "_type": "RapidNavigator.Index.Interaction.QueryParametersInfoType",
            "EntitiesFilter": {
                "Item": {
                    "_type": "HavingNameAndKind",
                    "Name": "lalala",
                    "Kind": "null",
                    "Invert": "false"
                }
            }
        }
    }

    from xmlrpc.client import ServerProxy

    print('connecting...')
    with ServerProxy(f"http://{ip}:{port}/") as s:
        print(s.system.listMethods())
        print('connected')
        print(s.PerformQuery("/", query))

    # print('init')
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect((ip, port))
    # print('connected.')
    #
    # s.send(command)
    #
    # time.sleep(2)
    # resp = s.recv(3000)
    # print(resp)

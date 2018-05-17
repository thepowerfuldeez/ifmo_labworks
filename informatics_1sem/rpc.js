var JsonTcpSockets = require('json-tcp-socket');

module.exports.JsonTcpSocketSink = function(sck) {
    var callback = null;

    this.send = function(o) {
        sck.write(o);
    };

    this.setCallback = function(cb) {
        callback = cb;
    };

    this.start = function() {
        sck.on('data', function (data) {
            if (callback != null)
                callback(data);
        });
    }
};

var Proxy = function(channel, id, interfaces) {

    this.call = function(methodName, args, onResult, onError) {
        channel.performCall(id, interfaces[0], methodName, null, args, onResult, onError);
    };

    this.callGeneric = function(methodName, genericParams, args, onResult, onError) {
        channel.performCall(id, interfaces[0], methodName, { "TypeName": genericParams }, args, onResult, onError);
    };
};

module.exports.Channel = function(sink) {
    var callsCount = 0;
    var pendingCalls = [];
    var me = this;

    this.remote = new Proxy(me, "0", ["RapidNavigator.Index.Interaction.Channel.IChannelService"]);

    this.start = function() {
        sink.start();
    };

    this.performCall = function(objId, declaringTypeName, methodName, genericParams, args, onResult, onError) {
        var callId  = ++callsCount;
        pendingCalls[callId] = {
            callId, methodName, args, onResult, onError
        };

        var callCmd = {
            "Item": {
              "_type": "Call",
              "CallId": callId,
              "RemoteInstanceId": { "Value": "" + objId },
              "MethodId": {
                "DeclaringTypeName": declaringTypeName,
                "MethodName": methodName,
                "GenericSignatureTypes": genericParams
              },
              "Arguments": { "Items": args }
            }
        };

        sink.send(callCmd);
    };

    var handleCallResult = function(callId, result, outArguments, ex) {
        if (ex == null) {
            if (result != null && result._type == "RapidNavigator.Index.Interaction.RpcRemoteObjectReferenceInfoType") {
                result = new Proxy(me, result.RemoteInstanceId.Value, result.InterfaceTypes.Items);
            }

            pendingCalls[callId].onResult(result);
        } else {
            pendingCalls[callId].onError(ex);
        }
    };

    var handleCallInvoke = function(callId, remoteInstanceId, methodId, args) {
        console.log('Unexpected Call command ', data._type, ': ', o);
    };

    sink.setCallback(function(o) {
        data = o.Item;
        switch(data._type) {
            case "Call": handleCallInvoke(data.CallId, data.RemoteInstanceId, data.MethodId, data.Arguments); break;
            case "Result": handleCallResult(data.CallId, data.ReturnValue.Item, data.OutArguments.Items, data.Exception); break;
            default: console.log('Unexpected command ', data._type, ': ', o); break;
        }
    });
};
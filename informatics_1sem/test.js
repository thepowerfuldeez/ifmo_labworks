var JsonTcpSockets = require('json-tcp-socket');
var rpc = require('./rpc');

var JsonTcpSockets = new JsonTcpSockets({tls: false});
var sck = new JsonTcpSockets.Socket();

var onErr = function (ex) {
    console.log(ex);
};

sck.on('connect', function () {
    var sink = new rpc.JsonTcpSocketSink(sck);
    var channel = new rpc.Channel(sink);
    channel.start();

    channel.remote.callGeneric("GetObjectByName", [ "RapidNavigator.Index.Interaction.INavigatorService" ], [ { Item: "svc" } ], function (svc) {
        console.log("Got nav service ");

        svc.call("OpenLogonSession", [ { Item: null } ], function (session) {
            console.log("Got session");

            session.call("get_Querying", [], function (querySvc) {
                console.log("Got query svc");

                var query = {
                    Item: {
                        _type: "RapidNavigator.Index.Interaction.QueryParametersInfoType",
                        EntitiesFilter: {
                            Item: {
                                _type: "HavingNameAndKind",
                                Name: "lalala",
                                Kind: null,
                                Invert: false
                            }
                        }
                    }
                };

                querySvc.call("PerformQuery", [ query ], function (result) {

                    console.log("Got result: ", result);

                }, onErr);
            }, onErr);
        }, onErr);
    }, onErr);
});

sck.connect(12345, '127.0.0.1');
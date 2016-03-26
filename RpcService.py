from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

class RpcServer(object):
        def __init__(self, callbacks=None, host='', port=8000, ):
            self.host = host
            self.port = port

            # add the method names and the handlers to the dispatcher methods.
            if callbacks:
                for keys in callbacks.keys():
                    dispatcher[keys] = callbacks[keys]

        @Request.application
        def application(self, request):
            # Dispatcher is dictionary {<method-name>: callable}
            dispatcher["echo"] = lambda s: s
            dispatcher["add"] = lambda a,b: a+b

            print("Request data",request.data)
            response = JSONRPCResponseManager.handle(request.data, dispatcher)
            return Response(response.json, mimetype="application/json")

        def start(self):
            self.app = run_simple(self.host, self.port, self.application)

if __name__ == "__main__":
    server = RpcServer()
    server.start()
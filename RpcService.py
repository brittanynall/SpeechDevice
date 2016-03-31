from werkzeug.exceptions import NotFound
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from werkzeug.wsgi import wrap_file, responder
import os
import logging

debug_logger = logging.getLogger(__name__)

from jsonrpc import JSONRPCResponseManager, dispatcher

class RpcServer(object):

        def __init__(self, callbacks=None, host='', port=8000, ):
            self.host = host
            self.port = port

            self.views = {'get_rpc': self.get_rpc,
                          'images':self.get_file}

            self.url_map = Map([Rule('/', endpoint='get_rpc'),
                                Rule('/jsonrpc', endpoint='get_rpc'),
                                Rule('/images', endpoint='images')])


            # add the method names and the handlers to the dispatcher methods.
            if callbacks:
                for keys in callbacks.keys():
                    dispatcher[keys] = callbacks[keys]

        def get_rpc(self, environ, request):
             response = JSONRPCResponseManager.handle(request.data, dispatcher)
             return Response(response.json, mimetype="application/json")

        def get_file(self, environ, request):
            try:
                file = open('images/'+request.query_string.decode(), 'rb')
            except Exception as e:
                debug_logger.debug("could not read file" + str(e))
                raise NotFound()
            return Response(wrap_file(environ, file), direct_passthrough=True)

        @responder
        def application(self, environ, start_response):
            request = Request(environ)
            urls = self.url_map.bind_to_environ(environ)
            return urls.dispatch(lambda e, v: self.views[e](environ, request, **v),
                         catch_http_exceptions=True)

        def start(self):
            self.app = run_simple(self.host, self.port, self.application)

if __name__ == "__main__":
    server = RpcServer()
    server.start()
from pprint import pprint
from twisted.application.internet import TCPServer
from twisted.application.service import Application
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.internet import reactor, endpoints
from twisted.web import server

class FormPage(Resource):
    def render_Get(self, request):
        return ''

    def render_POST(self, request):
        #pprint(request.__dict__)
        newdata = request.content.getvalue()
        print newdata
        return ''
root = Resource()
root.putChild("form", FormPage())
endpoints.serverFromString(reactor, "tcp:8080").listen(server.Site(root))
reactor.run()
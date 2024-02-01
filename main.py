import cherrypy
from dataman import DataController

def start_service():
    dataman = DataController()
    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    dispatcher.connect('name_get', '/', controller=dataman, action='GET', conditions=dict(method=['GET']))

    conf = {
        'global' : {
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 3000
        },
        '/':{'request.dispatch': dispatcher}
    }
    
    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)


if __name__ == '__main__':
    start_service()

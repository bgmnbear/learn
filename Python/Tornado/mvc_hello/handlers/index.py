import tornado.web
from model.entity import Entity


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        entity = Entity.get('whister')
        self.render('index.html', entity=entity)

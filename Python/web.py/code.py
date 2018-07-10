import web
from web.template import render

urls = (
    '/', 'index',
    '/todo', 'todo',
)

db = web.database(dbn='postgres', user='username', pw='password', db='dbname')


class index:
    def GET(self):
        render = web.template.render('templates/')
        return render.index()


class todo:
    def GET(self):
        todos = db.select('todo')
        return render.todo(todos)

    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/todo')


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

from bottle import route, run, template
from wisdom import *
import os

@route('/')
def wisdom():
    return template("index", content=generate())

@route("/assets/<file_name:path>")
def assets(file_name):
    return bottle.static_file(file_name, root="assets")

init()
APP_ROOT = os.path.abspath(os.path.dirname(__file__))
bottle.TEMPLATE_PATH.append(os.path.join(APP_ROOT, "assets/tpl"))
app = bottle.default_app()

if __name__ == '__main__':
    from flup.server.fcgi import FCGIServer
    run(host="localhost", server=FCGIServer, reloader=True)

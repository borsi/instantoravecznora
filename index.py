from bottle import route, run, template
from wisdom import *

@route('/')
def wisdom():
    init()
    return template("index", content=generate())

@route("/assets/<file_name:path>")
def assets(file_name):
    return bottle.static_file(file_name, root="assets")

run(host='localhost', port=8080, debug=True)

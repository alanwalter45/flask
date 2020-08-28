from flask import Flask

application = Flask(__name__)

@application.route("/home")
def home():
    return '<h1>hello world from Flask.</h1>'

@application.route("/saludo/<path:name>")
def saludo(name):
    return '<h2>Hi {}</h2>'.format(nam)


application.run(port=8000,debug=True)
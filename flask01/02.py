from flask import Flask

application = Flask(__name__)

@application.route("/home")
def home():
    return '<h1>hello world from Flask.</h1>'

application.run(port=8000,debug=True)
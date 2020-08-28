from flask import Flask,jsonify

app = Flask(__name__)

app.config.from_object('config')

@app.route("/")
def indice():
    personas = [{"name":Persona("walter").name}, Persona("pedro").name]
    return jsonify(personas)
    
class Persona:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return self.name
    
app.run(port=7000)

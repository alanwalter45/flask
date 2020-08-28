import flask

app = flask.Flask(__name__)

@app.route('/')
def pagina():
    title = "Pagina principal"
    lista = ("amar","dormir","codificar")
    return flask.render_template("index.html",title=title,lista=lista)

#@app.template_filter('mi_filtro')
def mi_filtro(x):
    return x[:5]+'[...]'

#app.add_template_filter(mi_filtro,'mi_filtro')

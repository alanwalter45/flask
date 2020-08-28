from flask import Blueprint, render_template
import otro.views

def configure(app):
    pagina = Blueprint('pagina',__name__,url_prefix="/pagina")
    otro.views.configure(pagina)
    app.register_blueprint(pagina)

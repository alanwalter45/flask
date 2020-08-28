from otro.app import render_template
import otro.models

def configure(pagina):
    @pagina.route('/')
    def index():
        info = otro.models.info
        return render_template('index.html',info=info)
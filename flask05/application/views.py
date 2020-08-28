from application.app import render_template
import application.models

def configure(app):
    @app.route('/')
    def index():
        info = application.models.info
        return render_template('index.html',info=info)
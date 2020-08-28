from flask import Flask, render_template
import application.views
import otro.app

app = Flask(__name__)
app.config.from_object('application.config.Config')
application.views.configure(app)
otro.app.configure(app)
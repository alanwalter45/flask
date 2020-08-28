from flask import Flask,render_template

app = Flask(
__name__,
static_folder='recursos/estaticos',
static_url_path="/archivos")

app.config['DEBUG'] = True
app.config['ENV'] = 'Development'


@app.route('/')
def index():
    return render_template('home.html')

app.run()
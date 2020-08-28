from flask import Flask,render_template,flash,request

app = Flask(__name__)
app.config['SECRET_KEY']='alan'

@app.route('/')
def index():
    flash('mi primer mensaje','sms1')
    return render_template('index.html')

@app.route('/',methods=['POST'])
def index_post():
    data = request.args.get('name','nada')
    return f"dato : {data}"

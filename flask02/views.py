from app import app,request,render_template

@app.route('/')
def root():
    name = request.args.get('name')
    if not name:
        name = "sin param" 
    return render_template('home.html',name=name)
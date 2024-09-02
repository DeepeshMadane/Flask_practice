from flask import Flask,render_template,request
"""
it will create instance of flask
which will act as a WSGI (webserver gateway interface) application

"""

## wsgi application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to the this best flask course online on udemy hello deppesh to getting started on this course hello"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'hello {name}!'
    return render_template('form.html')
    
@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name} you just submitted the form Thank you for the time!'
    
    return render_template('form.html')
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask,render_template,request,url_for,redirect
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
    
@app.route("/submit1",methods=['GET','POST'])
def submit1():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name} you just submitted the form Thank you for the time!'
    
    return render_template('form.html')

## variable rule

@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score>50:
        res="pass"
    else:
        res="fail"
    return render_template('result.html',result=res)


@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score>=35:
        res="pass"
    else:
        res="fail"
    exp={'score':score,'res':res}

    return render_template('result1.html',result=exp)

@app.route("/successif/<int:score>")
def successif(score):
    return render_template('result.html',result=score)

@app.route("/submit",methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        Science=float(request.form['Science'])
        C = float(request.form['C'])
        data_science=float(request.form['DataScience'])
        Dsa = float(request.form['Dsa'])

        total_score=((Science+C+data_science+Dsa)/400)*100
    else:
        return render_template('get_result.html')
    return redirect(url_for('successres',score=total_score))



if __name__ == "__main__":
    app.run(debug=True)
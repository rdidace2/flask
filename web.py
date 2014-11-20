__author__ = 'john'
from flask import Flask



app = Flask(__name__)

@app.route('/kigali')
def index():
    return "I am in the capital of Rwanda"

@app.route('/kuramutsa')

def mwaramutse():
    return "Mwaramutse mwese"

@app.route("/counter/<int:number>")

def count(number):

    if number ==1:

        return "number one"
    elif number==2:

        return "number two"
    elif number ==3:
        return "number three"
    elif number==4:
        return "number four"
    elif number==5:

        return "number five"

    else:

        return "unknown number"

@app.route("/counter2/<int:number>")

def counter2(number):

    numbers =('zero', 'one', 'two', 'three', 'four', 'five')

    if number <=5:

        return '<h1> number %s</h1>' %numbers[number]

    else:

        return '<h1> the number is not in the range</h1>'

@app.route('/counter3/<int:value>')

def counter3(value):

    values ={0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}

    return "<h1>Number %s</h1>" % values.get(value, 'unknown')




if __name__=='__main__':
    app.run(debug=True)
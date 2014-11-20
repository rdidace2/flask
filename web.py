__author__ = 'john'
from flask import Flask
from flask import request, make_response
from flask import  redirect

#from web import app
# from flask import current_app


app = Flask(__name__)

# current_app.name
#
# app_ctx = app.app_context()
# app_ctx.push()
# current_app.name

@app.route('/facebook')

def goto_facebook():

    response = make_response(redirect('http://www.facebook.com'))

    return response

@app.route('/google')

def goto_google():

    response = make_response(redirect('http://www.google.com'))

    return response

@app.route('/yahoo')

def goto_yahoo():

    response = make_response(redirect('http://www.yahoo.com'))

    return response

@app.route('/igihe')

def goto_igihe():

    response = make_response(redirect('http://www.igihe.com'))

    return response


@app.route('/')

def index1():

    user_agent =request.headers.get('User_Agent')

    response = make_response ( "<h2> The browser is %s</h2>" %user_agent)

    return response

@app.route('/kigali')

def index():


    response = make_response( "<h>I am in the capital of Rwanda</h>")

    return response

@app.route('/kuramutsa')

def mwaramutse():
    response = make_response("Mwaramutse mwese")

    return response

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
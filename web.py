__author__ = 'john'
from flask import Flask  #http://127.0.0.1:5000/kigali. that is when we can be able to see the words I am in the capital of Rwanda.

app = Flask(__name__)

@app.route('/kigali')
def index():
    return "I am in the capital of Rwanda"
if __name__=='__main__':
    app.run(debug=True)
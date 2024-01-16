from flask import Flask, request, render_template, make_response

import json

app = Flask(__name__)

@app.route("/")
def holloworld():
    return "Hello, World"

@app.route("/name")
def holloYanin():
    return "Hello, Yanin!"

@app.route("/home", methods=['POST','GET'])
def homefn():
    print('we are in home')
    namein = request.form.get('fname')
    lastnamein = request.form.get('lname')
    print(namein)
    print(lastnamein)
    return render_template("home.html",name='namein')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0', port=500


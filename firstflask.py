from flask import Flask, request, render_template, make_response
import sys
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
    if request.method == "GET":
        print('we are in home(GET)', file=sys.stdout)
        namein = request.args.get('fname')
        print(namein, file=sys.stdout)
        return render_template("home.html",name=namein)

    elif request.method == "POST":
        print('we are in home(POST)', file=sys.stdout)
        namein = request.form.get('fname')
        lastnamein = request.form.get('lname')
        print(namein, file=sys.stdout)
        print(lastnamein, file=sys.stdout)
        return render_template("home.html",name=namein)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0', port=500


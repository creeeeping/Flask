from flask import Flask, request, response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, This is Main Page!"

@app.route('/about')
def about():
    return "This is the about page!"

@app.route('/user/<username>')
def number(username):
    return f'UserName : {username}'

@app.route('/number/<int:number>')
def user_profile(number):
    return f'number : {number}'

import requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url, data=data)

    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)
    
    if request.method == 'GET':
        print("GET method")

    if request.method == 'POST':
        print("***POST mathod***", request.data)

    return response("SucessFully submitted", status=200)

if __name__ == "__main__":
    app.run(debug=True)
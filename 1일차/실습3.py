from flask import Flask 

app = Flask(__name__)


@app.route("/")
def Home():
    return "Home"

@app.route("/Hello")
def hello():
    return "Hello"


# 동적 라우팅

@app.route("/user/<name>")
def greet(name):
    return f"{name}님 만나서 반갑습니다"

if __name__ == "__main__":
    app.run(debug=True)
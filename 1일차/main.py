from flask import Flask # flask 가져오기

app = Flask(__name__) # flask를 사용할건데, app을 통해서 사용한다.


@app.route("/")
def hello_world():
    return "hello, flask!!"


if __name__ == "__main__":
    app.run(debug=True) # 서버 실행 
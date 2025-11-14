from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def index():
    return render_template("typing.html")


@sock.route("/ws")
def websocket(ws):
    while True:
        data = ws.receive()
        if data is None:
            break

        if data == "typing":
            ws.send("💬 입력 중...")
        elif data == "stop":
            ws.send("")


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def index():
    return render_template("sentiment.html")

@sock.route("/ws")
def websocket(ws):
    while True:
        text = ws.receive()
        if text is None:
            break

        # 감정 분석
        positive = ["happy", "love", "good", "great", "건영"] # 긍정 단어 리스트
        negative = ["sad", "bad", "angry", "동석"] # 부정 단어 리스트

        ## 긍정
        # for word in positive:
        #     if word in text:
        #         ws.send("😊 긍정")
        sentiment = "🤨 중립"
        if any(word in text.lower() for word in positive):
            # ws.send("😊 긍정")
            sentiment = "😊 긍정"

        ## 부정
        # for word in negative:
        #     if word in text:
        #         ws.send("😡 부정")
        elif any(word in text.lower() for word in negative):
            # ws.send("😡 부정")
            sentiment = "😡 부정"

        else:
            # ws.send("🤨 중립")
            sentiment = "🤨 중립"

        ws.send(sentiment)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from flask_sock import Sock
import threading
import time

app = Flask(__name__)
sock = Sock(app)

connections = []

@sock.route('/ws')
def websocket(ws):
    connections.append(ws)
    while True:
        data = ws.receive()
        if data is None:
            break
    connections.remove(ws)

def background_job():
    # 5초에 1번 서버가 메시지를 보낼 수 있도록 세팅
    while True:
        time.sleep(5)
        for ws in list(connections):
            try:
                ws.send("서버가 클라이언트에게 알림 보냄")
            except Exception:
                pass # 연결이 끊어졌을 때 아무것도 안하게


threading.Thread(target=background_job, daemon=True).start()

if __name__ == "__main__":
    app.run(debug=True)
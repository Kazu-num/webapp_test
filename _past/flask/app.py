from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print('Received message: ' + data)
    # ここでPythonの処理を実行します（例として、文字列の逆順を返します）
    result = data[::-1]
    # 処理が完了したらクライアントに結果を送信します
    emit('response', {'data': result})

if __name__ == '__main__':
    socketio.run(app)

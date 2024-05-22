from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_socketio import SocketIO, send
import os
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'
socketio = SocketIO(app)

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return 'File uploaded successfully'

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return redirect(request.url)
    image = request.files['image']
    if image.filename == '':
        return redirect(request.url)
    if image:
        imagepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(imagepath)
        image_url = url_for('uploaded_file', filename=image.filename)
        socketio.emit('image', {'url': image_url})
        return 'Image uploaded successfully'

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    if 'グラフ表示' in msg:
        # グラフを生成
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
        ax.set(xlabel='x-axis', ylabel='y-axis', title='Sample Graph')
        ax.grid()

        # 画像をファイルに保存
        graph_path = os.path.join('uploads', 'graph.png')
        fig.savefig(graph_path)
        plt.close(fig)

        # グラフの画像URLを送信
        graph_url = url_for('uploaded_file', filename='graph.png')
        socketio.emit('graph', {'url': graph_url})
    else:
        reversed_msg = msg[::-1]  # メッセージを逆にする
        send(reversed_msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

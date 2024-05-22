from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send
import os

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
        return 'Image uploaded successfully'

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

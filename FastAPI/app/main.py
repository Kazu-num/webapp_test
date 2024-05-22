from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import base64
from PIL import Image, ImageDraw, ImageFont
import io
import matplotlib.pyplot as plt

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        try:
            # JSON形式でデコードしてファイルメッセージを処理
            message = json.loads(data)
            if message["type"] == "text":
                response = {
                    "type": "text",
                    "content": f"Received: {message['content']}"
                }
                await websocket.send_text(json.dumps(response))
            elif message["type"] == "file":
                if message["filename"].endswith(('.png', '.jpg', '.jpeg')):
                    response = {
                        "type": "image",
                        "content": message["content"]
                    }
                    await websocket.send_text(json.dumps(response))
                elif message["filename"].endswith('.pdf'):
                    response = {
                        "type": "text",
                        "content": f"Received PDF file: {message['filename']}"
                    }
                    await websocket.send_text(json.dumps(response))
                elif message["filename"].endswith('.pptx'):
                    response = {
                        "type": "text",
                        "content": f"Received PowerPoint file: {message['filename']}"
                    }
                    await websocket.send_text(json.dumps(response))
            elif message["type"] == "graph":
                img = generate_graph()
                buffered = io.BytesIO()
                img.save(buffered, format="PNG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                response = {
                    "type": "graph",
                    "content": f"data:image/png;base64,{img_str}"
                }
                await websocket.send_text(json.dumps(response))
        except json.JSONDecodeError:
            response = {
                "type": "text",
                "content": "Error: Unable to parse message"
            }
            await websocket.send_text(json.dumps(response))

def generate_graph():
    plt.figure(figsize=(6, 4))
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
    plt.title('Sample Graph')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = Image.open(buf)
    return img

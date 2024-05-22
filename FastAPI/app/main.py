from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import base64

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
            file_message = json.loads(data)
            if "filename" in file_message and "content" in file_message:
                file_data = base64.b64decode(file_message["content"].split(",")[1])
                response = f"Received file: {file_message['filename']}"
                # ここでファイルデータを保存するなどの処理を行うことができます
                await websocket.send_text(response)
        except json.JSONDecodeError:
            # テキストメッセージとして処理
            response = f"Received: {data}"
            await websocket.send_text(response)

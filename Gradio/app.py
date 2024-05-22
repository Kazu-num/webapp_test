import gradio as gr

# チャット関数
def chat_function(user_input, user_file):
    response = f"You said: {user_input}"
    if user_file is not None:
        response += f"\nAnd you uploaded: {user_file.name}"
    return response

# ログ関数（ダミー）
def log_function():
    # ここにログを表示するための処理を追加
    return "This is a log of your past chats."

# チャットモードの設定
chat_interface = gr.Interface(
    fn=chat_function,
    inputs=[gr.Textbox(lines=2, placeholder="Enter your message here..."), gr.File()],
    outputs="text",
    title="Chat Mode",
    description="A chat application that can process text and file inputs."
)

# ログモードの設定
log_interface = gr.Interface(
    fn=log_function,
    inputs=[],
    outputs="text",
    title="Log Mode",
    description="Displays the chat logs."
)

# タブの設定
with gr.Blocks() as demo:
    with gr.Tabs():
        with gr.TabItem("Chat Mode"):
            chat_interface.render()
        with gr.TabItem("Log Mode"):
            log_interface.render()

# アプリケーションの起動
if __name__ == "__main__":
    demo.launch()

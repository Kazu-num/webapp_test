import gradio as gr

def chat_function(user_input, user_file):
    # ここでPython処理を行う
    response = f"You said: {user_input}"
    
    if user_file is not None:
        response += f"\nAnd you uploaded: {user_file.name}"
    
    return response

# インターフェースの設定
interface = gr.Interface(
    fn=chat_function,
    inputs=[gr.Textbox(lines=2, placeholder="Enter your message here..."), gr.File()],
    outputs="text",
    title="Enhanced Python Chat App",
    description="A chat application that can process text and file inputs."
)

# アプリケーションの起動
if __name__ == "__main__":
    interface.launch()

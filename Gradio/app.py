import gradio as gr

# チャット関数
def chat_function(user_input, user_file):
    response = f"You said: {user_input}"
    if user_file is not None:
        response += f"\nAnd you uploaded: {user_file.name}"
    return response

# ログ関数（ダミー）
def log_function():
    return "This is a log of your past chats."

# コンフィグ関数
def config_function(checkbox, radio, dropdown, slider):
    config_result = (
        f"Checkbox: {'Checked' if checkbox else 'Unchecked'}\n"
        f"Radio: {radio}\n"
        f"Dropdown: {dropdown}\n"
        f"Slider: {slider}"
    )
    return config_result

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

# コンフィグモードの設定
config_interface = gr.Interface(
    fn=config_function,
    inputs=[
        gr.Checkbox(label="Enable feature"),
        gr.Radio(["Option 1", "Option 2", "Option 3"], label="Select an option"),
        gr.Dropdown(["Choice A", "Choice B", "Choice C"], label="Choose from the dropdown"),
        gr.Slider(1, 100, label="Adjust the slider")
    ],
    outputs="text",
    title="Config Mode",
    description="Configuration settings for the chat application."
)

# タブの設定
with gr.Blocks() as demo:
    with gr.Tabs():
        with gr.TabItem("Chat Mode"):
            chat_interface.render()
        with gr.TabItem("Log Mode"):
            log_interface.render()
        with gr.TabItem("Config Mode"):
            config_interface.render()

# アプリケーションの起動
if __name__ == "__main__":
    demo.launch()

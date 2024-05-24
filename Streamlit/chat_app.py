import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt

class ChatApp:
    def __init__(self):
        self.initialize_session_state()
        self.main_ui()

    def initialize_session_state(self):
        if 'messages' not in st.session_state:
            st.session_state['messages'] = []

    def main_ui(self):
        st.title('Python Chat App with Streamlit')

        tab = st.sidebar.radio("モード選択", ["チャット", "設定", "データフレーム"])
        self.sidebar_options()

        if tab == "チャット":
            self.chat_ui()
        elif tab == "設定":
            self.settings_ui()
        elif tab == "データフレーム":
            self.dataframe_ui()

    def sidebar_options(self):
        st.sidebar.header("オプション")
        st.session_state.option = st.sidebar.selectbox('オプションを選択', ('オプション1', 'オプション2', 'オプション3'))
        st.sidebar.write('選択されたオプション:', st.session_state.option)

        if st.sidebar.checkbox('チェックボックスを表示'):
            st.session_state.checkbox = True
            st.sidebar.write('チェックボックスが選択されました')
        else:
            st.session_state.checkbox = False

        st.session_state.radio_option = st.sidebar.radio('ラジオボタンを選択', ['選択肢1', '選択肢2', '選択肢3'])
        st.sidebar.write('選択されたラジオボタン:', st.session_state.radio_option)

        st.session_state.slider_value = st.sidebar.slider('値を選択', 0, 100, 50)
        st.sidebar.write('スライダーの値:', st.session_state.slider_value)

    def chat_ui(self):
        user_text = st.text_input("テキスト入力: ", "")
        user_image = st.file_uploader("画像アップロード", type=["png", "jpg", "jpeg"])
        user_file = st.file_uploader("ファイルアップロード (PDF, PowerPoint)", type=["pdf", "pptx"])

        if st.button('送信'):
            self.process_input(user_text, user_image, user_file)

        st.subheader("チャット履歴")
        for message in st.session_state.messages:
            if 'text' in message:
                st.write(f"**{message['user']} :** {message['text']}")
            elif 'image' in message:
                st.write(f"**{message['user']} が画像をアップロードしました:**")
                st.image(message['image'])
            elif 'file' in message:
                st.write(f"**{message['user']} がファイルをアップロードしました:**")
                st.write(f"[{message['file'].name}](upload/{message['file'].name})")

        if st.button('Pythonプロセスを実行'):
            st.write('Pythonプロセスを実行中...')
            time.sleep(2)
            fig, ax = plt.subplots()
            ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
            ax.set_title('サンプルグラフ')
            st.pyplot(fig)
            st.write('プロセスが完了しました。')

    def settings_ui(self):
        if st.button('設定を確認'):
            st.session_state.messages.append({"user": "ボット", "text": f"選択されたオプション: {st.session_state.option}"})
            st.session_state.messages.append({"user": "ボット", "text": f"チェックボックス: {'選択済み' if st.session_state.checkbox else '未選択'}"})
            st.session_state.messages.append({"user": "ボット", "text": f"ラジオボタン: {st.session_state.radio_option}"})
            st.session_state.messages.append({"user": "ボット", "text": f"スライダーの値: {st.session_state.slider_value}"})

        st.subheader("チャット履歴")
        for message in st.session_state.messages:
            st.write(f"**{message['user']} :** {message['text']}")

    def dataframe_ui(self):
        if st.checkbox('データフレームを表示'):
            data = pd.DataFrame({
                '列1': [1, 2, 3, 4],
                '列2': [10, 20, 30, 40]
            })
            st.write(data)

    def process_input(self, user_text, user_image, user_file):
        if user_text:
            st.session_state.messages.append({"user": "あなた", "text": user_text})
            st.session_state.messages.append({"user": "ボット", "text": f"エコー: {user_text}"})

        if user_image:
            st.session_state.messages.append({"user": "あなた", "image": user_image})
            st.session_state.messages.append({"user": "ボット", "text": "画像がアップロードされました。"})

        if user_file:
            st.session_state.messages.append({"user": "あなた", "file": user_file})
            st.session_state.messages.append({"user": "ボット", "text": f"ファイルがアップロードされました: {user_file.name}"})

if __name__ == "__main__":
    ChatApp()

import streamlit as st
import pandas as pd

class ChatApp:
    def __init__(self):
        self.initialize_session_state()
        self.main_ui()

    def initialize_session_state(self):
        if 'messages' not in st.session_state:
            st.session_state['messages'] = {"チャット1": [], "チャット2": []}
        if 'current_tab' not in st.session_state:
            st.session_state['current_tab'] = 'チャット1'

    def main_ui(self):
        st.set_page_config(
            page_icon="💫",
            page_title="Chat with Echo Bot")

        tab1, tab2 = st.tabs(["チャット1", "チャット2"])

        with tab1:
            st.session_state.current_tab = 'チャット1'
            self.chat_ui('チャット1')

        with tab2:
            st.session_state.current_tab = 'チャット2'
            self.chat_ui('チャット2')

        self.sidebar_options()

    def sidebar_options(self):
        st.sidebar.header("オプション")
        st.session_state.option = st.sidebar.selectbox('オプションを選択', ('オプション1', 'オプション2', 'オプション3'))

        if st.sidebar.checkbox('チェックボックスを表示'):
            st.session_state.checkbox = True
        else:
            st.session_state.checkbox = False

        st.session_state.radio_option = st.sidebar.radio('ラジオボタンを選択', ['選択肢1', '選択肢2', '選択肢3'])

        st.session_state.slider_value = st.sidebar.slider('値を選択', 0, 100, 50)
        st.sidebar.write('スライダーの値:', st.session_state.slider_value)

    def chat_ui(self, tab):
        chat_container = st.container(height=700, border=False)

        # 現在のタブのチャット履歴を取得
        chat_history = st.session_state["messages"][tab]

        # チャット履歴を全て表示
        for message in chat_history:
            with chat_container.chat_message(message["role"]):
                st.markdown(message["content"])

        # ユーザー入力送信後処理
        prompt = st.chat_input("ここに入力してください", key=f"{tab}_input")
        if prompt:
            # ユーザの入力を表示する
            with chat_container.chat_message("user"):
                st.markdown(prompt)

            # ユーザの入力をチャット履歴に追加する
            chat_history.append({"role": "user", "content": prompt})

            # Botの返答を表示する（例としてエコーメッセージを表示）
            with chat_container.chat_message("assistant"):
                st.markdown(f"Echo: {prompt}")

            # Botの返答をチャット履歴に追加する
            chat_history.append({"role": "assistant", "content": f"Echo: {prompt}"})

        # 更新されたチャット履歴をセッション状態に保存
        st.session_state["messages"][tab] = chat_history

if __name__ == "__main__":
    ChatApp()

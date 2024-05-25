import streamlit as st
import pandas as pd

import styles

class ChatApp:
    def __init__(self):
        self.initialize_session_state()
        self.main_ui()

    def initialize_session_state(self):
        if 'messages' not in st.session_state:
            st.session_state['messages'] = {"chat1": [], "chat2": [], "chat3": []}
        if 'current_tab' not in st.session_state:
            st.session_state['current_tab'] = 'chat1'

    def main_ui(self):
        st.set_page_config(**styles.SET_PAGE_CONFIG)
        st.markdown(styles.HIDE_ST_STYLE, unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs(["chat1", "chat2", "chat3"])

        with tab1:
            st.session_state.current_tab = 'chat1'
            self.chat1_ui()

        with tab2:
            st.session_state.current_tab = 'chat2'
            self.chat2_ui()
        
        with tab3:
            st.session_state.current_tab = 'chat3'
            self.chat3_ui()

        self.sidebar_options()

        st.markdown(styles.IMPORTANT_STYLE, unsafe_allow_html=True)

    def chat1_ui(self):
        chat_history = st.session_state["messages"]["chat1"]

        col1, col2 = st.columns([7, 1])
        with col1:
            prompt = st.text_area("入力", height=100, label_visibility="collapsed", key='chat1_text')
            file = st.file_uploader("file upload", accept_multiple_files=False, label_visibility="collapsed", key='chat1_file')

        with col2:
            if st.button("Send", key='chat1_button'):
                if prompt:
                    chat_history.append({"role": "user", "type": "text", "content": prompt})
                    chat_history.append({"role": "assistant", "type": "text", "content": f"Echo: {prompt}"})
                if file:
                    if file.type.startswith('image/'):
                        chat_history.append({"role": "user", "type": "image", "content": file.getvalue()})
                        chat_history.append({"role": "assistant", "type": "text", "content": "きれい！"})
                    else:
                        file_details = {"filename": file.name, "filetype": file.type, "filesize": file.size}
                        chat_history.append({"role": "user", "type": "file_info", "content": file_details})

                st.session_state["messages"]["chat1"] = chat_history

        for message in chat_history:
            with st.chat_message(message["role"]):
                if message["type"] == "text":
                    st.markdown(message["content"])
                elif message["type"] == "image":
                    st.image(message["content"])
                elif message["type"] == "file_info":
                    st.markdown(f"File uploaded: {message['content']}")




    def chat2_ui(self):
        chat_container = st.container(height=640, border=False)
        chat_history = st.session_state["messages"]["chat2"]
        for message in chat_history:
            with chat_container.chat_message(message["role"]):
                st.markdown(message["content"])

        col1, col2 = st.columns([7, 1])

        # 左側のカラムにテキストエリアを配置
        with col1:
            text_area = st.text_area("入力", height=100, label_visibility="collapsed")
            file = st.file_uploader("file upload", accept_multiple_files=False, label_visibility="collapsed")

        # 右側のカラムに送信ボタンを配置
        with col2:
            st.container(height=140, border=False)
            if st.button("Send"):
                if text_area:
                    prompt = text_area
                    with chat_container.chat_message("user"):
                        st.markdown(prompt)

                    chat_history.append({"role": "user", "content": prompt})

                    with chat_container.chat_message("assistant"):
                        st.markdown(f"Echo: {prompt}")

                    chat_history.append({"role": "assistant", "content": f"Echo: {prompt}"})

                    st.session_state["messages"]["chat1"] = chat_history

    def chat3_ui(self):
        chat_container = st.container(height=800, border=False)
        chat_history = st.session_state["messages"]["chat3"]
        for message in chat_history:
            with chat_container.chat_message(message["role"]):
                st.markdown(message["content"])

        prompt = st.chat_input("ここに入力してください")
        if prompt:
            with chat_container.chat_message("user"):
                st.markdown(prompt)

            chat_history.append({"role": "user", "content": prompt})

            with chat_container.chat_message("assistant"):
                st.markdown(f"Echo: {prompt}")

            chat_history.append({"role": "assistant", "content": f"Echo: {prompt}"})

            st.session_state["messages"]["chat2"] = chat_history

    def sidebar_options(self):
        with st.sidebar:
            st.header(
                'Option',
                help='_Streamlit_ is :blue[cool] :sunglasses:')
            with st.expander('commands', expanded=False):
                st.text_area("命令")
                st.text_area("サンプル")
            st.session_state.option = st.sidebar.selectbox('オプションを選択', ('オプション1', 'オプション2', 'オプション3'))

            st.session_state.checkbox = st.sidebar.checkbox('チェックボックスを表示')

            st.session_state.radio_option = st.sidebar.radio('ラジオボタンを選択', ['選択肢1', '選択肢2', '選択肢3'])

            st.session_state.slider_value = st.sidebar.slider('値を選択', 0, 100, 50)

if __name__ == "__main__":
    ChatApp()

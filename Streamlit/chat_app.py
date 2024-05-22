import streamlit as st
import time
import pandas as pd

# セッションステートの初期化
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

st.title('Python Chat App with Streamlit')

# サイドバーでタブを選択
tab = st.sidebar.radio("モード選択", ["チャット", "ファイルアップロード", "データフレーム", "オプション"])

if tab == "チャット":
    # ユーザー入力セクション
    user_input = st.text_input("あなた: ", "")

    # ユーザー入力を処理する関数
    def process_input(user_input):
        if user_input:
            response = f"エコー: {user_input}"  # 簡単なエコーレスポンス
            st.session_state.messages.append({"user": "あなた", "text": user_input})
            st.session_state.messages.append({"user": "ボット", "text": response})

    # ユーザーがEnterキーを押したときに入力を処理
    if user_input:
        process_input(user_input)

    # チャット履歴を表示
    st.subheader("チャット履歴")
    for message in st.session_state.messages:
        if message['user'] == "あなた":
            st.write(f"**{message['user']}:** {message['text']}")
        else:
            st.write(f"*{message['user']}:* {message['text']}")

elif tab == "ファイルアップロード":
    # ファイルアップロードセクション
    uploaded_file = st.file_uploader("ファイルを選択", type=["pdf", "pptx", "txt"])

    if uploaded_file is not None:
        st.write(f"アップロードされたファイル: {uploaded_file.name}")

elif tab == "データフレーム":
    # 追加のUI要素
    if st.checkbox('データフレームを表示'):
        data = pd.DataFrame({
            '列1': [1, 2, 3, 4],
            '列2': [10, 20, 30, 40]
        })
        st.write(data)

elif tab == "オプション":
    option = st.selectbox(
        'オプションを選択',
        ('オプション1', 'オプション2', 'オプション3')
    )

    st.write('選択されたオプション:', option)

    # スライダーの例
    slider_value = st.slider('値を選択', 0, 100, 50)
    st.write('スライダーの値:', slider_value)

    # Pythonプロセスを実行するボタン
    if st.button('Pythonプロセスを実行'):
        st.write('Pythonプロセスを実行中...')
        time.sleep(2)
        st.write('プロセスが完了しました。')

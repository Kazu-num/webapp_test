import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt

# セッションステートの初期化
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

st.title('Python Chat App with Streamlit')

# サイドバーでタブを選択
tab = st.sidebar.radio("モード選択", ["チャット", "ファイルアップロード", "データフレーム", "オプション"])

if tab == "チャット":
    # テキスト入力
    user_text = st.text_input("テキスト入力: ", "")

    # 画像アップロード
    user_image = st.file_uploader("画像アップロード", type=["png", "jpg", "jpeg"])

    # ファイルアップロード (PDF, PowerPoint)
    user_file = st.file_uploader("ファイルアップロード (PDF, PowerPoint)", type=["pdf", "pptx"])

    # ユーザー入力を処理する関数
    def process_input(user_text, user_image, user_file):
        if user_text:
            st.session_state.messages.append({"user": "あなた", "text": user_text})
            st.session_state.messages.append({"user": "ボット", "text": f"エコー: {user_text}"})

        if user_image:
            st.session_state.messages.append({"user": "あなた", "image": user_image})
            st.session_state.messages.append({"user": "ボット", "text": "画像がアップロードされました。"})

        if user_file:
            st.session_state.messages.append({"user": "あなた", "file": user_file})
            st.session_state.messages.append({"user": "ボット", "text": f"ファイルがアップロードされました: {user_file.name}"})

    # ユーザーが入力を送信したときに処理
    if st.button('送信'):
        process_input(user_text, user_image, user_file)

    # チャット履歴を表示
    st.subheader("チャット履歴")
    for message in st.session_state.messages:
        if 'text' in message:
            st.write(f"**{message['user']}:** {message['text']}")
        elif 'image' in message:
            st.write(f"**{message['user']} が画像をアップロードしました:**")
            st.image(message['image'])
        elif 'file' in message:
            st.write(f"**{message['user']} がファイルをアップロードしました:**")
            st.write(f"[{message['file'].name}](upload/{message['file'].name})")

    # Pythonプロセスを実行するボタン
    if st.button('Pythonプロセスを実行'):
        st.write('Pythonプロセスを実行中...')
        # 例として、簡単なグラフを表示
        time.sleep(2)
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
        ax.set_title('サンプルグラフ')
        st.pyplot(fig)
        st.write('プロセスが完了しました。')

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

    # チェックボックスの例
    if st.checkbox('チェックボックスを表示'):
        st.write('チェックボックスが選択されました')

    # ラジオボタンの例
    radio_option = st.radio('ラジオボタンを選択', ['選択肢1', '選択肢2', '選択肢3'])
    st.write('選択されたラジオボタン:', radio_option)

    # スライダーの例
    slider_value = st.slider('値を選択', 0, 100, 50)
    st.write('スライダーの値:', slider_value)

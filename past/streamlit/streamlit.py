import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def sample_1():
    # タイトル
    st.title('Streamlit サンプルアプリケーション')

    # テキスト入力
    name = st.text_input('あなたの名前を入力してください')

    # ボタン
    if st.button('送信'):
        st.write(f'こんにちは、{name}さん！')

def sample_2():
    # タイトル
    st.title('スライダーとグラフの例')

    # スライダー
    x = st.slider('Xの範囲', 0, 100, 50)

    # データ生成
    data = np.linspace(0, x, 100)
    y = np.sin(data)

    # グラフ描画
    fig, ax = plt.subplots()
    ax.plot(data, y)
    st.pyplot(fig)

def sample_3():
    # タイトル
    st.title('ファイルアップロードの例')

    # ファイルアップロード
    uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

    if uploaded_file is not None:
        # ファイルの内容をデータフレームとして読み込む
        df = pd.read_csv(uploaded_file)
        # データフレームを表示
        st.write(df)

def sample_4():
    # セッションステートの初期化
    if 'mode' not in st.session_state:
        st.session_state.mode = 'home'

    # モードを切り替える関数
    def set_mode(new_mode):
        st.session_state.mode = new_mode

    # サイドバーにボタンを配置
    with st.sidebar:
        st.button("ホームモード", on_click=set_mode, args=('home',))
        st.button("設定モード", on_click=set_mode, args=('settings',))

    # モードに応じたUIの表示
    if st.session_state.mode == 'home':
        st.title('ホームモード')
        st.write('これはホームモードです。ここでは主な機能を紹介します。')
        st.image('https://via.placeholder.com/300', caption='Placeholder Image')
    elif st.session_state.mode == 'settings':
        st.title('設定モード')
        st.write('これは設定モードです。ここでは設定を変更できます。')
        option = st.selectbox('オプションを選択してください', ['オプション 1', 'オプション 2', 'オプション 3'])
        st.write(f'選択されたオプション: {option}')

    # アプリケーションの実行
    if __name__ == '__main__':
        st.write('モードに応じたUIが表示されます。サイドバーのボタンをクリックしてモードを切り替えてください。')

def sample_5():
    # タイトル
    st.title('Streamlit 複数モードUIサンプル')

    # モードの選択
    mode = st.sidebar.selectbox('モード選択', ['ホーム', '設定', '情報'])

    # テキスト入力
    text_input = st.sidebar.text_input('テキスト入力')

    # ラジオボタン
    radio_option = st.sidebar.radio('オプションを選択してください', ['オプション 1', 'オプション 2', 'オプション 3'])

    # ドロップダウン
    dropdown_option = st.sidebar.selectbox('ドロップダウンを選択してください', ['選択肢 1', '選択肢 2', '選択肢 3'])

    # 選択されたモードに応じたUI表示
    if mode == 'ホーム':
        st.header('ホームモード')
        st.write('ここはホームモードです。主な機能を紹介します。')
        st.write(f'入力されたテキスト: {text_input}')
        st.write(f'選択されたラジオオプション: {radio_option}')
        st.write(f'選択されたドロップダウンオプション: {dropdown_option}')

    elif mode == '設定':
        st.header('設定モード')
        st.write('ここは設定モードです。設定を変更できます。')
        st.write(f'入力されたテキスト: {text_input}')
        st.write(f'選択されたラジオオプション: {radio_option}')
        st.write(f'選択されたドロップダウンオプション: {dropdown_option}')

    elif mode == '情報':
        st.header('情報モード')
        st.write('ここは情報モードです。詳細情報を表示します。')
        st.write(f'入力されたテキスト: {text_input}')
        st.write(f'選択されたラジオオプション: {radio_option}')
        st.write(f'選択されたドロップダウンオプション: {dropdown_option}')


# sample_1()
# sample_2()
# sample_3()
# sample_4()
sample_5()
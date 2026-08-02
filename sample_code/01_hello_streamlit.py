import streamlit as st

st.set_page_config(page_title="Hello Streamlit", page_icon="🐍")

st.title("PythonのみでWebアプリ入門")
st.subheader("Streamlitを使った画面作成")
st.write("これはStreamlitで作成したWebアプリです。")
st.info("Pythonだけで画面を作成できます。")

st.markdown("""
### 今日学ぶこと
- テキストの表示
- 入力ウィジェット
- CSVデータの読み込み
- 集計とグラフ表示
""")

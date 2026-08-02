import streamlit as st

st.set_page_config(page_title="Session State", page_icon="🧠")
st.title("Session Stateで値を保持する")

if "count" not in st.session_state:
    st.session_state.count = 0

col1, col2, col3 = st.columns(3)

if col1.button("+1"):
    st.session_state.count += 1

if col2.button("-1"):
    st.session_state.count -= 1

if col3.button("リセット"):
    st.session_state.count = 0

st.metric("現在のカウント", st.session_state.count)

st.caption(
    "Streamlitは操作のたびにスクリプトを再実行しますが、"
    "st.session_stateの値は同じセッション内で保持されます。"
)

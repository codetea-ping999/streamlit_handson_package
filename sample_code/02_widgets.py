import streamlit as st

st.set_page_config(page_title="入力UI", page_icon="⌨️")
st.title("入力ウィジェットを使ってみよう")

name = st.text_input("名前を入力してください")
age = st.slider("年齢", min_value=18, max_value=70, value=30)
department = st.selectbox(
    "部署を選択してください",
    ["営業", "開発", "総務", "製造", "品質保証"],
)
interests = st.multiselect(
    "興味のあるテーマ",
    ["データ分析", "業務自動化", "生成AI", "Webアプリ", "クラウド"],
)
show_detail = st.checkbox("入力内容の詳細を表示する")

if st.button("実行"):
    if not name.strip():
        st.warning("名前を入力してください。")
    else:
        st.success(f"{name}さん、ようこそ！")
        st.write(f"所属部署: {department}")
        st.write(f"年齢: {age}歳")
        if show_detail:
            st.write("興味のあるテーマ:", interests or "未選択")

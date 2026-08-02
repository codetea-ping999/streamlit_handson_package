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

# 演習：以下を追加
years_of_experience = st.number_input("経験年数", min_value=0, max_value=50, value=0)
learning_purpose = st.text_area("受講目的を入力してください")

if st.button("実行"):
    if not name.strip():
        st.warning("名前を入力してください。")
    else:
        st.success(f"{name}さん、ようこそ！")
        st.write(f"所属部署: {department}")
        st.write(f"年齢: {age}歳")
        if show_detail:
            st.write("興味のあるテーマ:", interests or "未選択")

        # 演習：json()で入力内容を表示
        st.json({
            "名前": name,
            "年齢": age,
            "部署": department,
            "経験年数": years_of_experience,
            "受講目的": learning_purpose,
            "興味のあるテーマ": interests,
        })

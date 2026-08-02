from datetime import date

import streamlit as st

st.set_page_config(page_title="業務日報フォーム", page_icon="📝")
st.title("業務日報入力アプリ")

with st.form("daily_report", clear_on_submit=False):
    report_date = st.date_input("日付", value=date.today())
    name = st.text_input("氏名")
    department = st.selectbox(
        "部署",
        ["営業", "開発", "総務", "製造", "品質保証"],
    )
    work = st.text_area("本日の作業内容")
    issue = st.text_area("課題・困りごと")
    submitted = st.form_submit_button("登録")

if submitted:
    if not name.strip() or not work.strip():
        st.error("氏名と作業内容は必須です。")
    else:
        st.success("日報を受け付けました。")
        st.write("#### 入力内容")
        st.write({
            "日付": str(report_date),
            "氏名": name,
            "部署": department,
            "作業内容": work,
            "課題": issue or "なし",
        })

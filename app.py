import streamlit as st

st.set_page_config(
    page_title="Streamlit ハンズオン",
    page_icon=":material/home:",
    layout="wide",
)

# Define navigation with sections
pages = {
    "": [
        st.Page("app_pages/home.py", title="ホーム", icon=":material/home:"),
    ],
    "基礎講座": [
        st.Page("app_pages/01_hello_streamlit.py", title="01 Hello Streamlit", icon=":material/rocket:"),
        st.Page("app_pages/02_widgets.py", title="02 入力UI", icon=":material/input:"),
        st.Page("app_pages/03_csv_upload.py", title="03 CSV読込", icon=":material/upload:"),
    ],
    "応用講座": [
        st.Page("app_pages/04_sales_dashboard.py", title="04 売上分析", icon=":material/bar_chart:"),
        st.Page("app_pages/05_form.py", title="05 フォーム", icon=":material/description:"),
    ],
    "高度な機能": [
        st.Page("app_pages/06_session_state.py", title="06 セッション状態", icon=":material/memory:"),
        st.Page("app_pages/07_cache.py", title="07 キャッシュ", icon=":material/bolt:"),
    ],
    "完成版プロジェクト": [
        st.Page("app_pages/08_weather_app.py", title="08 天気予報アプリ", icon=":material/cloud:"),
        st.Page("app_pages/09_inventory_system.py", title="09 在庫管理システム", icon=":material/inventory_2:"),
        st.Page("app_pages/10_customer_analytics.py", title="10 顧客分析ダッシュボード", icon=":material/people:"),
    ]
}

page = st.navigation(pages, position="sidebar")
page.run()

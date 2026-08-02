from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="売上分析アプリ",
    page_icon="📊",
    layout="wide",
)

@st.cache_data
def load_csv(file_or_path) -> pd.DataFrame:
    """CSVを読み込み、必要な列とデータ型を検証する。"""
    df = pd.read_csv(file_or_path)
    required_columns = {"日付", "部署", "担当者", "売上", "件数", "商品カテゴリ"}
    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"不足している列: {', '.join(sorted(missing))}")

    df["日付"] = pd.to_datetime(df["日付"], errors="coerce")
    df["売上"] = pd.to_numeric(df["売上"], errors="coerce")
    df["件数"] = pd.to_numeric(df["件数"], errors="coerce")
    return df.dropna(subset=["日付", "部署", "売上", "件数"])

st.title("売上分析アプリ")
st.write("CSVファイルを読み込み、部署別・日別の売上を確認します。")

uploaded_file = st.sidebar.file_uploader("CSVファイル", type=["csv"])
use_sample = st.sidebar.checkbox("サンプルCSVを使用する", value=uploaded_file is None)

try:
    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        data_source = "アップロードファイル"
    elif use_sample:
        sample_path = Path(__file__).resolve().parent / "data" / "sample_sales.csv"
        df = load_csv(sample_path)
        data_source = "教材付属サンプルCSV"
    else:
        st.info("CSVをアップロードするか、サンプルCSVを使用してください。")
        st.stop()
except (FileNotFoundError, ValueError, pd.errors.ParserError) as exc:
    st.error(f"CSVを読み込めませんでした: {exc}")
    st.stop()

st.sidebar.success(f"データソース: {data_source}")

all_departments = sorted(df["部署"].dropna().unique().tolist())
selected_departments = st.sidebar.multiselect(
    "部署",
    all_departments,
    default=all_departments,
)

min_date = df["日付"].min().date()
max_date = df["日付"].max().date()
selected_period = st.sidebar.date_input(
    "対象期間",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

filtered_df = df[df["部署"].isin(selected_departments)].copy()
if isinstance(selected_period, (tuple, list)) and len(selected_period) == 2:
    start_date, end_date = selected_period
    filtered_df = filtered_df[
        filtered_df["日付"].dt.date.between(start_date, end_date)
    ]

if filtered_df.empty:
    st.warning("条件に一致するデータがありません。")
    st.stop()

total_sales = int(filtered_df["売上"].sum())
total_count = int(filtered_df["件数"].sum())
average_per_case = int(total_sales / total_count) if total_count else 0

col1, col2, col3 = st.columns(3)
col1.metric("合計売上", f"{total_sales:,}円")
col2.metric("合計件数", f"{total_count:,}件")
col3.metric("1件あたり売上", f"{average_per_case:,}円")

tab1, tab2, tab3 = st.tabs(["ダッシュボード", "データ明細", "操作メモ"])

with tab1:
    left, right = st.columns(2)

    with left:
        st.subheader("部署別売上")
        department_summary = (
            filtered_df.groupby("部署")["売上"].sum().sort_values(ascending=False)
        )
        st.bar_chart(department_summary)

    with right:
        st.subheader("商品カテゴリ別売上")
        category_summary = (
            filtered_df.groupby("商品カテゴリ")["売上"].sum().sort_values(ascending=False)
        )
        st.bar_chart(category_summary)

    st.subheader("日別売上推移")
    daily_summary = filtered_df.groupby("日付")["売上"].sum().sort_index()
    st.line_chart(daily_summary)

with tab2:
    display_df = filtered_df.copy()
    display_df["日付"] = display_df["日付"].dt.strftime("%Y-%m-%d")
    st.dataframe(display_df, use_container_width=True, hide_index=True)

    csv_bytes = display_df.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "絞り込み結果をCSVでダウンロード",
        data=csv_bytes,
        file_name="filtered_sales.csv",
        mime="text/csv",
    )

with tab3:
    st.markdown("""
    ### このアプリで確認できるStreamlitの機能
    - `st.file_uploader`：CSVアップロード
    - `st.sidebar`：条件指定
    - `st.multiselect` / `st.date_input`：フィルタ入力
    - `st.metric`：主要指標
    - `st.bar_chart` / `st.line_chart`：グラフ表示
    - `st.tabs` / `st.columns`：レイアウト
    - `st.cache_data`：CSV読み込みのキャッシュ
    - `st.download_button`：集計結果の出力
    """)

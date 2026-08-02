from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="売上ダッシュボード", page_icon="📊", layout="wide")
st.title("売上分析ダッシュボード")

sample_path = Path(__file__).resolve().parents[1] / "data" / "sample_sales.csv"
df = pd.read_csv(sample_path, parse_dates=["日付"])

departments = sorted(df["部署"].unique())
selected = st.sidebar.multiselect("部署で絞り込み", departments, default=departments)
filtered_df = df[df["部署"].isin(selected)]

if filtered_df.empty:
    st.warning("表示対象の部署を1つ以上選択してください。")
    st.stop()

total_sales = int(filtered_df["売上"].sum())
total_count = int(filtered_df["件数"].sum())
average_sales = int(filtered_df["売上"].mean())

col1, col2, col3 = st.columns(3)
col1.metric("合計売上", f"{total_sales:,}円")
col2.metric("合計件数", f"{total_count:,}件")
col3.metric("1行あたり平均売上", f"{average_sales:,}円")

st.subheader("部署別売上")
department_summary = filtered_df.groupby("部署")["売上"].sum().sort_values(ascending=False)
st.bar_chart(department_summary)

st.subheader("日別売上")
daily_summary = filtered_df.groupby("日付")["売上"].sum()
st.line_chart(daily_summary)

st.subheader("明細")
st.dataframe(filtered_df, use_container_width=True, hide_index=True)

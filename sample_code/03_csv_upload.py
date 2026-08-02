from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="CSVアップロード", page_icon="📄", layout="wide")
st.title("CSVデータを表示してみよう")

uploaded_file = st.file_uploader("CSVファイルを選択してください", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success(f"{len(df)}件のデータを読み込みました。")
    st.dataframe(df, use_container_width=True)
else:
    st.info("CSVを選択していないため、教材付属のサンプルCSVを表示します。")
    sample_path = Path(__file__).resolve().parents[1] / "data" / "sample_sales.csv"
    if sample_path.exists():
        df = pd.read_csv(sample_path)
        st.dataframe(df, use_container_width=True)
    else:
        st.error("data/sample_sales.csv が見つかりません。")

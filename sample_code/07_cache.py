from pathlib import Path
import time

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Cache", page_icon="⚡")
st.title("Cacheで重い処理を省略する")

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    # 重い処理を模擬するため2秒待機します。
    time.sleep(2)
    return pd.read_csv(path, parse_dates=["日付"])

sample_path = Path(__file__).resolve().parents[1] / "data" / "sample_sales.csv"

start = time.perf_counter()
df = load_data(str(sample_path))
elapsed = time.perf_counter() - start

st.write(f"読み込み時間: {elapsed:.3f}秒")
st.dataframe(df, use_container_width=True)
st.info("同じ条件で再実行すると、2回目以降はキャッシュが利用されます。")

if st.button("キャッシュを削除"):
    st.cache_data.clear()
    st.success("キャッシュを削除しました。次回は再読み込みされます。")

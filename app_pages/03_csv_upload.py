from pathlib import Path

import pandas as pd
import streamlit as st

st.title("CSVデータを表示してみよう")

st.markdown("""
## 📌 このレッスンについて

実際のWebアプリケーションでは、ユーザーが持つCSVファイルを
アップロードして処理することがよくあります。

このレッスンでは、ファイルアップロード機能を使って、
CSVデータを読み込み、表形式で表示する方法を学びます。

### 学習目標
- ✅ ファイルアップロード機能を実装する
- ✅ CSVファイルをPandasで読み込む
- ✅ DataFrameをStreamlitで表示する
- ✅ データの行数や列数を確認する

---

## 📁 ファイルアップロード (`st.file_uploader`)

ファイルをアップロードするUIを提供します。
""")

st.code("""
uploaded_file = st.file_uploader(
    "CSVファイルを選択してください",
    type=["csv"]  # CSV形式のみ受け付ける
)

if uploaded_file is not None:
    # ファイルが選択された場合
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
else:
    # ファイルが選択されていない場合
    st.info("ファイルを選択してください")
""", language="python")

st.info("""
💡 **`type=["csv"]` について：**
- 許可するファイル形式を指定します
- `type=["csv", "xlsx"]` とすることで複数形式に対応できます
- 指定しない場合は、すべてのファイル形式を受け付けます
""")

st.divider()

st.markdown("""
## 🔍 実際に試してみよう

### オプション1: CSVファイルをアップロード

下のボタンをクリックして、あなたのCSVファイルをアップロードしてください。
""")

uploaded_file = st.file_uploader("📤 CSVファイルを選択してください", type=["csv"])

if uploaded_file is not None:
    st.markdown("### ✅ ファイルアップロード完了")

    try:
        df = pd.read_csv(uploaded_file)

        # ファイル情報を表示
        col1, col2, col3 = st.columns(3)
        col1.metric("行数", len(df))
        col2.metric("列数", len(df.columns))
        col3.metric("ファイルサイズ", f"{uploaded_file.size / 1024:.1f} KB")

        st.success(f"✅ {len(df)}件のデータを読み込みました。")

        st.markdown("### 📊 データプレビュー")
        st.dataframe(df, width="stretch", use_container_width=True)

        # 列情報を表示
        st.markdown("### 📋 列の情報")
        st.write(df.dtypes)

        # 基本統計量
        st.markdown("### 📈 基本統計量")
        st.dataframe(df.describe(), width="stretch")

    except Exception as e:
        st.error(f"❌ ファイルの読み込みに失敗しました: {e}")

else:
    st.markdown("""
    ### 📌 または、サンプルデータを使用

    下のボタンをクリックすると、教材付属のサンプルCSVが表示されます。
    """)

st.divider()

st.markdown("### 🎓 サンプルデータの表示")

sample_path = Path(__file__).resolve().parent.parent / "data" / "sample_sales.csv"

if st.button("📊 サンプルデータを読み込む"):
    if sample_path.exists():
        df = pd.read_csv(sample_path)

        st.markdown("### 📈 サンプル売上データ")
        st.info("このデータは教材に付属する売上データです。")

        # データの概要
        col1, col2, col3 = st.columns(3)
        col1.metric("行数", len(df))
        col2.metric("列数", len(df.columns))
        col3.metric("期間", f"{df.columns[0]} ～ {df.columns[-1]}")

        st.dataframe(df, width="stretch", use_container_width=True)

        # 列の説明
        st.markdown("### 📝 データの説明")
        st.markdown("""
        - **日付** - 取引日
        - **部署** - 営業が行われた部署（営業、開発、総務など）
        - **担当者** - 担当した人名
        - **売上** - 売上金額（円）
        - **件数** - 取引件数
        - **商品カテゴリ** - 商品の分類
        """)

        # データの統計
        st.markdown("### 📊 売上の統計")
        if "売上" in df.columns:
            st.write(f"総売上: ¥{df['売上'].sum():,}")
            st.write(f"平均売上: ¥{df['売上'].mean():,.0f}")
            st.write(f"最大売上: ¥{df['売上'].max():,}")
            st.write(f"最小売上: ¥{df['売上'].min():,}")
    else:
        st.error("❌ data/sample_sales.csv が見つかりません。")

st.divider()

st.markdown("""
## 📚 PandasとDataFrameについて

### DataFrameとは？

DataFrameは、Pandasライブラリの基本的なデータ構造で、
Excelの表やデータベースのテーブルのようなものです。

```python
# CSVを読み込むと、DataFrameが返される
df = pd.read_csv("data.csv")

# DataFrameの最初の5行を表示
df.head()

# 行数と列数を取得
len(df)  # 行数
len(df.columns)  # 列数

# 特定の列にアクセス
df["列名"]

# 統計情報を取得
df.describe()
```

### Streamlitでの表示

```python
# 通常の表示
st.dataframe(df)

# 全幅を使用して表示
st.dataframe(df, width="stretch")

# 行番号を非表示にする
st.dataframe(df, hide_index=True)
```

---

## 💡 実装のコツ

### ✅ エラー処理を含める
```python
try:
    df = pd.read_csv(uploaded_file)
    st.success("読み込み成功")
except Exception as e:
    st.error(f"エラー: {e}")
```

### ✅ ファイル情報を表示する
```python
st.write(f"ファイルサイズ: {len(df)} 行")
st.write(f"列: {', '.join(df.columns)}")
```

### ✅ サンプルデータでテストする
ユーザーが簡単にテストできるように、
サンプルCSVを提供することをお勧めします。

---

## 📚 次のステップ

**次のレッスン「04 売上分析」では：**
- 読み込んだデータをフィルタリングする
- グラフやチャートで可視化する
- ダッシュボードを作成する

**このレッスンのポイント:**
1. `st.file_uploader()` でファイルアップロードUI
2. `pd.read_csv()` でCSVをDataFrameに
3. `st.dataframe()` でDataFrameを表示
4. 常に **エラー処理** を含める

---

**💻 今すぐやってみよう！**

1. 上でサンプルデータボタンをクリックしてみてください
2. 自分のCSVファイルがあれば、アップロードしてみてください
3. ファイル情報や統計情報がどのように表示されるか確認しましょう
""")

from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
st.title("売上分析ダッシュボード")

st.markdown("""
## 📌 このレッスンについて

これまでのレッスンで学んだ知識を組み合わせて、
実際に使えるダッシュボードを作成します。

ダッシュボードとは、重要な情報を一目で理解できるように
複数のグラフや表を組み合わせた画面です。

### 学習目標
- ✅ サイドバーでのフィルタリング
- ✅ メトリクスの表示（st.metric）
- ✅ グラフの作成（棒グラフ、折れ線グラフ）
- ✅ データの集計（Pandas groupby）
- ✅ レイアウトの工夫（列、タブなど）

---

## 🎯 ダッシュボードの構成

このダッシュボードには以下の要素が含まれます：

1. **フィルタ** - 部署を選択して表示データを絞る
2. **KPI（重要指標）** - 合計売上、件数などの主要指標
3. **グラフ** - 部署別の売上、日別の推移
4. **データ表** - 詳細な取引データ

---

## 💡 実装の流れ

### ステップ1: データの読み込み
""")

st.code("""
import pandas as pd

# CSVを読み込む
df = pd.read_csv("sample_sales.csv", parse_dates=["日付"])
""", language="python")

st.markdown("""
### ステップ2: サイドバーでのフィルタリング
""")

st.code("""
# 部署のリストを取得
departments = sorted(df["部署"].unique())

# サイドバーでマルチセレクトを表示
selected = st.sidebar.multiselect(
    "部署で絞り込み",
    departments,
    default=departments  # 最初はすべて選択された状態
)

# 選択された部署のみに絞る
filtered_df = df[df["部署"].isin(selected)]
""", language="python")

st.markdown("""
**`st.sidebar`について：**
- `st.sidebar.xxx()` でサイドバーにウィジェットを配置
- ページレイアウトがすっきりする
- フィルタなどのコントロールに向いている

### ステップ3: メトリクスの表示
""")

st.code("""
# 重要指標を計算
total_sales = int(filtered_df["売上"].sum())
total_count = int(filtered_df["件数"].sum())

# 3列に並べて表示
col1, col2, col3 = st.columns(3)
col1.metric("合計売上", f"{total_sales:,}円")
col2.metric("合計件数", f"{total_count:,}件")
col3.metric("平均売上", f"{average_sales:,}円")
""", language="python")

st.markdown("""
**`st.metric()`について：**
- 大きく表示される数字用
- ダッシュボードのKPI表示に最適
- 前年度との比較などの増減表示も可能

### ステップ4: グラフの表示
""")

st.code("""
# 部署別に集計
department_summary = filtered_df.groupby("部署")["売上"].sum()
st.bar_chart(department_summary)

# 日別に集計
daily_summary = filtered_df.groupby("日付")["売上"].sum()
st.line_chart(daily_summary)
""", language="python")

st.markdown("""
**`groupby`について：**
- Pandasの集計機能
- 特定の列で分類して、別の列を集計
- `groupby("部署")["売上"].sum()` = 部署ごとの売上合計

---

## 📊 実際のダッシュボード

以下が実際に動作するダッシュボードです。
左のサイドバーで部署をフィルタして、データがどのように変わるか観察してください。
""")

st.divider()

# データ読み込み
sample_path = Path(__file__).resolve().parent.parent / "data" / "sample_sales.csv"
df = pd.read_csv(sample_path, parse_dates=["日付"])

# サイドバーでフィルタリング
departments = sorted(df["部署"].unique())
selected = st.sidebar.multiselect("🏢 部署で絞り込み", departments, default=departments)
filtered_df = df[df["部署"].isin(selected)]

# データが空でないか確認
if filtered_df.empty:
    st.warning("⚠️ 表示対象の部署を1つ以上選択してください。")
    st.stop()

# KPI計算
total_sales = int(filtered_df["売上"].sum())
total_count = int(filtered_df["件数"].sum())
average_sales = int(filtered_df["売上"].mean())

# メトリクス表示
st.markdown("### 📈 主要指標（KPI）")
col1, col2, col3 = st.columns(3)
col1.metric("💰 合計売上", f"{total_sales:,}円")
col2.metric("📊 合計件数", f"{total_count:,}件")
col3.metric("💹 1件あたり平均売上", f"{average_sales:,}円")

st.divider()

# グラフ
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.markdown("### 📊 部署別売上")
    department_summary = filtered_df.groupby("部署")["売上"].sum().sort_values(ascending=False)
    st.bar_chart(department_summary)

with col_chart2:
    st.markdown("### 💹 商品カテゴリ別売上")
    if "商品カテゴリ" in filtered_df.columns:
        category_summary = filtered_df.groupby("商品カテゴリ")["売上"].sum().sort_values(ascending=False)
        st.bar_chart(category_summary)

st.divider()

st.markdown("### 📈 日別売上推移")
daily_summary = filtered_df.groupby("日付")["売上"].sum().sort_index()
st.line_chart(daily_summary)

st.divider()

# データテーブル
st.markdown("### 📋 取引明細データ")

# 表示カラムの選択
show_columns = st.multiselect(
    "表示する列を選択（デフォルトはすべて表示）",
    filtered_df.columns.tolist(),
    default=filtered_df.columns.tolist()
)

# カラムが選択されているか確認
if show_columns:
    display_df = filtered_df[show_columns].copy()
else:
    display_df = filtered_df.copy()

st.dataframe(display_df, width="stretch", hide_index=True)

st.divider()

st.markdown("""
## 💡 ダッシュボード設計のコツ

### ✅ 良い設計
```python
# 1. フィルタを用意（サイドバー）
# 2. KPIを大きく表示
# 3. グラフで全体像を表示
# 4. 詳細データはテーブルで表示
```

### ⚡ パフォーマンス最適化
```python
# 重いデータ読み込みはキャッシュする
@st.cache_data
def load_data():
    return pd.read_csv("large_file.csv")

df = load_data()  # 初回のみ読み込み、以降はキャッシュから
```

### 📐 レイアウトのコツ
```python
# 複数のグラフを横並びに
col1, col2 = st.columns(2)
with col1:
    st.bar_chart(data1)
with col2:
    st.bar_chart(data2)

# タブで情報を分類
tab1, tab2, tab3 = st.tabs(["概要", "詳細", "設定"])
with tab1:
    st.write("概要情報")
with tab2:
    st.dataframe(df)
```

---

## 📚 よく使う集計パターン

### 合計を計算
```python
total = df["売上"].sum()
```

### 平均を計算
```python
average = df["売上"].mean()
```

### グループごとに集計
```python
group_summary = df.groupby("部署")["売上"].sum()
```

### 複数の列で集計
```python
multi_group = df.groupby(["日付", "部署"])["売上"].sum()
```

---

## 🎓 次のレッスン

**次は「05 フォーム」で学ぶこと：**
- フォーム要素をまとめて処理する
- 送信ボタンで一括入力する
- データの保存や送信を模擬する

**このレッスンのポイント:**
1. `st.sidebar` でスッキリしたレイアウト
2. `st.metric()` でKPI表示
3. `groupby()` でデータ集計
4. グラフと表で多角的にデータを表示

---

**💻 今すぐやってみよう！**

1. 左のサイドバーで異なる部署を選択して、グラフが変わるか確認
2. 表示する列を変更して、データテーブルがどう変わるか試す
3. 新しい集計方法を試してみる（例：商品カテゴリ別など）
""")

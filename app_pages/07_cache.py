from pathlib import Path
import time

import pandas as pd
import streamlit as st

st.title("Cacheで重い処理を省略する")

st.markdown("""
## 📌 このレッスンについて

Streamlitはウィジェット操作のたびにスクリプトを再実行します。
毎回重い処理（データ読み込み、機械学習など）を実行すると、
アプリが遅くなってしまいます。

このレッスンでは、計算結果を**キャッシュ**して、
不要な再計算を避ける方法を学びます。

### 学習目標
- ✅ キャッシュの概念を理解する
- ✅ `@st.cache_data` でデータ処理をキャッシュ
- ✅ `@st.cache_resource` で共有リソースをキャッシュ
- ✅ キャッシュの有効期限を管理する

---

## ⚡ キャッシュとは？

### 問題: キャッシュなし

```python
# このコードは操作のたびに実行される
def load_large_file():
    time.sleep(5)  # 5秒かかる重い処理
    return pd.read_csv("large_data.csv")

df = load_large_file()
st.dataframe(df)

# ユーザーが何かをクリックするたびに5秒待たされる ❌
```

### 解決: キャッシュを使う

```python
@st.cache_data
def load_large_file():
    time.sleep(5)  # 初回のみ実行
    return pd.read_csv("large_data.csv")

df = load_large_file()
st.dataframe(df)

# 2回目以降は瞬時に実行される ✅
```

---

## 🎯 2つのキャッシュデコレータ

### 1. `@st.cache_data`

**用途:** 関数の**戻り値**（データ）をキャッシュ

```python
@st.cache_data
def load_csv(path: str):
    return pd.read_csv(path)

@st.cache_data
def process_data(df):
    return df.groupby("category").sum()

@st.cache_data
def fetch_api_data(url):
    import requests
    return requests.get(url).json()
```

**キャッシュの有効期限:**
- デフォルト: Streamlitプロセスの実行中
- TTL設定で期限を指定可能

### 2. `@st.cache_resource`

**用途:** **オブジェクト**（リソース）をキャッシュ

```python
@st.cache_resource
def get_database_connection():
    import sqlite3
    return sqlite3.connect("db.sqlite")

@st.cache_resource
def load_ml_model():
    import tensorflow as tf
    return tf.keras.models.load_model("model.h5")

@st.cache_resource
def get_api_client():
    import requests
    return requests.Session()
```

### 使い分け

| 対象 | デコレータ | 例 |
|-----|---------|-----|
| **データ（可変）** | `@st.cache_data` | DataFrameを読み込む |
| **リソース（不変）** | `@st.cache_resource` | DB接続、ML モデル |
| **画像、ファイル** | `@st.cache_data` | 画像ファイル |

---

## 📊 実践: パフォーマンス比較

以下のデモでキャッシュの効果を実感してください。
""")

st.divider()

st.markdown("""
### 🔍 実験方法

1. **初回実行** - 「データを読み込む」をクリック
   - 読み込み時間: **2秒**（遅い）

2. **2回目実行** - 再度クリック
   - 読み込み時間: **0秒前後**（高速）
   - 理由：キャッシュから取得

3. **キャッシュクリア** - 「キャッシュを削除」をクリック
   - キャッシュがリセット

4. **3回目実行** - 再度「データを読み込む」をクリック
   - 読み込み時間: **2秒**（また遅い）
   - 理由：キャッシュが削除されたので再計算

---

### 📈 デモ
""")

# キャッシュ関数の定義
@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    # 重い処理を模擬するため2秒待機
    time.sleep(2)
    return pd.read_csv(path, parse_dates=["日付"])

sample_path = Path(__file__).resolve().parent.parent / "data" / "sample_sales.csv"

# ボタンをクリックして実行
if st.button("📥 データを読み込む"):
    st.info("💾 読み込み中... 初回は2秒かかります")

    start = time.perf_counter()
    df = load_data(str(sample_path))
    elapsed = time.perf_counter() - start

    # 実行時間を表示
    if elapsed < 0.1:
        st.success(f"⚡ 読み込み完了（キャッシュから取得）: {elapsed:.3f}秒")
    else:
        st.warning(f"⏳ 読み込み完了（新規取得）: {elapsed:.3f}秒")

    # データを表示
    st.dataframe(df.head(10), width="stretch", use_container_width=True)

    # 統計情報
    st.markdown("### 📊 データ統計")
    col1, col2, col3 = st.columns(3)
    col1.metric("行数", len(df))
    col2.metric("列数", len(df.columns))
    col3.metric("メモリ使用量", f"{df.memory_usage().sum() / 1024:.1f} KB")

st.divider()

st.markdown("### 🗑️ キャッシュ管理")

if st.button("🔄 キャッシュを削除"):
    st.cache_data.clear()
    st.success("✅ キャッシュを削除しました。次回は再読み込みされます。")

st.divider()

st.markdown("""
## 💻 コード実装例

### パターン1: 基本的なキャッシュ

```python
@st.cache_data
def load_csv(filename):
    return pd.read_csv(filename)

df = load_csv("data.csv")
st.dataframe(df)
```

### パターン2: 引数が異なる場合

```python
@st.cache_data
def process_data(filename, column):
    df = pd.read_csv(filename)
    return df.groupby(column).sum()

# 異なる引数で呼び出すと、別々にキャッシュされる
df1 = process_data("sales.csv", "department")  # キャッシュA
df2 = process_data("sales.csv", "region")      # キャッシュB
```

**重要:** キャッシュの鍵は**引数**です。
異なる引数で呼ぶと、新しいキャッシュが作成されます。

### パターン3: 有効期限を設定

```python
@st.cache_data(ttl=3600)  # 1時間キャッシュ
def fetch_weather():
    import requests
    return requests.get("https://api.weather.com").json()
```

### パターン4: リソースのキャッシュ

```python
@st.cache_resource
def get_database():
    import sqlite3
    return sqlite3.connect("data.db")

# すべての関数で同じDB接続を使用
db = get_database()
```

---

## ⚠️ キャッシュ時の注意点

### ❌ キャッシュしてはいけない場合

```python
# ❌ 時間によって結果が変わる（キャッシュ不適切）
@st.cache_data
def get_current_time():
    return datetime.datetime.now()
```

### ✅ 適切にキャッシュする場合

```python
# ✅ 毎回同じ結果が返される（キャッシュ推奨）
@st.cache_data
def calculate_pi():
    return 3.14159265359
```

### ⚠️ mutable（変更可能）なオブジェクトに注意

```python
@st.cache_data
def get_list():
    return [1, 2, 3]

# キャッシュされたリストを変更しない！
lst = get_list()
lst.append(4)  # ❌ キャッシュ内のオブジェクトが変更される
```

---

## 📊 パフォーマンス実測

一般的なシナリオでの高速化の例：

| 処理内容 | キャッシュなし | キャッシュあり | 高速化倍率 |
|---------|-------------|------------|---------|
| CSV読み込み（1GB） | 5秒 | 0.1秒 | **50倍** |
| ML推論（画像） | 3秒 | 0.05秒 | **60倍** |
| API呼び出し | 2秒 | 0.01秒 | **200倍** |
| データ集計 | 1秒 | 0.01秒 | **100倍** |

---

## 🎓 ベストプラクティス

### ✅ キャッシュの使い方

```python
# 1. 重い処理は関数に切り出す
@st.cache_data
def load_and_process():
    df = pd.read_csv("large_file.csv")
    return df.groupby("category").sum()

# 2. サイドバーでのフィルタは キャッシュ外
df = load_and_process()  # キャッシュ
filtered = df[df["value"] > 100]  # キャッシュ外（毎回実行）

# 3. 有効期限を設定（必要に応じて）
@st.cache_data(ttl=3600)
def fetch_external_data():
    # 外部APIから1時間ごとに更新
    pass
```

### 💡 アプリの高速化の流れ

1. **遅い部分を特定** - 実行時間を計測
2. **関数に切り出す** - 重い処理を関数化
3. **デコレータを追加** - `@st.cache_data` または `@st.cache_resource`
4. **テストして確認** - 2回目の実行が高速化されているか確認

---

## 📚 次のステップ

### 学習完了！🎉

これで基本的なStreamlitの機能をすべて学びました。

次は、実際のプロジェクトで応用してみましょう：

1. **ファイルアップロード + 分析**
   - CSVをアップロット → データ分析 → グラフ表示

2. **Webスクレイピング**
   - 外部サイトからデータを取得 → キャッシュで高速化

3. **機械学習アプリ**
   - モデルをキャッシュ → 予測結果を表示

4. **マルチページアプリ**
   - ホーム、分析、設定などの複数ページ

---

**このレッスンのポイント:**
1. `@st.cache_data` でデータを高速化
2. `@st.cache_resource` でリソースを共有
3. **キャッシュの鍵は引数**（異なる引数で別キャッシュ）
4. 不適切なキャッシュはパフォーマンス低下につながる

---

**💻 今すぐやってみよう！**

1. 「データを読み込む」ボタンを複数回クリック
2. 最初と2回目の実行時間の違いを観察
3. 「キャッシュを削除」してリセット
4. 自分のプロジェクトで遅い処理を見つけてキャッシュに変えてみる

---

## 🏆 すべてのレッスン完了です！

おめでとうございます🎉

学んだこと：
- ✅ 01: テキスト表示とMarkdown
- ✅ 02: 入力ウィジェット
- ✅ 03: ファイルアップロードとデータ処理
- ✅ 04: ダッシュボード作成
- ✅ 05: フォーム実装
- ✅ 06: Session State による状態管理
- ✅ 07: キャッシュによるパフォーマンス最適化

**次のステップ:**
- 複数ページのアプリを作成してみよう
- 外部データソース（API、DB）を接続してみよう
- コミュニティテンプレートを参考にしよう

**参考資料:**
- [Streamlit公式ドキュメント](https://docs.streamlit.io/)
- [Streamlit コミュニティフォーラム](https://discuss.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
""")

if st.button("キャッシュを削除"):
    st.cache_data.clear()
    st.success("キャッシュを削除しました。次回は再読み込みされます。")

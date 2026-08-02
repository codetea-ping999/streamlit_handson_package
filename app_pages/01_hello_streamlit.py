import streamlit as st

st.title("PythonのみでWebアプリ入門")
st.subheader("Streamlitを使った画面作成")

st.markdown("""
## 📌 このレッスンについて

Streamlitは、**Pythonのみ**でWebアプリケーションを構築できるオープンソースの
アプリケーションフレームワークです。HTMLやJavaScript、CSSの知識がなくても、
Pythonの知識だけで美しいWebアプリを作成できます。

### 学習目標
このレッスンを終了後、以下ができるようになります：
- ✅ Streamlitの基本的な使い方を理解する
- ✅ テキスト、タイトル、サブタイトルを表示する
- ✅ 情報メッセージ、警告、エラーを表示する
- ✅ Markdownでリッチテキストを作成する

---

## 💡 Streamlitの特徴

### 1. シンプルなPythonコード
```python
import streamlit as st
st.title("Hello Streamlit")
```
これだけで、Webアプリに大きなタイトルが表示されます。

### 2. 自動再読み込み
コードを保存すると、Streamlitは自動的にアプリを再実行します。
開発がとても効率的です。

### 3. Pythonの全機能が使える
- データ分析（pandas、numpy）
- 機械学習（scikit-learn、TensorFlow）
- 可視化（matplotlib、plotly）
- その他、PyPIの全てのライブラリ

---

## 🎨 テキスト表示の基本

以下は、Streamlitでよく使うテキスト表示の方法です：
""")

# 実践例: テキスト表示
st.markdown("### 実践例: 異なるテキスト表示方法")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**コード例:**")
    st.code("""
import streamlit as st

# タイトル（最も大きい）
st.title("タイトル")

# サブタイトル
st.subheader("サブタイトル")

# 通常のテキスト
st.write("通常のテキストです")

# キャプション（小さいテキスト）
st.caption("キャプション（説明など）")
    """, language="python")

with col2:
    st.markdown("**実行結果:**")
    st.write("このような形で表示されます ↓")
    st.divider()
    st.title("タイトル")
    st.subheader("サブタイトル")
    st.write("通常のテキストです")
    st.caption("キャプション（説明など）")

st.divider()

# メッセージ表示
st.markdown("""
## 📢 メッセージ表示

ユーザーに対して、情報、警告、エラーなどを表示できます。
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**コード例:**")
    st.code("""
# 情報メッセージ
st.info("情報を表示します")

# 成功メッセージ
st.success("成功しました")

# 警告メッセージ
st.warning("注意してください")

# エラーメッセージ
st.error("エラーが発生しました")
    """, language="python")

with col2:
    st.markdown("**実行結果:**")
    st.info("ℹ️ 情報を表示します")
    st.success("✅ 成功しました")
    st.warning("⚠️ 注意してください")
    st.error("❌ エラーが発生しました")

st.divider()

# Markdown
st.markdown("""
## 🎯 Markdownでリッチテキスト

`st.markdown()`を使うと、Markdownで複雑なテキストを作成できます。
Markdownは、HTMLよりもシンプルなマークアップ言語です。

### 基本的なMarkdown記法
- **太字** → `**太字**`
- *イタリック* → `*イタリック*`
- `コード` → `` `コード` ``
- [リンク](https://streamlit.io) → `[リンク](URL)`

### 色付きテキスト（Streamlit独自）
- :red[赤いテキスト] → `:red[赤いテキスト]`
- :green[緑のテキスト] → `:green[緑のテキスト]`
- :blue[青いテキスト] → `:blue[青いテキスト]`

試してみましょう：
""")

# 実践例: Markdown
st.markdown("""
:red[**これは重要です！**] このフレーズは赤で表示されます。

:green[✓ 成功] と :blue[ℹ️ 情報] を組み合わせることもできます。
""")

st.divider()

# 次のステップ
st.markdown("""
## 📚 次のステップ

**次のレッスン「02 入力UI」では：**
- ユーザーからの入力を受け取る方法を学びます
- テキスト入力、ボタン、スライダー、セレクトボックスなど
  様々なウィジェットを使います

**このレッスンのポイント:**
1. `st.title()` = ページのタイトル
2. `st.write()` = 基本的なテキスト表示
3. `st.markdown()` = リッチなテキスト表示
4. `st.info()`, `st.success()`, `st.warning()`, `st.error()` = メッセージ表示

---

**💻 今すぐやってみよう！**

このアプリの右上の「編集」ボタン（📝）をクリックして、
コードを編集してみてください。ファイルを保存すると、
すぐにアプリが更新されます！
""")

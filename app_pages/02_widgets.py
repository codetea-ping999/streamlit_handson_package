import streamlit as st

st.title("入力ウィジェットを使ってみよう")

st.markdown("""
## 📌 このレッスンについて

前のレッスンでは、テキストを**表示**する方法を学びました。
このレッスンでは、ユーザーから**入力**を受け取る方法を学びます。

Streamlitには、様々な入力ウィジェット（UI部品）が用意されています。

### 学習目標
- ✅ テキスト入力を受け取る
- ✅ スライダーで数値を選択する
- ✅ セレクトボックスで選択肢から1つ選ぶ
- ✅ マルチセレクトで複数選択する
- ✅ チェックボックスで有効/無効を切り替える
- ✅ ボタンをクリックして処理を実行する

---

## 🎮 入力ウィジェット

### 1. テキスト入力 (`st.text_input`)

ユーザーにテキストを入力させます。
""")

st.code("""
name = st.text_input("名前を入力してください")
st.write(f"あなたの名前: {name}")
""", language="python")

st.info("💡 入力内容は、変数に自動的に格納されます。Streamlitは再実行時に最新の値を保持します。")

st.divider()

st.markdown("""
### 2. スライダー (`st.slider`)

スライダーをドラッグして、範囲内の数値を選択します。
最小値、最大値、デフォルト値を指定できます。
""")

st.code("""
age = st.slider(
    "年齢を選択してください",
    min_value=18,
    max_value=70,
    value=30  # デフォルト値
)
""", language="python")

st.divider()

st.markdown("""
### 3. セレクトボックス (`st.selectbox`)

複数の選択肢から1つだけ選ぶことができます。
""")

st.code("""
department = st.selectbox(
    "部署を選択してください",
    ["営業", "開発", "総務", "製造", "品質保証"]
)
""", language="python")

st.divider()

st.markdown("""
### 4. マルチセレクト (`st.multiselect`)

複数の選択肢から、複数選ぶことができます。
""")

st.code("""
interests = st.multiselect(
    "興味のあるテーマ（複数選択可）",
    ["データ分析", "業務自動化", "生成AI", "Webアプリ", "クラウド"]
)
""", language="python")

st.divider()

st.markdown("""
### 5. チェックボックス (`st.checkbox`)

True/False（チェック/アンチェック）を切り替えます。
""")

st.code("""
show_detail = st.checkbox("詳細情報を表示する")
if show_detail:
    st.write("詳細が表示されます")
else:
    st.write("詳細は非表示です")
""", language="python")

st.divider()

st.markdown("""
### 6. ボタン (`st.button`)

ボタンをクリックされたときだけ、特定の処理を実行します。
""")

st.code("""
if st.button("実行"):
    st.success("ボタンがクリックされました！")
""", language="python")

st.divider()

st.markdown("""
## 🎯 実践: 社員情報フォーム

以下のフォームに、実際に入力してみてください。
すべての入力が「実行」ボタンの下に表示されます。
""")

st.markdown("### 📋 入力フォーム")

name = st.text_input("名前を入力してください")
age = st.slider("年齢", min_value=18, max_value=70, value=30)
department = st.selectbox(
    "部署を選択してください",
    ["営業", "開発", "総務", "製造", "品質保証"],
)
interests = st.multiselect(
    "興味のあるテーマ",
    ["データ分析", "業務自動化", "生成AI", "Webアプリ", "クラウド"],
)
show_detail = st.checkbox("入力内容の詳細を表示する")

st.markdown("### 🔘 実行")

if st.button("実行"):
    if not name.strip():
        st.warning("⚠️ 名前を入力してください。")
    else:
        st.success(f"✅ {name}さん、ようこそ！")

        # 入力内容を見やすく表示
        result_data = {
            "名前": name,
            "年齢": f"{age}歳",
            "部署": department,
        }

        st.markdown("### 📊 入力内容")
        st.write(result_data)

        if show_detail:
            st.markdown("### 💬 詳細情報")
            st.write("興味のあるテーマ:", interests or "未選択")

            # 年代別メッセージ
            if age < 25:
                st.info("🌟 若い世代ですね。新しい技術の習得が得意な時期です！")
            elif age < 40:
                st.info("💼 経験と成長のバランスが取れた時期ですね。")
            else:
                st.info("🎓 豊富な経験をお持ちですね。ぜひ後進の指導をお願いします。")

st.divider()

st.markdown("""
## 💭 入力値の保持について

Streamlitでは、ウィジェットの入力値は**セッション内で保持**されます。
つまり、ページをリロードしても入力値は消えません。

これは次のレッスン「06 セッション状態」で詳しく学びます。

---

## 📚 よく使うウィジェット一覧

| ウィジェット | 使用方法 | 戻り値 |
|-----------|--------|-------|
| `st.text_input()` | テキスト入力 | 文字列 |
| `st.number_input()` | 数値入力 | 数値 |
| `st.slider()` | スライダー | 数値 |
| `st.selectbox()` | 1つ選択 | 文字列 |
| `st.multiselect()` | 複数選択 | リスト |
| `st.checkbox()` | チェック | ブール値 |
| `st.radio()` | ラジオボタン | 文字列 |
| `st.button()` | ボタン | ブール値 |

---

## 🎓 実装のコツ

### ✅ 良い例：入力値の検証
```python
name = st.text_input("名前")
if st.button("送信"):
    if not name.strip():
        st.error("名前を入力してください")
    else:
        # 処理を実行
        st.success("登録しました")
```

### ❌ 悪い例：検証なし
```python
name = st.text_input("名前")
# ユーザーが空白で送信した場合、エラーが発生する可能性がある
process_name(name)
```

---

## 📚 次のステップ

**次のレッスン「03 CSV読込」では：**
- ファイルをアップロードする方法
- CSVファイルをDataFrameとして読み込む
- データを表形式で表示する

**このレッスンのポイント:**
1. ウィジェットの入力値は**自動的に変数に格納**される
2. ボタンクリック時に処理を実行する場合は、`if st.button():`で囲む
3. 常に**入力値を検証**してからユーザーに返す

---

**💻 今すぐやってみよう！**

1. 上のフォームに様々な値を入力してみてください
2. ボタンをクリックすると、入力内容が表示されます
3. 詳細情報のチェックボックスをONにすると、さらに多くの情報が表示されます
""")

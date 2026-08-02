from datetime import date

import streamlit as st

st.title("業務日報入力アプリ")

st.markdown("""
## 📌 このレッスンについて

これまでのレッスンでは、ウィジェットを操作するたびに
Streamlitがスクリプト全体を再実行していました。

このレッスンでは、複数の入力をまとめて処理する
**フォーム**を使用します。

### 学習目標
- ✅ `st.form()` でフォームを作成する
- ✅ 複数入力を一括で処理する
- ✅ 送信前の入力検証（バリデーション）
- ✅ 送信後の結果表示

---

## 🎯 フォームの必要性

### 問題：フォームなしの場合

```python
# ウィジェットを操作するたびに再実行される
name = st.text_input("氏名")
email = st.text_input("メール")
submit = st.button("送信")

# 問題：nameやemailを変更するたびに再実行され、
# スクリプト全体が何度も実行されて非効率
```

### 解決：フォームを使う場合

```python
with st.form("my_form"):
    name = st.text_input("氏名")
    email = st.text_input("メール")
    submitted = st.form_submit_button("送信")

if submitted:
    # 送信ボタンをクリックした時のみこのブロックが実行される
    process_form(name, email)
```

---

## 📋 フォームの実装

### ステップ1: フォームを作成
""")

st.code("""
with st.form("form_id"):
    # フォーム内に入力ウィジェットを配置
    name = st.text_input("名前")
    age = st.slider("年齢", 18, 70)

    # 送信ボタン（st.form_submit_button）
    submitted = st.form_submit_button("送信")
""", language="python")

st.markdown("""
### ステップ2: 送信時に処理

```python
if submitted:
    # バリデーション（入力チェック）
    if not name.strip():
        st.error("名前を入力してください")
    else:
        # 処理を実行
        st.success("登録しました")
```

**フォームのメリット：**
- 複数入力を一括で処理できる
- 送信までウィジェット変更時の再実行が抑制される
- UX（ユーザー体験）が向上する

---

## 🎯 実践: 業務日報フォーム

実際に日報を入力してみてください。送信ボタンをクリックするまで、
他の入力は記憶されます。
""")

st.divider()

st.markdown("### 📝 入力フォーム")

with st.form("daily_report", clear_on_submit=False):
    col1, col2 = st.columns(2)

    with col1:
        report_date = st.date_input("📅 日付", value=date.today())
        name = st.text_input("👤 氏名")

    with col2:
        department = st.selectbox(
            "🏢 部署",
            ["営業", "開発", "総務", "製造", "品質保証"],
        )

    st.markdown("### 📝 詳細情報")
    work = st.text_area("📋 本日の作業内容")
    issue = st.text_area("⚠️ 課題・困りごと")

    st.markdown("### 🔘 送信")
    submitted = st.form_submit_button("✅ 登録する")

if submitted:
    # バリデーション（入力確認）
    if not name.strip():
        st.error("❌ 氏名は必須です。入力してください。")
    elif not work.strip():
        st.error("❌ 作業内容は必須です。入力してください。")
    else:
        st.success("✅ 日報を受け付けました。")

        st.markdown("### 📊 入力内容確認")

        # 入力内容を見やすく表示
        summary_data = {
            "日付": str(report_date),
            "氏名": name,
            "部署": department,
            "作業内容": work,
            "課題": issue or "なし",
        }

        st.json(summary_data)

        st.markdown("""
        ---

        #### 💾 実際の運用では...

        このデータは以下のように処理されます：
        - 📊 データベースに保存
        - 📧 上司へメール送信
        - 📈 分析に利用
        """)

st.divider()

st.markdown("""
## 💡 フォーム実装のコツ

### ✅ 複数の入力をグループ化

```python
with st.form("user_form"):
    # 個人情報グループ
    st.markdown("### 個人情報")
    name = st.text_input("名前")
    age = st.slider("年齢", 18, 70)

    # 連絡先グループ
    st.markdown("### 連絡先")
    email = st.text_input("メール")
    phone = st.text_input("電話番号")

    submitted = st.form_submit_button("送信")
```

### ✅ 列を使ってレイアウト工夫

```python
with st.form("form_id"):
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("名")
    with col2:
        last_name = st.text_input("姓")

    submitted = st.form_submit_button("送信")
```

### ✅ 必須項目を明記

```python
st.markdown("### 必須項目 ✱")
name = st.text_input("氏名 ✱")
email = st.text_input("メール ✱")

st.markdown("### 任意項目")
comment = st.text_area("コメント")
```

### ✅ バリデーション（入力チェック）

```python
if submitted:
    errors = []

    if not name.strip():
        errors.append("氏名は必須です")

    if not email.strip():
        errors.append("メールは必須です")
    elif "@" not in email:
        errors.append("有効なメールアドレスを入力してください")

    if errors:
        for error in errors:
            st.error(error)
    else:
        st.success("送信成功！")
```

---

## 📚 フォーム関連のパラメータ

### st.form() のパラメータ

| パラメータ | 説明 |
|-----------|------|
| `key` | フォームの一意な識別子（必須） |
| `clear_on_submit=True` | 送信後、フォームをクリアするか |

### st.form_submit_button() のパラメータ

| パラメータ | 説明 |
|-----------|------|
| `label` | ボタンのテキスト |
| `help` | ホバー時に表示されるヘルプテキスト |
| `type` | `"primary"` (デフォルト) または `"secondary"` |

---

## 🎓 実装パターン

### パターン1: 簡単なフォーム

```python
with st.form("simple_form"):
    name = st.text_input("名前")
    submitted = st.form_submit_button("送信")

if submitted:
    st.write(f"こんにちは、{name}さん")
```

### パターン2: バリデーション付き

```python
with st.form("validated_form"):
    name = st.text_input("名前")
    age = st.number_input("年齢", min_value=0, max_value=150)
    submitted = st.form_submit_button("送信")

if submitted:
    if age < 18:
        st.warning("18歳以上である必要があります")
    else:
        st.success(f"{name}さんを登録しました")
```

### パターン3: 複数段階のフォーム

```python
# ステップ1: 個人情報
with st.form("step1"):
    name = st.text_input("名前")
    step1_submitted = st.form_submit_button("次へ")

if step1_submitted:
    st.session_state.name = name
    # ステップ2に進む

# ステップ2: 詳細情報
if st.session_state.get("name"):
    with st.form("step2"):
        st.write(f"{st.session_state.name}さんの詳細情報")
        email = st.text_input("メール")
        step2_submitted = st.form_submit_button("送信")
```

---

## 📚 次のレッスン

**次は「06 セッション状態」で学ぶこと：**
- `st.session_state` を使った状態管理
- フォーム送信後のデータの保持
- 複数ページにまたがるデータ共有

**このレッスンのポイント:**
1. `st.form()` で複数入力をまとめる
2. `st.form_submit_button()` で送信する
3. **常に入力値をバリデーション**する
4. ユーザーフレンドリーなメッセージを表示

---

**💻 今すぐやってみよう！**

1. 上のフォームに日報データを入力してみてください
2. 必須項目を空のまま送信してみて、バリデーションを確認
3. 異なる部署を選択して、どう表示が変わるか試す
""")

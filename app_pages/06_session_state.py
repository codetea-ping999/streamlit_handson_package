import streamlit as st

st.title("Session Stateで値を保持する")

st.markdown("""
## 📌 このレッスンについて

Streamlitは、ウィジェット操作やボタンクリックのたびに
スクリプト全体を**再実行**します。

では、どのように値をページをまたいで保持するのでしょうか？
その答えが **Session State** です。

### 学習目標
- ✅ Streamlitの再実行の仕組みを理解する
- ✅ `st.session_state` でデータを保持する
- ✅ ページ間でデータを共有する
- ✅ 状態管理を適切に実装する

---

## 🔄 Streamlitの再実行の仕組み

### 実行フロー図

```
ユーザー操作（ボタンクリック、入力など）
           ↓
Streamlit がスクリプトを全て再実行
           ↓
ページが再描画される
```

### 問題: 通常の変数は保持されない

```python
count = 0

if st.button("カウント"):
    count += 1  # ❌ この値は保持されない！

st.write(count)  # 常に0が表示される
```

**なぜ？** スクリプトが再実行されるたびに、`count = 0` に
リセットされるからです。

### 解決: Session State を使う

```python
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("カウント"):
    st.session_state.count += 1  # ✅ この値が保持される！

st.write(st.session_state.count)
```

---

## 📝 Session State の基本

### 初期化（最初の一度だけ実行）

```python
if "key" not in st.session_state:
    st.session_state.key = initial_value
```

**ポイント:**
- `"key" not in st.session_state` で、初めてアクセスされたかチェック
- True の場合のみ初期化される
- 2回目以降はこのブロックをスキップ

### 値の読み取り

```python
# 値を読み取る
value = st.session_state.count
print(value)

# または
value = st.session_state["count"]
print(value)
```

### 値の更新

```python
# 値を更新する
st.session_state.count = 10

# または
st.session_state["count"] = 10

# 増加・減少
st.session_state.count += 1
st.session_state.count -= 1
```

---

## 🎯 実践: カウンターアプリ

以下のカウンターアプリで、Session State の動作を確認してください。
ボタンをクリックすると、カウントが保持されます。
""")

st.divider()

# Session State の初期化
if "count" not in st.session_state:
    st.session_state.count = 0
    st.session_state.history = []

st.markdown("### 🎮 カウンターコントロール")

# 3つのボタンを並べて表示
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ +1", use_container_width=True):
        st.session_state.count += 1
        st.session_state.history.append(f"+1 → {st.session_state.count}")

with col2:
    if st.button("➖ -1", use_container_width=True):
        st.session_state.count -= 1
        st.session_state.history.append(f"-1 → {st.session_state.count}")

with col3:
    if st.button("🔄 リセット", use_container_width=True):
        st.session_state.count = 0
        st.session_state.history.append("🔄 リセット")

st.divider()

st.markdown("### 📊 現在の状態")

# メトリクスで表示
col1, col2, col3 = st.columns(3)
col1.metric("📈 現在のカウント", st.session_state.count)
col2.metric("🔢 操作回数", len(st.session_state.history))

if st.session_state.count > 0:
    col3.metric("➕ 増加傾向", f"+{st.session_state.count}")
elif st.session_state.count < 0:
    col3.metric("➖ 減少傾向", str(st.session_state.count))
else:
    col3.metric("⚪ ニュートラル", "0")

st.divider()

# 操作履歴を表示
if st.session_state.history:
    st.markdown("### 📜 操作履歴")

    # 最新5件を表示
    recent_history = st.session_state.history[-5:]

    for i, operation in enumerate(recent_history, 1):
        st.text(f"{i}. {operation}")

    if len(st.session_state.history) > 5:
        st.caption(f"...他 {len(st.session_state.history) - 5} 件")

st.divider()

st.markdown("""
## 💡 Session State の実世界での活用例

### 例1: ショッピングカート

```python
if "cart" not in st.session_state:
    st.session_state.cart = []

# 商品を追加
if st.button("カートに追加"):
    st.session_state.cart.append(product)

# カート内容を表示
st.write("カート:", st.session_state.cart)
```

### 例2: ログイン状態

```python
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.button("ログイン"):
    st.session_state.logged_in = True

if st.session_state.logged_in:
    st.write("ログイン済み")
else:
    st.write("ログインしてください")
```

### 例3: ウィザード（複数ステップ）

```python
if "step" not in st.session_state:
    st.session_state.step = 1

if st.session_state.step == 1:
    st.write("ステップ1: 個人情報")
    if st.button("次へ"):
        st.session_state.step = 2

elif st.session_state.step == 2:
    st.write("ステップ2: 確認")
    if st.button("完了"):
        st.session_state.step = 3
```

---

## 📚 Session State のルール

### ✅ 推奨される使い方

```python
# 1. 初回チェック
if "key" not in st.session_state:
    st.session_state.key = default_value

# 2. 明示的に値を更新
st.session_state.key = new_value

# 3. 読み取り
value = st.session_state.key
```

### ❌ 避けるべき使い方

```python
# ❌ 毎回新しい値に初期化される
if st.button("Click"):
    my_var = 0
    my_var += 1
    st.write(my_var)  # 常に1が表示される
```

### ✅ 複数のキーを管理

```python
if "user_data" not in st.session_state:
    st.session_state.user_data = {
        "name": "",
        "age": 0,
        "email": ""
    }

# 個別にアクセス
st.session_state.user_data["name"] = "Taro"
```

---

## 🎓 Session State vs グローバル変数

| 項目 | Session State | グローバル変数 |
|-----|-------------|------------|
| **保持期間** | ユーザーセッション内 | スクリプト再実行時にリセット |
| **複数ユーザー** | ユーザーごとに独立 | ユーザー間で共有（危険） |
| **推奨用途** | 状態管理、ユーザー入力 | 使用非推奨 |

### なぜユーザーごとに独立？

Streamlit はユーザーごとに独立したセッションを管理します。
同じアプリでも、ユーザーAの入力がユーザーBに見えることはありません。

```
ユーザーA: st.session_state.count = 5
↕
アプリケーション（共有）
↕
ユーザーB: st.session_state.count = 0
（独立している）
```

---

## 📚 次のレッスン

**次は「07 キャッシュ」で学ぶこと：**
- 重い計算結果をキャッシュして高速化
- `@st.cache_data` でデータ読み込みを最適化
- `@st.cache_resource` で共有リソースを管理

**このレッスンのポイント:**
1. Streamlitはウィジェット操作で再実行される
2. `st.session_state` で値を保持する
3. **必ず初回チェック** を行う
4. ユーザーごとに独立したセッション

---

**💻 今すぐやってみよう！**

1. 上のカウンターでボタンをクリックして、値が保持される様子を確認
2. ボタンを複数回クリックして、操作履歴が記録されるのを確認
3. ページを離れて戻ってくると、カウントがリセットされることを確認
   （理由：新しいセッションが開始される）

---

## 🎯 応用課題

上のカウンターに以下の機能を追加してみてください：
- [ ] 入力フィールドで任意の数字を加算できる機能
- [ ] 偶数/奇数を表示する機能
- [ ] カウントの最小値・最大値を設定する機能
""")

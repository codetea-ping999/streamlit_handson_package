# Streamlit ハンズオン手順書
## Pythonのみでウェブアプリケーション入門

---

## 1. ハンズオンの目的

本ハンズオンでは、講義用スライドの内容に沿って、Pythonのみで動作する簡易Webアプリケーションを段階的に作成します。

最終的には、`app.py` で起動するマルチページアプリの中で、基礎から応用までのレッスンに加えて、次の3つの完成版プロジェクトを完成させます。

- **天気予報アプリ** - 外部APIとの連携、エラーハンドリング
- **在庫管理システム** - Session Stateを使ったDataFrameのCRUD操作
- **顧客分析ダッシュボード** - RFM分析・LTV計算などの高度な集計と可視化

### 想定時間

約100〜120分

### 対象者

- Pythonの変数、条件分岐、関数を学んだ方
- pandasの経験はなくても可
- Webアプリケーション開発が初めての方

---

## 2. 使用するファイル

```text
streamlit_handson_package/
├── HANDSON_GUIDE.md             # 本手順書
├── requirements.txt             # 使用ライブラリ
├── app.py                       # マルチページ・ナビゲーター（起動の入口）
├── app_pages/                   # app.py が束ねる各ページ
│   ├── home.py                  # ホーム
│   ├── 01_hello_streamlit.py
│   ├── 02_widgets.py
│   ├── 03_csv_upload.py
│   ├── 04_sales_dashboard.py
│   ├── 05_form.py
│   ├── 06_session_state.py
│   ├── 07_cache.py
│   ├── 08_weather_app.py        # 完成版プロジェクト：天気予報アプリ
│   ├── 09_inventory_system.py   # 完成版プロジェクト：在庫管理システム
│   └── 10_customer_analytics.py # 完成版プロジェクト：顧客分析ダッシュボード
├── data/
│   └── sample_sales.csv         # 演習用データ
├── sample_code/                 # 各ステップのサンプルコード（app_pages/01〜07と同内容を単体実行可能）
│   ├── 01_hello_streamlit.py
│   ├── 02_widgets.py
│   ├── 03_csv_upload.py
│   ├── 04_sales_dashboard.py
│   ├── 05_form.py
│   ├── 06_session_state.py
│   └── 07_cache.py
└── sample_code_answers/         # 演習の実装例（参考）
    ├── 01_hello_streamlit_answer.py
    ├── 02_widgets_answer.py
    ├── 03_csv_upload_answer.py
    ├── 04_sales_dashboard_answer.py
    ├── 05_form_answer.py
    ├── 06_session_state_answer.py
    └── 07_cache_answer.py
```

---

## 3. 環境構築

### 3.1 前提ソフトウェア

- Python 3.10以上
- Visual Studio Code
- Webブラウザ
- ターミナル、PowerShell、コマンドプロンプトのいずれか

Pythonの確認コマンド（以下のいずれかで3.10以上が表示されればOK）：

```bash
python --version
```

または

```bash
python3 --version
```

**Windows**: `python` が見つからない場合は `python3` を使用してください。Pythonをインストールした際、環境変数PATHに追加されていない可能性があります。

### 3.2 仮想環境の作成

教材フォルダをVS Codeで開き、ターミナルで実行します。

```bash
python -m venv .venv
```

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

実行ポリシーのエラーが出た場合は、現在のPowerShellセッションだけ許可します。

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

#### Windows コマンドプロンプト

```cmd
.venv\Scripts\activate.bat
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

仮想環境が有効になると、ターミナルの先頭に `(.venv)` が表示されます。

### 3.3 ライブラリのインストール

仮想環境が有効化されている状態で実行してください。

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**注意**：`pip install -r requirements.txt` 実行時に以下のメッセージが表示されることがあります。  
`WARNING: Running pip as the 'root' user...` → 仮想環境内では無視して問題ありません。

確認：

```bash
streamlit --version
```

Streamlitのバージョン（例：`Streamlit, version 1.42.0`）が表示されればインストール成功です。

### 3.4 Streamlitの動作確認

```bash
streamlit hello
```

ブラウザにサンプル画面が表示されたら成功です。停止するときはターミナルで `Ctrl + C` を押します。

**ブラウザが自動で開かない場合**：
`streamlit run`を実行したターミナル出力に表示されるURL（デフォルト：`http://localhost:8501`）を手動でブラウザに入力してください。

**毎回ブラウザが開くのを避けたい場合**：

```bash
streamlit run app.py --logger.level=error
```

または `streamlit config` で設定ファイルを編集します。

---

## 4. Step 1：Hello Streamlit

講義スライド対応：環境構築、Hello Streamlit、画面表示の基本

### 4.1 実行

```bash
streamlit run sample_code/01_hello_streamlit.py
```

### 4.2 確認すること

- タイトルと文章がブラウザに表示される
- Pythonコードを変更して保存すると画面へ反映される
- `st.title()`、`st.write()`、`st.info()` の違い

### 4.3 演習

次の内容を追加してください。

```python
st.success("環境構築が完了しました。")
st.code("streamlit run app.py")
```

### 4.4 ポイント

StreamlitはPythonファイルを上から下へ実行し、`st.xxx()` の呼び出しを画面要素として描画します。

---

## 5. Step 2：入力ウィジェット

講義スライド対応：入力UI、レイアウト設計

### 5.1 実行

```bash
streamlit run sample_code/02_widgets.py
```

### 5.2 操作

1. 名前を入力する
2. 年齢をスライダーで選ぶ
3. 部署を選ぶ
4. 興味のあるテーマを複数選ぶ
5. 「実行」ボタンを押す

### 5.3 学習ポイント

| UI | Streamlit関数 | Pythonで受け取る型 |
|---|---|---|
| テキスト入力 | `st.text_input()` | `str` |
| スライダー | `st.slider()` | `int` |
| 単一選択 | `st.selectbox()` | `str` |
| 複数選択 | `st.multiselect()` | `list` |
| チェック | `st.checkbox()` | `bool` |
| ボタン | `st.button()` | `bool` |

### 5.4 演習

次の入力項目を追加してください。

- 経験年数を `st.number_input()` で入力
- 受講目的を `st.text_area()` で入力
- 入力内容を `st.json()` で表示

---

## 6. Step 3：CSVアップロード

講義スライド対応：CSVアップロード、pandas連携

### 6.1 実行

```bash
streamlit run sample_code/03_csv_upload.py
```

### 6.2 操作

1. `data/sample_sales.csv` をアップロードする
2. 表示された行数を確認する
3. 列名とデータを確認する

### 6.3 コードの重要部分

```python
uploaded_file = st.file_uploader("CSVファイル", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
```

`st.file_uploader()`が返すオブジェクトは、`pandas.read_csv()`に直接渡せます。

### 6.3.5 pandas基本データ型

CSVを読み込むと、`pd.DataFrame`（表形式のデータ構造）が返されます。よく使う操作を紹介します。

| 操作 | コード | 戻り値の型 |
| --- | --- | --- |
| 行数・列数を取得 | `df.shape` | `tuple (行数, 列数)` |
| 先頭N行を取得 | `df.head(5)` | `DataFrame` |
| 列名を取得 | `df.columns` | `Index` |
| 特定列を抽出 | `df["列名"]` | `Series`（1次元配列） |
| 合計を計算 | `df["売上"].sum()` | `int` または `float` |
| 部署ごとに集計 | `df.groupby("部署")["売上"].sum()` | `Series`（集計結果） |

### 6.4 演習

次の情報を画面に表示してください。

```python
st.write("行数:", len(df))
st.write("列名:", list(df.columns))
st.write("先頭5件")
st.dataframe(df.head())
```

---

## 7. Step 4：集計・指標・グラフ

講義スライド対応：集計と指標表示、グラフ表示、Sidebar、Columns

### 7.1 実行

```bash
streamlit run sample_code/04_sales_dashboard.py
```

### 7.2 操作

- サイドバーで表示する部署を変更する
- 合計売上、合計件数、平均売上が変化することを確認する
- 棒グラフと折れ線グラフの違いを確認する

### 7.3 pandasによる集計

```python
summary = df.groupby("部署")["売上"].sum()
```

処理の意味：

1. `部署` ごとに行をグループ化
2. `売上` 列を選択
3. 各グループの合計を計算

### 7.4 指標の表示

```python
col1, col2 = st.columns(2)
col1.metric("合計売上", f"{total_sales:,}円")
col2.metric("合計件数", f"{total_count:,}件")
```

### 7.5 演習

商品カテゴリ別の売上グラフを追加してください。

```python
category_summary = df.groupby("商品カテゴリ")["売上"].sum()
st.bar_chart(category_summary)
```

---

## 8. Step 5：Form

講義スライド対応：Form、入力をまとめて送信

### 8.1 実行

```bash
streamlit run sample_code/05_form.py
```

### 8.2 Formを使う理由

Streamlitはウィジェットを操作するたびにスクリプトを再実行します。`st.form()` を使用すると、複数の入力を「登録」ボタン押下時にまとめて処理できます。

```python
with st.form("daily_report"):
    name = st.text_input("氏名")
    submitted = st.form_submit_button("登録")
```

### 8.3 演習

次の項目を追加してください。

- 作業時間：`st.number_input()`
- 完了状態：`st.radio()`
- 優先度：`st.selectbox()`

---

## 9. Step 6：Session State

講義スライド対応：Streamlitの実行モデル、Session State

### 9.1 実行

```bash
streamlit run sample_code/06_session_state.py
```

### 9.2 実行モデル

Streamlitでは、ボタンや入力欄を操作するたびにPythonスクリプトが上から再実行されます。通常の変数は再作成されるため、値を保持したい場合は `st.session_state` を使用します。

```python
if "count" not in st.session_state:
    st.session_state.count = 0
```

### 9.3 演習

カウント履歴を保持してください。

ヒント：

```python
if "history" not in st.session_state:
    st.session_state.history = []
```

ボタン操作時に次を実行します。

```python
st.session_state.history.append(st.session_state.count)
```

---

## 10. Step 7：Cache

講義スライド対応：Cache、重い処理の高速化

### 10.1 実行

```bash
streamlit run sample_code/07_cache.py
```

### 10.2 確認

1. 最初の読み込みでは約2秒かかる
2. 画面操作や再実行後は短時間で表示される
3. 「キャッシュを削除」を押すと、再び読み込みに時間がかかる

### 10.3 CacheとSession Stateの違い

| 機能 | 目的 | 主な用途 |
|---|---|---|
| `st.session_state` | ユーザー操作をまたいで値を保持 | カウンター、入力途中、チャット履歴 |
| `st.cache_data` | 同じ計算結果を再利用 | CSV読込、API結果、集計処理 |

---

## 11. 最終演習：完成版プロジェクト

講義スライド対応：ミニ演習「売上分析アプリ」

### 11.1 完成版を実行

```bash
streamlit run app.py
```

サイドバーの「完成版プロジェクト」セクションから、以下の3つのアプリを開けます。

### 11.2 08 天気予報アプリ（`app_pages/08_weather_app.py`）

- 外部API（`requests`）から天気データを取得する
- APIレスポンスを整形して表示する
- 通信エラー・不正な入力に対するエラーハンドリングを行う

### 11.3 09 在庫管理システム（`app_pages/09_inventory_system.py`）

- `st.session_state` で在庫データを保持する
- 商品の追加・編集・削除（CRUD）を行う
- 入力値を検証する

### 11.4 10 顧客分析ダッシュボード（`app_pages/10_customer_analytics.py`）

- `numpy`を使ったRFM分析・LTV計算などの集計を行う
- 複数条件でのフィルタリングを行う
- 複数のグラフを組み合わせてダッシュボード化する

### 11.5 コードリーディングの順番（共通）

1. `st.set_page_config()` / `import` 文：画面設定と依存ライブラリ
2. `st.session_state` の初期化：状態管理が必要な箇所
3. `st.sidebar` / `st.tabs()` / `st.columns()`：入力条件とレイアウト
4. データの絞り込み・集計処理
5. `st.metric()` / `st.bar_chart()` / `st.line_chart()`：指標・可視化
6. `st.form()` / `st.button()`：ユーザー操作の受け口

### 11.6 発展課題

#### 課題A：担当者フィルター

04売上分析ダッシュボードのサイドバーに担当者の複数選択を追加します。

#### 課題B：最高売上の表示

04売上分析ダッシュボードで、最大売上の担当者と金額を `st.metric()` または `st.success()` で表示します。

#### 課題C：CSVの入力エラー表示

03CSV読込・04売上分析ダッシュボードで、売上や件数に数値以外が含まれた場合に削除件数を警告表示します。

#### 課題D：新しい完成版プロジェクトを作る

08〜10のような「完成版プロジェクト」を自分でもう1つ作り、`app_pages/11_your_project.py` として追加し、`app.py` の `pages` 辞書に登録してみましょう。

---

## 12. よくあるエラーと対処

### `streamlit` コマンドが見つからない

仮想環境が有効か確認します。

```bash
pip show streamlit
python -m streamlit run app.py
```

### `ModuleNotFoundError: No module named 'pandas'`

```bash
pip install -r requirements.txt
```

### CSVの文字化け

ExcelからCSVを保存するときは「CSV UTF-8（コンマ区切り）」を選びます。

Python側でShift-JISを読む場合：

```python
df = pd.read_csv(uploaded_file, encoding="cp932")
```

### ポート8501が使用中

```bash
streamlit run app.py --server.port 8502
```

### 画面が更新されない

- Pythonファイルを保存したか確認
- ブラウザの「Rerun」を押す
- ターミナルにエラーが出ていないか確認

### 相対パスでファイルが見つからない

Streamlitは実行位置から相対パスを解決するため、実行ディレクトリが重要です。  
`Path(__file__)` を基準にすることで、実行場所に依存しないパスを作成できます。

**間違った例**（実行ディレクトリに依存）：

```python
df = pd.read_csv("data/sample_sales.csv")  # 実行位置によって失敗する可能性
```

**正しい例**（ファイル位置を基準）：

```python
from pathlib import Path
sample_path = Path(__file__).resolve().parent / "data" / "sample_sales.csv"
df = pd.read_csv(sample_path)
```

**補足**：各サンプルコードは以下のように実行してください。

- `streamlit run sample_code/04_sales_dashboard.py`（プロジェクトルートから実行）
- パスの `parents[1]` は `sample_code/` フォルダーの親（プロジェクトルート）を指しています

---

## 13. 研修終了時の確認項目

- [ ] 仮想環境を作成できた
- [ ] Streamlitアプリを起動できた
- [ ] `st.title()` や `st.write()` で画面表示できた
- [ ] 入力ウィジェットの値をPython変数として取得できた
- [ ] CSVをpandasで読み込めた
- [ ] `groupby()` でデータを集計できた
- [ ] `st.metric()` で指標を表示できた
- [ ] 棒グラフと折れ線グラフを表示できた
- [ ] Form、Session State、Cacheの役割を説明できる
- [ ] 完成版プロジェクト（天気予報アプリ・在庫管理システム・顧客分析ダッシュボード）のいずれかを起動・操作できた

---

## 14. 参考資料・ドキュメント（新規）

### 公式ドキュメント

- [Streamlit公式ドキュメント](https://docs.streamlit.io/)
- [Streamlit API リファレンス](https://docs.streamlit.io/develop/api-reference)
- [pandas 公式ドキュメント](https://pandas.pydata.org/docs/)

### よく使う機能の参照

| 機能 | 公式ドキュメント |
| --- | --- |
| `st.text_input()` / `st.slider()` | [Input widgets](https://docs.streamlit.io/develop/api-reference/widgets/st.text_input) |
| `st.file_uploader()` | [File uploader](https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader) |
| `st.bar_chart()` / `st.line_chart()` | [Chart elements](https://docs.streamlit.io/develop/api-reference/charts) |
| `st.session_state` | [Session State](https://docs.streamlit.io/develop/api-reference/session-state) |
| `@st.cache_data` | [Caching](https://docs.streamlit.io/develop/concepts/performance/caching) |
| `pd.read_csv()` / `df.groupby()` | [pandas API reference](https://pandas.pydata.org/docs/reference/index.html) |

---

## 15. 終了方法

Streamlitアプリを停止するときは、実行中のターミナルで次を押します。

```text
Ctrl + C
```

仮想環境を終了します。

```bash
deactivate
```

---

## 16. 演習の解答例（オプション）

### 16.1 自己確認ポイント

各Stepの演習に取り組んだ後、以下のポイントで自分の実装を確認してください。

**Step 1の演習：** `st.success()`と`st.code()`を追加したか？  
**Step 2の演習：** `st.number_input()`、`st.text_area()`、`st.json()`を追加したか？  
**Step 3の演習：** `len(df)`、`list(df.columns)`、`df.head()`を表示したか？  
**Step 4の演習：** 商品カテゴリ別の売上グラフを追加したか？  
**Step 5の演習：** 作業時間、完了状態、優先度の入力項目を追加したか？  
**Step 6の演習：** カウント履歴をリストで保持したか？  
**Step 7の演習：** キャッシュが正常に動作しているか時間を計測して確認したか？

### 16.2 解答例ファイル

各Stepの演習に対する実装例が `sample_code_answers/` フォルダーに用意されています。

```text
sample_code_answers/
├── 01_hello_streamlit_answer.py
├── 02_widgets_answer.py
├── 03_csv_upload_answer.py
├── 04_sales_dashboard_answer.py
├── 05_form_answer.py
├── 06_session_state_answer.py
└── 07_cache_answer.py
```

参考にしたい場合は次のコマンドで実行できます。

```bash
streamlit run sample_code_answers/01_hello_streamlit_answer.py
```

**注意**：解答例を確認する前に、まず自分で実装に取り組むことをオススメします。

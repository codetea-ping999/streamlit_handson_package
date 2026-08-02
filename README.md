# Streamlit ハンズオン教材

Pythonのみでウェブアプリケーションを開発するためのハンズオン教材です。  
**マルチページアプリ `app.py` の中で、基礎から応用までのレッスンと3つの完成版プロジェクトを体験できます。**

## 📚 このコースで学べること

- **Streamlit基礎**：画面表示とテキスト操作
- **入力UI**：スライダー、選択ボックス、複数選択ウィジェット
- **データ処理**：CSVアップロードとpandasによる集計
- **データ可視化**：棒グラフと折れ線グラフの表示
- **フォーム設計**：複数入力をまとめて処理
- **セッション管理**：Session Stateで値を保持
- **パフォーマンス最適化**：@st.cache_dataで処理を高速化
- **実装スキル**：天気予報アプリ・在庫管理システム・顧客分析ダッシュボードの構築

### 想定時間：100〜120分 | 対象：Python基礎を習得した方

---

## 📁 ファイル構成

```text
streamlit_handson_package/
├── HANDSON_GUIDE.md              # 詳細な学習手順書 ← まずはこちらをお読みください
├── README.md                      # このファイル
├── requirements.txt               # 必要なライブラリ
├── app.py                         # マルチページ・ナビゲーター（起動の入口）
├── app_pages/                     # app.py が束ねる各ページ
│   ├── home.py                    # ホーム（学習ガイド）
│   ├── 01_hello_streamlit.py      # 基礎講座：画面表示
│   ├── 02_widgets.py              # 基礎講座：入力UI
│   ├── 03_csv_upload.py           # 基礎講座：CSV読込
│   ├── 04_sales_dashboard.py      # 応用講座：売上分析
│   ├── 05_form.py                 # 応用講座：フォーム
│   ├── 06_session_state.py        # 高度な機能：セッション状態
│   ├── 07_cache.py                # 高度な機能：キャッシュ
│   ├── 08_weather_app.py          # 完成版プロジェクト：天気予報アプリ
│   ├── 09_inventory_system.py     # 完成版プロジェクト：在庫管理システム
│   └── 10_customer_analytics.py   # 完成版プロジェクト：顧客分析ダッシュボード
├── data/
│   └── sample_sales.csv           # 演習用データ（実際のビジネスデータ）
├── sample_code/                   # レッスン01〜07に対応するステップ別サンプルコード
│   ├── 01_hello_streamlit.py      # ステップ1：基本的な画面表示
│   ├── 02_widgets.py              # ステップ2：入力ウィジェット
│   ├── 03_csv_upload.py           # ステップ3：CSVアップロード
│   ├── 04_sales_dashboard.py      # ステップ4：集計とグラフ表示
│   ├── 05_form.py                 # ステップ5：フォーム操作
│   ├── 06_session_state.py        # ステップ6：値の保持
│   └── 07_cache.py                # ステップ7：キャッシング
└── sample_code_answers/           # 演習問題の実装例（参考用）
    ├── 01_hello_streamlit_answer.py
    ├── 02_widgets_answer.py
    ├── 03_csv_upload_answer.py
    ├── 04_sales_dashboard_answer.py
    ├── 05_form_answer.py
    ├── 06_session_state_answer.py
    └── 07_cache_answer.py
```

`sample_code/` は `app_pages/01〜07` と同じ内容を単体で実行できるようにしたファイルです。`streamlit run sample_code/01_hello_streamlit.py` のように1レッスンだけ動かして写経したいときに使います。

---

## 🚀 クイックスタート

### 1. 環境構築

```bash
# 仮想環境を作成
python -m venv .venv
```

### 2. 仮想環境を有効化

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows コマンドプロンプト**
```cmd
.venv\Scripts\activate.bat
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

### 3. ライブラリをインストール

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. アプリを起動

```bash
streamlit run app.py
```

ブラウザが自動で開き、`http://localhost:8501` にアクセスします。サイドバーからレッスンを選んで学習を進めてください。

---

## 📖 学習の進め方

```bash
streamlit run app.py
```

上記コマンドでアプリを起動すると、左側のサイドバーからすべてのレッスン・プロジェクトへ移動できます。各ページは `sample_code/` の同名ファイルを単体実行しても同じ内容を確認できます。

### 基礎講座（レッスン01〜03）

- **01 Hello Streamlit** - `st.title()` / `st.write()` など画面表示の基本
- **02 入力UI** - テキスト入力、スライダー、ドロップダウン、複数選択などのウィジェット
- **03 CSV読込** - ファイルアップロードとpandasによるデータ処理

### 応用講座（レッスン04〜05）

- **04 売上分析** - `groupby()`で集計し、KPI指標とグラフで可視化
- **05 フォーム** - 複数の入力項目を「送信」ボタンでまとめて処理

### 高度な機能（レッスン06〜07）

- **06 セッション状態** - Streamlitの再実行モデルとSession Stateによる値の保持
- **07 キャッシュ** - `@st.cache_data`で重い処理をキャッシュし、パフォーマンスを最適化

### 完成版プロジェクト（レッスン08〜10）

これまでのスキルを組み合わせた実践的なアプリです。

- **08 天気予報アプリ** - 外部API（`requests`）連携、レスポンス処理、エラーハンドリング
- **09 在庫管理システム** - Session Stateを使ったDataFrameのCRUD操作
- **10 顧客分析ダッシュボード** - `numpy`を使ったRFM分析・LTV計算などの高度な集計と可視化

---

## 💡 演習問題について

各ステップに演習問題が用意されています。  
まず**自分で実装に取り組んだ後**、`sample_code_answers/`フォルダーの実装例を参考にしてください。

例：ステップ1の解答例を実行する場合

```bash
streamlit run sample_code_answers/01_hello_streamlit_answer.py
```

---

## 📚 参考資料

- [Streamlit公式ドキュメント](https://docs.streamlit.io/)
- [Streamlit APIリファレンス](https://docs.streamlit.io/develop/api-reference)
- [pandas公式ドキュメント](https://pandas.pydata.org/docs/)
- [HANDSON_GUIDE.md](HANDSON_GUIDE.md) - 詳細な学習手順書

---

## ⚠️ トラブルシューティング

### `streamlit`コマンドが見つからない

```bash
# 仮想環境が有効か確認
pip show streamlit

# または
python -m streamlit run app.py
```

### `ModuleNotFoundError: No module named 'pandas'`

```bash
pip install -r requirements.txt
```

### ポート8501が使用中の場合

```bash
streamlit run app.py --server.port 8502
```

### CSVが開けない / 文字化けする

ExcelからCSVを保存するときは「CSV UTF-8（コンマ区切り）」形式を選択してください。

---

## 📋 よくある質問（FAQ）

**Q：Pythonをインストールしていません**  
A：[Python公式サイト](https://www.python.org/downloads/)からPython 3.10以上をインストールしてください。

**Q：pandas や Streamlit の使い方をもっと詳しく知りたい**  
A：[HANDSON_GUIDE.md](HANDSON_GUIDE.md)の「14. 参考資料・ドキュメント」セクションをご覧ください。

**Q：演習の解答例が見たい**  
A：`sample_code_answers/`フォルダーに全演習問題の実装例が用意されています。

---

## 📝 備考

- このコースは講義スライド「Pythonのみでウェブアプリケーション入門（Streamlit）」に対応しています
- 実装の詳細は [HANDSON_GUIDE.md](HANDSON_GUIDE.md) に記載されています
- 環境構築や実行時のエラーについては、ガイドの「12. よくあるエラーと対処」を参照してください
# streamlit_handson_package
# streamlit_handson_package
# streamlit_handson_package
# streamlit_handson_package
# streamlit_handson_package

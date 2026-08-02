# Streamlit ハンズオン教材

Pythonのみでウェブアプリケーションを開発するためのハンズオン教材です。  
**7つのステップで段階的に学び、最終的に実務的な売上分析アプリを完成させます。**

## 📚 このコースで学べること

- **Streamlit基礎**：画面表示とテキスト操作
- **入力UI**：スライダー、選択ボックス、複数選択ウィジェット
- **データ処理**：CSVアップロードとpandasによる集計
- **データ可視化**：棒グラフと折れ線グラフの表示
- **フォーム設計**：複数入力をまとめて処理
- **セッション管理**：Session Stateで値を保持
- **パフォーマンス最適化**：@st.cache_dataで処理を高速化
- **実装スキル**：実務的なダッシュボードアプリの構築

### 想定時間：100〜120分 | 対象：Python基礎を習得した方

---

## 📁 ファイル構成

```text
streamlit_handson_package/
├── HANDSON_GUIDE.md              # 詳細な学習手順書 ← まずはこちらをお読みください
├── README.md                      # このファイル
├── requirements.txt               # 必要なライブラリ
├── app.py                         # 完成版：売上分析アプリ
├── data/
│   └── sample_sales.csv           # 演習用データ（実際のビジネスデータ）
├── sample_code/                   # 7つのステップ別サンプルコード
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

### 4. 完成版アプリを実行

```bash
streamlit run app.py
```

ブラウザが自動で開き、`http://localhost:8501` にアクセスします。

---

## 📖 学習の進め方

### Step 1：Hello Streamlit（画面表示）

```bash
streamlit run sample_code/01_hello_streamlit.py
```

Streamlitで画面にテキストを表示する基本を学びます。

### Step 2：入力ウィジェット（ユーザー操作）

```bash
streamlit run sample_code/02_widgets.py
```

テキスト入力、スライダー、ドロップダウン、複数選択など、さまざまな入力UIを体験します。

### Step 3：CSVアップロード（ファイル操作）

```bash
streamlit run sample_code/03_csv_upload.py
```

ユーザーがアップロードしたCSVファイルを読み込み、pandasで操作します。

### Step 4：集計・指標・グラフ（データ可視化）

```bash
streamlit run sample_code/04_sales_dashboard.py
```

`groupby()`で集計し、KPI指標とグラフで可視化します。

### Step 5：フォーム（複数入力の管理）

```bash
streamlit run sample_code/05_form.py
```

複数の入力項目を「送信」ボタンでまとめて処理します。

### Step 6：Session State（値の保持）

```bash
streamlit run sample_code/06_session_state.py
```

Streamlitの再実行モデルを理解し、セッション内で値を保持します。

### Step 7：キャッシング（処理の高速化）

```bash
streamlit run sample_code/07_cache.py
```

`@st.cache_data`で重い処理をキャッシュし、パフォーマンスを最適化します。

### 最終演習：売上分析アプリ

```bash
streamlit run app.py
```

すべてのスキルを組み合わせた実務的なダッシュボードアプリです。

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

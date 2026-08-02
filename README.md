# Streamlit ハンズオン教材

講義用スライド「Pythonのみでウェブアプリケーション入門（Streamlit）」に対応した実習教材です。

## ファイル構成

```text
streamlit_handson_package/
├── HANDSON_GUIDE.md
├── README.md
├── requirements.txt
├── app.py
├── data/
│   └── sample_sales.csv
└── sample_code/
    ├── 01_hello_streamlit.py
    ├── 02_widgets.py
    ├── 03_csv_upload.py
    ├── 04_sales_dashboard.py
    ├── 05_form.py
    ├── 06_session_state.py
    └── 07_cache.py
```

## 最短の実行手順

```bash
python -m venv .venv
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

### macOS / Linux

```bash
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

ブラウザで `http://localhost:8501` を開きます。

詳細は [HANDSON_GUIDE.md](HANDSON_GUIDE.md) を参照してください。
# streamlit_handson_package
# streamlit_handson_package
# streamlit_handson_package

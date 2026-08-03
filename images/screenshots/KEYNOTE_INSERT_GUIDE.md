# Keynoteスライドへの画像挿入ガイド

`streamlit_webapp_intro_training.key` はバイナリ形式（Snappy圧縮のprotobuf）のため、
スクリプトでスライド内のテキストを自動抽出したり、スライド番号を自動判定することができません。
そのため、このフォルダの画像はKeynoteへ自動挿入せず、対応関係の一覧のみを用意しています。
以下を参考に、該当するスライドを目視で探して手動で挿入してください。

## 挿入手順（共通）

1. Keynoteで `streamlit_webapp_intro_training.key` を開く
2. 下表の「対応する講義トピック」に該当するスライドを探す
3. 「挿入」→「画像を選択」で、対応する画像ファイルをスライドに配置する
4. 必要に応じてキャプション（例：「実際の画面」）を添える

## 画像とスライドトピックの対応表

| 画像ファイル | 対応する講義トピック（HANDSON_GUIDE.mdの「講義スライド対応」より） |
| --- | --- |
| `00_app_top.png` | イントロ／アプリ全体像の紹介（マルチページアプリ `app.py` の起動画面） |
| `01_hello_streamlit.png` | 環境構築、Hello Streamlit、画面表示の基本 |
| `02_widgets.png` | 入力UI、レイアウト設計 |
| `03_csv_upload.png` | CSVアップロード、pandas連携 |
| `04_sales_dashboard.png` | 集計と指標表示、グラフ表示、Sidebar、Columns |
| `05_form.png` | Form、入力をまとめて送信 |
| `06_session_state.png` | Streamlitの実行モデル、Session State |
| `07_cache.png` | Cache、重い処理の高速化 |
| `08_weather_app.png` | 最終演習「完成版プロジェクト」：天気予報アプリ |
| `09_inventory_system.png` | 最終演習「完成版プロジェクト」：在庫管理システム |
| `10_customer_analytics.png` | 最終演習「完成版プロジェクト」：顧客分析ダッシュボード |

## 補足

- 画像はすべて `streamlit run app.py` を実際に起動し、Playwright（Chromiumヘッドレスブラウザ）で
  各レッスンの操作結果（ウィジェット入力後・CSVアップロード後・フォーム送信後など）を撮影したものです。
- 解像度は 1440×900 で統一しています。スライドに配置する際は縦横比を保ったまま縮小してください。

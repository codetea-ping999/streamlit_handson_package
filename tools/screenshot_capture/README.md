# スクリーンショット撮影ツール

`images/screenshots/` にあるアプリ画面のスクリーンショットを再撮影するためのPlaywrightスクリプトです。
レッスンの内容やUI文言を変更したときに、画像を撮り直すために使います。

## セットアップ（初回のみ）

このツールはドキュメント作成用の一時的な開発ツールのため、アプリ本体の `requirements.txt` には含めていません。
使う前に、プロジェクトの `.venv` を有効化した状態で以下を実行してください。

```bash
source .venv/bin/activate
pip install playwright
playwright install chromium
```

## 実行方法

```bash
source .venv/bin/activate
python tools/screenshot_capture/capture_screenshots.py
```

- `app.py` を裏で自動起動し、Chromiumヘッドレスブラウザで各レッスン・完成版プロジェクトの画面を巡回して撮影します
- 撮影が終わるとStreamlitプロセスは自動的に終了します
- 出力先は `images/screenshots/` 配下（ファイル名は既存の画像と同じ）

## 使い終わったら

継続的に使わない場合は、以下でアンインストールして問題ありません（スクリプト自体はこのディレクトリに残ります）。

```bash
pip uninstall -y playwright pyee greenlet
rm -rf ~/Library/Caches/ms-playwright
```

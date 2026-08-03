"""
アプリの実際の画面をPlaywrightで自動撮影し、images/screenshots/ に保存するスクリプト。

前提（このリポジトリのrequirements.txtには含めていません）:
    pip install playwright
    playwright install chromium

実行方法（プロジェクトルートの.venvを有効化した状態で）:
    python tools/screenshot_capture/capture_screenshots.py
"""

import subprocess
import time
import urllib.request
from pathlib import Path

from playwright.sync_api import sync_playwright

REPO = Path(__file__).resolve().parents[2]
APP = REPO / "app.py"
CSV_PATH = REPO / "data" / "sample_sales.csv"
OUT_DIR = REPO / "images" / "screenshots"
PORT = 8611
BASE_URL = f"http://localhost:{PORT}"

OUT_DIR.mkdir(parents=True, exist_ok=True)


def wait_for_server(url, timeout=40):
    start = time.time()
    while time.time() - start < timeout:
        try:
            urllib.request.urlopen(url, timeout=2)
            return True
        except Exception:
            time.sleep(0.5)
    raise RuntimeError(f"Server at {url} did not start within {timeout}s")


def goto_page(page, link_name):
    page.get_by_role("link", name=link_name, exact=False).first.click()
    page.wait_for_timeout(1200)


def select_option(page, combobox_label, option_name):
    combo = page.get_by_role("combobox", name=combobox_label, exact=False)
    combo.click()
    combo.press("ArrowDown")
    page.wait_for_timeout(300)
    page.get_by_role("option", name=option_name, exact=True).click()
    page.wait_for_timeout(200)


def click_checkbox(page, label):
    page.get_by_role("checkbox", name=label, exact=False).locator(
        "xpath=ancestor::label[1]"
    ).click()


def main():
    proc = subprocess.Popen(
        [
            str(REPO / ".venv" / "bin" / "streamlit"),
            "run",
            str(APP),
            "--server.headless=true",
            f"--server.port={PORT}",
            "--server.address=localhost",
            "--browser.gatherUsageStats=false",
        ],
        cwd=str(REPO),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    try:
        wait_for_server(BASE_URL)
        time.sleep(2)

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            page.goto(BASE_URL, wait_until="networkidle")
            page.wait_for_timeout(1500)

            # 00: home
            page.screenshot(path=str(OUT_DIR / "00_app_top.png"))

            # 01: hello streamlit
            goto_page(page, "01 Hello Streamlit")
            page.screenshot(path=str(OUT_DIR / "01_hello_streamlit.png"))

            # 02: widgets - fill in inputs then click 実行
            goto_page(page, "02 入力UI")
            page.get_by_label("名前を入力してください").fill("山田 太郎")
            select_option(page, "部署を選択してください", "開発")
            combo = page.get_by_role("combobox", name="興味のあるテーマ", exact=False)
            combo.click()
            combo.press("ArrowDown")
            page.wait_for_timeout(300)
            page.get_by_role("option", name="データ分析", exact=True).click()
            page.wait_for_timeout(200)
            page.get_by_role("option", name="生成AI", exact=True).click()
            page.wait_for_timeout(200)
            page.keyboard.press("Escape")
            click_checkbox(page, "入力内容の詳細を表示する")
            page.get_by_role("button", name="実行").click()
            page.wait_for_timeout(800)
            page.screenshot(path=str(OUT_DIR / "02_widgets.png"), full_page=True)

            # 03: csv upload
            goto_page(page, "03 CSV読込")
            page.locator("input[type='file']").first.set_input_files(str(CSV_PATH))
            page.wait_for_timeout(1200)
            page.get_by_text("ファイルアップロード完了", exact=False).scroll_into_view_if_needed()
            page.wait_for_timeout(400)
            page.screenshot(path=str(OUT_DIR / "03_csv_upload.png"))

            # 04: sales dashboard (default view already shows metrics + charts)
            goto_page(page, "04 売上分析")
            page.wait_for_timeout(1000)
            page.get_by_text("主要指標（KPI）", exact=False).scroll_into_view_if_needed()
            page.wait_for_timeout(400)
            page.screenshot(path=str(OUT_DIR / "04_sales_dashboard.png"))

            # 05: form
            goto_page(page, "05 フォーム")
            page.get_by_label("氏名", exact=False).fill("鈴木 花子")
            page.get_by_label("本日の作業内容", exact=False).fill("顧客対応と資料作成を実施しました。")
            page.get_by_label("課題・困りごと", exact=False).fill("特になし")
            page.get_by_role("button", name="登録する", exact=False).click()
            page.wait_for_timeout(800)
            page.screenshot(path=str(OUT_DIR / "05_form.png"), full_page=True)

            # 06: session state - click +1 a few times
            goto_page(page, "06 セッション状態")
            plus_button = page.get_by_role("button", name="+1", exact=False)
            for _ in range(3):
                plus_button.click()
                page.wait_for_timeout(300)
            page.screenshot(path=str(OUT_DIR / "06_session_state.png"), full_page=True)

            # 07: cache - click load button and wait
            goto_page(page, "07 キャッシュ")
            page.get_by_role("button", name="データを読み込む", exact=False).click()
            page.wait_for_timeout(2500)
            page.screenshot(path=str(OUT_DIR / "07_cache.png"), full_page=True)

            # 08: weather app (default city already selected)
            goto_page(page, "08 天気予報アプリ")
            page.wait_for_timeout(1000)
            page.get_by_role("heading", name="の天気", exact=False).scroll_into_view_if_needed()
            page.wait_for_timeout(400)
            page.screenshot(path=str(OUT_DIR / "08_weather_app.png"))

            # 09: inventory system (default dashboard tab)
            goto_page(page, "09 在庫管理システム")
            page.wait_for_timeout(1000)
            page.get_by_text("在庫サマリー", exact=False).scroll_into_view_if_needed()
            page.wait_for_timeout(400)
            page.screenshot(path=str(OUT_DIR / "09_inventory_system.png"))

            # 10: customer analytics (default first tab)
            goto_page(page, "10 顧客分析ダッシュボード")
            page.wait_for_timeout(1000)
            page.get_by_text("主要KPI", exact=False).scroll_into_view_if_needed()
            page.wait_for_timeout(400)
            page.screenshot(path=str(OUT_DIR / "10_customer_analytics.png"))

            browser.close()

        print("DONE")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()


if __name__ == "__main__":
    main()

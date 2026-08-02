import streamlit as st
import requests
from datetime import datetime, timedelta
import pandas as pd

st.title("🌤️ 天気予報アプリ")

st.markdown("""
## 📌 このプロジェクトについて

このアプリは、OpenWeatherMap APIを使用して、
世界中の都市の現在の天気と予報を表示します。

### 学習できること
- ✅ 外部APIとの連携
- ✅ APIレスポンスの処理
- ✅ エラーハンドリング
- ✅ リアルタイムデータの表示
- ✅ 天気情報の可視化

### 技術スタック
- Streamlit - UI フレームワーク
- requests - HTTP通信
- pandas - データ処理
- OpenWeatherMap API - 天気データ

---

## 🎯 アプリの機能

1. **都市検索** - 世界中の都市から検索
2. **現在の天気表示** - 気温、湿度、風速など
3. **天気アイコン** - 天気に合わせた絵文字表示
4. **5日間の予報** - グラフで予報を可視化
5. **複数都市の比較** - 複数都市の天気を並べて表示

---

## 💡 実装のポイント

### APIキーの設定

実際に使用する場合は、以下の手順でAPIキーを取得してください：

1. [OpenWeatherMap](https://openweathermap.org/api) にアクセス
2. 無料プランで登録
3. APIキーをコピー
4. `.streamlit/secrets.toml` に保存

```toml
[openweathermap]
api_key = "your_api_key_here"
```

---
""")

st.divider()

# デモ用のモック関数（実際のAPIの代わり）
def get_mock_weather(city):
    """デモンストレーション用のモック天気データ"""
    mock_data = {
        "Tokyo": {
            "name": "Tokyo",
            "temp": 28.5,
            "feels_like": 30.2,
            "humidity": 65,
            "pressure": 1013,
            "wind_speed": 3.2,
            "description": "Clear sky",
            "icon": "☀️"
        },
        "London": {
            "name": "London",
            "temp": 18.3,
            "feels_like": 17.8,
            "humidity": 72,
            "pressure": 1015,
            "wind_speed": 4.5,
            "description": "Partly cloudy",
            "icon": "⛅"
        },
        "Sydney": {
            "name": "Sydney",
            "temp": 22.1,
            "feels_like": 21.5,
            "humidity": 58,
            "pressure": 1018,
            "wind_speed": 5.2,
            "description": "Sunny",
            "icon": "🌞"
        },
        "New York": {
            "name": "New York",
            "temp": 25.7,
            "feels_like": 26.2,
            "humidity": 68,
            "pressure": 1012,
            "wind_speed": 4.8,
            "description": "Rainy",
            "icon": "🌧️"
        },
    }
    return mock_data.get(city, mock_data["Tokyo"])

st.markdown("### 🌍 都市を選択してください")

col1, col2 = st.columns([3, 1])

with col1:
    city = st.selectbox(
        "都市を選択",
        ["Tokyo", "London", "Sydney", "New York"],
        label_visibility="collapsed"
    )

with col2:
    if st.button("🔄 更新", use_container_width=True):
        st.rerun()

st.divider()

# 天気データを取得
weather = get_mock_weather(city)

st.markdown(f"## {weather['icon']} {weather['name']} の天気")

# 主要情報をメトリクスで表示
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🌡️ 気温",
    f"{weather['temp']:.1f}°C",
    f"体感: {weather['feels_like']:.1f}°C"
)
col2.metric(
    "💧 湿度",
    f"{weather['humidity']}%"
)
col3.metric(
    "💨 風速",
    f"{weather['wind_speed']:.1f} m/s"
)
col4.metric(
    "🔽 気圧",
    f"{weather['pressure']} hPa"
)

st.divider()

# 現在の天気の詳細
st.markdown("### 📊 現在の条件")

weather_detail = {
    "天気": weather['description'],
    "気温": f"{weather['temp']:.1f}°C",
    "体感気温": f"{weather['feels_like']:.1f}°C",
    "湿度": f"{weather['humidity']}%",
    "風速": f"{weather['wind_speed']:.1f} m/s",
    "気圧": f"{weather['pressure']} hPa"
}

df_weather = pd.DataFrame([weather_detail]).T
df_weather.columns = ["値"]
st.dataframe(df_weather, use_container_width=True)

st.divider()

st.markdown("### 📈 5日間の予報（シミュレーション）")

# 5日間の予報データをシミュレート
forecast_dates = [datetime.now() + timedelta(days=i) for i in range(1, 6)]
forecast_temps = [
    weather['temp'] + (i * 0.5) + ((-1) ** i) * 2
    for i in range(5)
]

df_forecast = pd.DataFrame({
    "日付": [d.strftime("%m月%d日") for d in forecast_dates],
    "予想気温": forecast_temps
})

st.line_chart(df_forecast.set_index("日付"))

st.divider()

st.markdown("### 📍 複数都市の比較")

comparison_cities = ["Tokyo", "London", "Sydney", "New York"]
comparison_data = []

for c in comparison_cities:
    w = get_mock_weather(c)
    comparison_data.append({
        "都市": c,
        "気温": f"{w['temp']:.1f}°C",
        "湿度": f"{w['humidity']}%",
        "天気": w['description'],
        "アイコン": w['icon']
    })

df_comparison = pd.DataFrame(comparison_data)
st.dataframe(df_comparison, use_container_width=True, hide_index=True)

st.divider()

st.markdown("""
## 💡 実装のコツ

### 外部APIの呼び出し

```python
import requests

def get_weather(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    return response.json()
```

### エラーハンドリング

```python
try:
    weather = get_weather(city, api_key)
    st.write(f"気温: {weather['main']['temp']}°C")
except requests.exceptions.RequestException as e:
    st.error(f"API呼び出しエラー: {e}")
except KeyError:
    st.error("都市が見つかりません")
```

### APIレスポンスのキャッシュ

```python
@st.cache_data(ttl=3600)  # 1時間キャッシュ
def get_weather(city, api_key):
    # API呼び出し
    response = requests.get(...)
    return response.json()
```

---

## 🚀 応用課題

以下の機能を追加してみてください：

- [ ] **複数都市の検索** - ユーザーが任意の都市を入力できる
- [ ] **週間天気予報** - 7日間の詳細予報を表示
- [ ] **アラート機能** - 悪天候の通知
- [ ] **地図表示** - 都市の位置を地図で表示
- [ ] **言語設定** - 複数言語対応
- [ ] **データベース保存** - 閲覧履歴を保存

---

## 📚 参考資料

- [OpenWeatherMap API Documentation](https://openweathermap.org/api)
- [Streamlit requests ガイド](https://docs.streamlit.io/)
- [HTTP通信とJSON処理](https://docs.python-requests.org/)

---

**このアプリは、学習目的のデモンストレーション版です。**
実運用では、エラーハンドリング、レート制限対策、キャッシュ管理などを
さらに充実させてください。
""")

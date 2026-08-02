import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.title("👥 顧客分析ダッシュボード")

st.markdown("""
## 📌 このプロジェクトについて

このアプリは、顧客データを分析する高度なダッシュボードです。
複数の分析手法を組み合わせた、実践的なビジネスインテリジェンスアプリです。

### 学習できること
- ✅ 高度なデータ分析（RFM分析、LTV計算）
- ✅ 複雑なフィルタリング
- ✅ 複数グラフの組み合わせ
- ✅ ユーザーセグメンテーション
- ✅ KPIの計算と可視化

### 分析手法
- 📊 RFM分析（Recency, Frequency, Monetary）
- 💰 LTV計算（ライフタイムバリュー）
- 🎯 セグメンテーション
- 📈 成長分析
- 🔍 詳細分析

---

## 🎯 アプリの構成

1. **概要ダッシュボード** - 全体的なKPI表示
2. **RFM分析** - 顧客価値の分類
3. **セグメント分析** - 顧客グループの詳細分析
4. **成長分析** - 時系列での成長トレンド
5. **詳細データ** - 顧客ごとの詳細情報

---
""")

st.divider()

# サンプルデータの生成
@st.cache_data
def generate_sample_data():
    """顧客データのシミュレーション"""
    np.random.seed(42)

    # 顧客データ
    n_customers = 100
    customer_ids = [f"CUST_{i+1:04d}" for i in range(n_customers)]

    # 各顧客の購買行動をシミュレート
    data = []
    for cid in customer_ids:
        # 顧客属性
        segment = np.random.choice(["Gold", "Silver", "Bronze"])
        last_purchase_days = np.random.randint(1, 365)
        purchase_count = max(1, int(np.random.exponential(3)))
        total_spent = purchase_count * np.random.uniform(1000, 50000)
        signup_days = np.random.randint(30, 1095)  # 30日～3年前

        # LTV計算（簡易版）
        avg_order_value = total_spent / purchase_count if purchase_count > 0 else 0
        purchase_frequency = purchase_count / (signup_days / 30) if signup_days > 0 else 0
        ltv = avg_order_value * purchase_frequency * 36  # 3年間のLTV

        data.append({
            "顧客ID": cid,
            "セグメント": segment,
            "最終購買日前": last_purchase_days,
            "購買回数": purchase_count,
            "累計購買額": int(total_spent),
            "LTV": int(ltv),
            "平均注文額": int(avg_order_value),
            "登録日前": signup_days,
            "登録月": (datetime.now() - timedelta(days=signup_days)).strftime("%Y-%m")
        })

    return pd.DataFrame(data)

df = generate_sample_data()

# タブの作成
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 概要",
    "🎯 RFM分析",
    "👥 セグメント分析",
    "📈 成長分析",
    "📋 詳細データ"
])

# ========== TAB1: 概要ダッシュボード ==========
with tab1:
    st.markdown("### 📈 主要KPI")

    col1, col2, col3, col4 = st.columns(4)

    total_customers = len(df)
    total_revenue = df["累計購買額"].sum()
    avg_ltv = df["LTV"].mean()
    repeat_rate = (df["購買回数"] > 1).sum() / len(df) * 100

    col1.metric("👥 顧客数", f"{total_customers:,}")
    col2.metric("💰 総売上", f"¥{total_revenue:,}")
    col3.metric("📊 平均LTV", f"¥{avg_ltv:,.0f}")
    col4.metric("🔄 リピート率", f"{repeat_rate:.1f}%")

    st.divider()

    # グラフ
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 💰 セグメント別売上")
        segment_revenue = df.groupby("セグメント")["累計購買額"].sum()
        st.bar_chart(segment_revenue)

    with col2:
        st.markdown("#### 👥 セグメント別顧客数")
        segment_count = df["セグメント"].value_counts()
        st.bar_chart(segment_count)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📊 購買回数の分布")
        purchase_dist = df["購買回数"].value_counts().sort_index()
        st.bar_chart(purchase_dist)

    with col2:
        st.markdown("#### 📈 LTVの分布")
        ltv_bins = [0, 10000, 50000, 100000, 500000, 1000000]
        ltv_dist = pd.cut(df["LTV"], bins=ltv_bins).value_counts().sort_index()
        st.bar_chart(ltv_dist)

# ========== TAB2: RFM分析 ==========
with tab2:
    st.markdown("### 🎯 RFM分析")

    st.info("""
    **RFM分析とは？**
    - **R (Recency)** - 最後の購買からの日数が短い（最近購入）
    - **F (Frequency)** - 購買頻度が高い（よく購入）
    - **M (Monetary)** - 購買金額が大きい（多く支払う）

    これら3つの軸で顧客を分類し、価値の高い顧客を特定します。
    """)

    st.divider()

    # RFMスコア計算
    df_rfm = df.copy()

    # R: Recencyスコア（1-5）
    df_rfm["R_score"] = pd.qcut(
        df_rfm["最終購買日前"],
        q=5,
        labels=[5, 4, 3, 2, 1],
        duplicates="drop"
    ).astype(int)

    # F: Frequencyスコア（1-5）
    df_rfm["F_score"] = pd.qcut(
        df_rfm["購買回数"],
        q=5,
        labels=[1, 2, 3, 4, 5],
        duplicates="drop"
    ).astype(int)

    # M: Monetaryスコア（1-5）
    df_rfm["M_score"] = pd.qcut(
        df_rfm["累計購買額"],
        q=5,
        labels=[1, 2, 3, 4, 5],
        duplicates="drop"
    ).astype(int)

    # 総合スコア
    df_rfm["RFM_score"] = df_rfm["R_score"] + df_rfm["F_score"] + df_rfm["M_score"]

    # RFMランク分類
    def classify_rfm(score):
        if score >= 13:
            return "VIP顧客"
        elif score >= 10:
            return "優良顧客"
        elif score >= 7:
            return "一般顧客"
        else:
            return "低価値顧客"

    df_rfm["RFM_rank"] = df_rfm["RFM_score"].apply(classify_rfm)

    # RFMランク別の統計
    col1, col2, col3, col4 = st.columns(4)

    vip = len(df_rfm[df_rfm["RFM_rank"] == "VIP顧客"])
    good = len(df_rfm[df_rfm["RFM_rank"] == "優良顧客"])
    normal = len(df_rfm[df_rfm["RFM_rank"] == "一般顧客"])
    low = len(df_rfm[df_rfm["RFM_rank"] == "低価値顧客"])

    col1.metric("⭐ VIP顧客", vip)
    col2.metric("💎 優良顧客", good)
    col3.metric("📊 一般顧客", normal)
    col4.metric("📉 低価値顧客", low)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📊 RFMランク別顧客数")
        rank_dist = df_rfm["RFM_rank"].value_counts()
        st.bar_chart(rank_dist)

    with col2:
        st.markdown("#### 💰 RFMランク別平均売上")
        rank_revenue = df_rfm.groupby("RFM_rank")["累計購買額"].mean()
        st.bar_chart(rank_revenue)

    st.divider()

    # RFMスコアテーブル
    st.markdown("#### 📋 顧客別RFMスコア（上位20件）")

    display_rfm = df_rfm[[
        "顧客ID", "最終購買日前", "購買回数", "累計購買額",
        "R_score", "F_score", "M_score", "RFM_score", "RFM_rank"
    ]].sort_values("RFM_score", ascending=False).head(20)

    st.dataframe(display_rfm, use_container_width=True, hide_index=True)

# ========== TAB3: セグメント分析 ==========
with tab3:
    st.markdown("### 👥 セグメント分析")

    # セグメント選択
    selected_segment = st.multiselect(
        "分析するセグメントを選択",
        df["セグメント"].unique(),
        default=df["セグメント"].unique().tolist()
    )

    segment_df = df[df["セグメント"].isin(selected_segment)]

    if len(segment_df) == 0:
        st.warning("⚠️ 選択されたセグメントのデータがありません")
    else:
        # セグメント別統計
        st.markdown("#### 📊 セグメント別統計")

        segment_stats = segment_df.groupby("セグメント").agg({
            "顧客ID": "count",
            "累計購買額": ["sum", "mean"],
            "購買回数": "mean",
            "LTV": "mean"
        }).round(0)

        segment_stats.columns = ["顧客数", "総売上", "平均売上", "平均購買回数", "平均LTV"]
        st.dataframe(segment_stats, use_container_width=True)

        st.divider()

        # セグメント内の詳細分析
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 💰 セグメント別売上の分布")
            segment_box = segment_df.groupby("セグメント")["累計購買額"].apply(list)
            # 簡易的なボックスプロット代わりにバー表示
            st.bar_chart(
                segment_df.groupby("セグメント")["累計購買額"].agg(["min", "mean", "max"])
            )

        with col2:
            st.markdown("#### 📈 セグメント別LTV分布")
            st.bar_chart(
                segment_df.groupby("セグメント")["LTV"].agg(["min", "mean", "max"])
            )

# ========== TAB4: 成長分析 ==========
with tab4:
    st.markdown("### 📈 成長分析")

    # 月別のシミュレーション
    st.markdown("#### 📊 月別新規顧客数と売上")

    # 登録月別に集計
    monthly_stats = df.groupby("登録月").agg({
        "顧客ID": "count",
        "累計購買額": "sum"
    }).rename(columns={"顧客ID": "新規顧客数"})

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("##### 📍 新規顧客数の推移")
        st.bar_chart(monthly_stats["新規顧客数"])

    with col2:
        st.markdown("##### 📍 月別売上の推移")
        st.bar_chart(monthly_stats["累計購買額"])

    st.divider()

    # 累積グラフ
    st.markdown("#### 📈 累積顧客数と累積売上")

    cumulative_stats = monthly_stats.cumsum()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("##### 👥 累積顧客数")
        st.line_chart(cumulative_stats["新規顧客数"])

    with col2:
        st.markdown("##### 💰 累積売上")
        st.line_chart(cumulative_stats["累計購買額"])

# ========== TAB5: 詳細データ ==========
with tab5:
    st.markdown("### 📋 顧客詳細データ")

    # フィルタ条件
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_segments = st.multiselect(
            "セグメント",
            df["セグメント"].unique(),
            default=df["セグメント"].unique().tolist(),
            key="filter_segment"
        )

    with col2:
        min_ltv = st.number_input(
            "最小LTV",
            min_value=0,
            value=0,
            step=10000
        )

    with col3:
        max_ltv = st.number_input(
            "最大LTV",
            min_value=0,
            value=int(df["LTV"].max()),
            step=10000
        )

    # フィルタリング
    filtered_df = df[
        (df["セグメント"].isin(selected_segments)) &
        (df["LTV"] >= min_ltv) &
        (df["LTV"] <= max_ltv)
    ]

    st.markdown(f"#### 検出された顧客数: {len(filtered_df):,}件")

    # ソート
    sort_by = st.selectbox(
        "ソート条件",
        ["LTV（高い順）", "累計購買額（高い順）", "購買回数（多い順）", "最終購買（最近順）"]
    )

    if sort_by == "LTV（高い順）":
        filtered_df = filtered_df.sort_values("LTV", ascending=False)
    elif sort_by == "累計購買額（高い順）":
        filtered_df = filtered_df.sort_values("累計購買額", ascending=False)
    elif sort_by == "購買回数（多い順）":
        filtered_df = filtered_df.sort_values("購買回数", ascending=False)
    else:
        filtered_df = filtered_df.sort_values("最終購買日前", ascending=True)

    # データテーブル表示
    display_cols = [
        "顧客ID", "セグメント", "購買回数", "累計購買額",
        "LTV", "平均注文額", "最終購買日前"
    ]

    st.dataframe(
        filtered_df[display_cols],
        use_container_width=True,
        hide_index=True
    )

st.divider()

st.markdown("""
## 💡 実装のポイント

### RFM分析の実装

```python
# Recencyスコア（1-5）
df["R_score"] = pd.qcut(
    df["最終購買日前"],
    q=5,
    labels=[5, 4, 3, 2, 1]
).astype(int)

# RFMランク分類
def classify_rfm(r, f, m):
    score = r + f + m
    if score >= 13:
        return "VIP顧客"
    elif score >= 10:
        return "優良顧客"
    # ...
```

### セグメント別集計

```python
# セグメント別統計
segment_stats = df.groupby("セグメント").agg({
    "顧客ID": "count",
    "売上": ["sum", "mean"],
    "購買回数": "mean"
})
```

### 複雑なフィルタリング

```python
# 複数条件でフィルタ
filtered = df[
    (df["セグメント"].isin(selected)) &
    (df["LTV"] >= min_value) &
    (df["LTV"] <= max_value)
]
```

---

## 🚀 応用課題

以下の機能を追加してみてください：

- [ ] **顧客セグメンテーション** - K-means で自動セグメント作成
- [ ] **予測分析** - 離脱顧客の予測
- [ ] **コホート分析** - 同時期登録顧客の行動追跡
- [ ] **顧客生涯価値予測** - 機械学習による将来LTV予測
- [ ] **チャーン予測** - 解約リスク顧客の特定
- [ ] **推奨商品提示** - 購買履歴に基づく商品提案

---

## 📚 参考資料

- [RFM分析について](https://www.investopedia.com/terms/r/rfmanalysis.asp)
- [LTV計算ガイド](https://www.profitwell.com/blog/what-is-customer-lifetime-value)
- [Streamlit データ可視化](https://docs.streamlit.io/library/api-reference/charts)
""")

import streamlit as st
import pandas as pd
from datetime import datetime

st.title("📦 在庫管理システム")

st.markdown("""
## 📌 このプロジェクトについて

このアプリは、商品の在庫を管理するシステムです。
基本的なCRUD操作（作成、読取、更新、削除）を実装しています。

### 学習できること
- ✅ Session State による状態管理
- ✅ DataFrameのCRUD操作
- ✅ ページレイアウト設計
- ✅ ユーザー入力の検証
- ✅ データのインポート/エクスポート

### 機能一覧
- 📝 商品の追加・編集・削除
- 📊 在庫管理ダッシュボード
- 📈 在庫の推移グラフ
- 📁 CSVでのデータ管理
- ⚠️ 在庫不足アラート

---

## 🎯 アプリの構成

このアプリは以下の3つのタブで構成されています：

1. **ダッシュボード** - 在庫の概要表示
2. **在庫管理** - 商品の追加・編集・削除
3. **データ管理** - インポート・エクスポート

---
""")

st.divider()

# Session State の初期化
if "inventory" not in st.session_state:
    st.session_state.inventory = pd.DataFrame({
        "商品ID": [1, 2, 3, 4, 5],
        "商品名": ["ノート", "ペン", "消しゴム", "定規", "鉛筆"],
        "カテゴリ": ["文具", "文具", "文具", "文具", "文具"],
        "現在庫": [50, 120, 85, 30, 200],
        "最小在庫": [20, 30, 20, 10, 50],
        "単価": [100, 50, 30, 200, 20],
        "最終更新": [datetime.now()] * 5
    })

# タブの作成
tab1, tab2, tab3 = st.tabs(["📊 ダッシュボード", "📝 在庫管理", "📁 データ管理"])

# ========== TAB1: ダッシュボード ==========
with tab1:
    st.markdown("### 📈 在庫サマリー")

    inventory = st.session_state.inventory

    # 主要指標
    col1, col2, col3, col4 = st.columns(4)

    total_items = len(inventory)
    total_value = (inventory["現在庫"] * inventory["単価"]).sum()
    low_stock = len(inventory[inventory["現在庫"] < inventory["最小在庫"]])
    avg_stock = inventory["現在庫"].mean()

    col1.metric("📦 商品数", total_items)
    col2.metric("💰 総在庫価値", f"¥{total_value:,}")
    col3.metric("⚠️ 在庫不足", low_stock)
    col4.metric("📊 平均在庫", f"{avg_stock:.0f}個")

    st.divider()

    # グラフ
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📊 商品別在庫量")
        chart_data = inventory.set_index("商品名")["現在庫"]
        st.bar_chart(chart_data)

    with col2:
        st.markdown("#### 💰 商品別在庫価値")
        value_data = (inventory["現在庫"] * inventory["単価"])
        chart_value = pd.DataFrame({
            "商品": inventory["商品名"],
            "在庫価値": value_data
        }).set_index("商品")
        st.bar_chart(chart_value)

    st.divider()

    # 在庫不足アラート
    if low_stock > 0:
        st.markdown("### ⚠️ 在庫不足アラート")
        low_stock_items = inventory[inventory["現在庫"] < inventory["最小在庫"]]

        alert_data = low_stock_items[[
            "商品ID", "商品名", "現在庫", "最小在庫"
        ]].copy()
        alert_data["不足数"] = alert_data["最小在庫"] - alert_data["現在庫"]

        st.dataframe(alert_data, use_container_width=True, hide_index=True)

    st.divider()

    # 全在庫テーブル
    st.markdown("### 📋 全在庫詳細")
    display_inventory = inventory.copy()
    display_inventory["最終更新"] = display_inventory["最終更新"].dt.strftime("%Y-%m-%d %H:%M")
    display_inventory["在庫価値"] = display_inventory["現在庫"] * display_inventory["単価"]
    st.dataframe(display_inventory, use_container_width=True, hide_index=True)

# ========== TAB2: 在庫管理 ==========
with tab2:
    st.markdown("### ➕ 新規商品追加")

    sub_tab1, sub_tab2, sub_tab3 = st.tabs(["追加", "編集", "削除"])

    # 追加
    with sub_tab1:
        with st.form("add_product"):
            product_name = st.text_input("商品名 ✱")
            category = st.selectbox(
                "カテゴリ ✱",
                ["文具", "事務用品", "書籍", "その他"]
            )
            stock = st.number_input("現在庫 ✱", min_value=0, value=0)
            min_stock = st.number_input("最小在庫 ✱", min_value=0, value=0)
            price = st.number_input("単価 ✱", min_value=0, value=0)

            if st.form_submit_button("✅ 追加"):
                if not product_name.strip():
                    st.error("❌ 商品名は必須です")
                else:
                    new_id = st.session_state.inventory["商品ID"].max() + 1
                    new_product = pd.DataFrame({
                        "商品ID": [new_id],
                        "商品名": [product_name],
                        "カテゴリ": [category],
                        "現在庫": [stock],
                        "最小在庫": [min_stock],
                        "単価": [price],
                        "最終更新": [datetime.now()]
                    })
                    st.session_state.inventory = pd.concat(
                        [st.session_state.inventory, new_product],
                        ignore_index=True
                    )
                    st.success(f"✅ 商品 '{product_name}' を追加しました")

    # 編集
    with sub_tab2:
        inventory = st.session_state.inventory
        if len(inventory) > 0:
            edit_product = st.selectbox(
                "編集する商品を選択",
                inventory["商品名"].tolist(),
                key="edit_select"
            )

            idx = inventory[inventory["商品名"] == edit_product].index[0]
            current = inventory.loc[idx]

            with st.form("edit_product"):
                new_stock = st.number_input(
                    "現在庫",
                    min_value=0,
                    value=int(current["現在庫"])
                )
                new_min = st.number_input(
                    "最小在庫",
                    min_value=0,
                    value=int(current["最小在庫"])
                )
                new_price = st.number_input(
                    "単価",
                    min_value=0,
                    value=int(current["単価"])
                )

                if st.form_submit_button("✏️ 更新"):
                    st.session_state.inventory.loc[idx, "現在庫"] = new_stock
                    st.session_state.inventory.loc[idx, "最小在庫"] = new_min
                    st.session_state.inventory.loc[idx, "単価"] = new_price
                    st.session_state.inventory.loc[idx, "最終更新"] = datetime.now()
                    st.success(f"✅ '{edit_product}' を更新しました")
        else:
            st.info("📭 商品がまだありません")

    # 削除
    with sub_tab3:
        inventory = st.session_state.inventory
        if len(inventory) > 0:
            delete_product = st.selectbox(
                "削除する商品を選択",
                inventory["商品名"].tolist(),
                key="delete_select"
            )

            st.warning(f"⚠️ '{delete_product}' を削除します。この操作は取り消せません。")

            if st.button("🗑️ 削除する", type="primary"):
                st.session_state.inventory = st.session_state.inventory[
                    st.session_state.inventory["商品名"] != delete_product
                ].reset_index(drop=True)
                st.success(f"✅ '{delete_product}' を削除しました")
        else:
            st.info("📭 商品がまだありません")

# ========== TAB3: データ管理 ==========
with tab3:
    st.markdown("### 💾 データのインポート/エクスポート")

    col1, col2 = st.columns(2)

    # エクスポート
    with col1:
        st.markdown("#### 📥 エクスポート（CSV出力）")

        inventory = st.session_state.inventory
        export_df = inventory.copy()
        export_df["最終更新"] = export_df["最終更新"].dt.strftime("%Y-%m-%d %H:%M:%S")

        csv = export_df.to_csv(index=False)
        csv_bytes = csv.encode("utf-8-sig")

        st.download_button(
            label="📥 CSVをダウンロード",
            data=csv_bytes,
            file_name=f"inventory_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )

    # インポート
    with col2:
        st.markdown("#### 📤 インポート（CSV読込）")

        uploaded_file = st.file_uploader("CSVファイルを選択", type=["csv"])

        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                st.success("✅ ファイルを読み込みました")

                st.write("#### プレビュー")
                st.dataframe(df, use_container_width=True)

                if st.button("📤 データを置き換える"):
                    st.session_state.inventory = df
                    st.success("✅ 在庫データを更新しました")

            except Exception as e:
                st.error(f"❌ ファイル読み込みエラー: {e}")

    st.divider()

    st.markdown("### 📊 在庫統計")

    inventory = st.session_state.inventory

    stats_data = {
        "項目": [
            "総商品数",
            "総在庫数",
            "総在庫価値",
            "平均在庫量",
            "最大在庫",
            "最小在庫",
            "在庫不足商品数"
        ],
        "値": [
            len(inventory),
            int(inventory["現在庫"].sum()),
            f"¥{(inventory['現在庫'] * inventory['単価']).sum():,}",
            f"{inventory['現在庫'].mean():.0f}個",
            f"{inventory['現在庫'].max():.0f}個",
            f"{inventory['現在庫'].min():.0f}個",
            len(inventory[inventory["現在庫"] < inventory["最小在庫"]])
        ]
    }

    df_stats = pd.DataFrame(stats_data)
    st.dataframe(df_stats, use_container_width=True, hide_index=True)

st.divider()

st.markdown("""
## 💡 実装のポイント

### Session State による状態管理

```python
if "inventory" not in st.session_state:
    st.session_state.inventory = pd.DataFrame({...})

# 新規商品を追加
new_product = pd.DataFrame({...})
st.session_state.inventory = pd.concat(
    [st.session_state.inventory, new_product]
)
```

### DataFrame の行操作

```python
# 特定の行を取得
idx = inventory[inventory["商品名"] == name].index[0]
current = inventory.loc[idx]

# 値を更新
inventory.loc[idx, "現在庫"] = new_value

# 削除
inventory = inventory[inventory["商品名"] != name]
```

### CSV のインポート/エクスポート

```python
# エクスポート
csv = inventory.to_csv(index=False)
st.download_button(
    label="ダウンロード",
    data=csv,
    file_name="inventory.csv",
    mime="text/csv"
)

# インポート
uploaded = st.file_uploader("CSVを選択", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
```

---

## 🚀 応用課題

以下の機能を追加してみてください：

- [ ] **在庫移動履歴** - いつ、誰が、どのくらい変更したかを記録
- [ ] **自動アラート** - 在庫不足時にメール送信
- [ ] **バーコード対応** - QRコード/バーコードスキャン機能
- [ ] **複数保管場所** - 倉庫A、倉庫Bなど複数拠点対応
- [ ] **在庫予測** - 過去データから将来の在庫を予測
- [ ] **セキュリティ** - ログイン機能、操作ログ

---

## 📚 参考資料

- [Streamlit DataFrame](https://docs.streamlit.io/library/api-reference/data/st.dataframe)
- [Pandas チュートリアル](https://pandas.pydata.org/docs/user_guide/index.html)
- [CSV 処理のベストプラクティス](https://realpython.com/python-csv/)
""")

# 📍 東京地域 人口 Choropleth Map

このプロジェクトは、東京都内の市区町村ごとの人口データを視覚的に表示する **Choropleth Map（濃淡地図）** を作成したものです。  
**Leaflet.js** と **D3.js**, **GeoJSON** を使用し、人口密度を色の濃淡で表現しています。

---

## 🗂 ファイル構成

| ファイル名 | 内容 |
|------------|------|
| `tokyo_population_map.html` | 地図表示のメインHTMLファイル |
| `tokyo.geojson` | 東京都の地理情報を含む GeoJSON ファイル |
| `tokyo.csv` | 各地域の人口データ（例：`世田谷区,939099`） |
| `Screenshot 2025-07-07 at 21.02.12.png` | 実行結果のスクリーンショット |

※ 上記のファイルはすべて **同一ディレクトリに配置**してください。

---

## 🔧 使用ライブラリ

- [Leaflet.js](https://leafletjs.com/) - 地図描画用ライブラリ
- [D3.js](https://d3js.org/) - データ読み込みおよび処理
- GeoJSON - 地理情報フォーマット

---

## 🚀 使い方

### 方法①：ブラウザで直接開く（簡易）

1. このリポジトリを clone または zip でダウンロード
2. `tokyo_population_map.html` をダブルクリックでブラウザで開く

※ 一部のブラウザでは `fetch()` によるローカルファイル読み込み制限があるため、下記の「方法②」を推奨

---

### 方法②：ローカルサーバーで起動（推奨）

```bash
cd /path/to/project
python3 -m http.server 8000
```

その後、ブラウザで以下のURLにアクセス：

```
http://localhost:8000/tokyo_population_map.html
```

---

## 📊 データ形式について

### `tokyo.csv`

```csv
地域,人口
世田谷区,939099
足立区,695121
...
```

- `tokyo.geojson` の地域名と一致している必要があります（例：「世田谷区」）

---

## 🗺️ サンプル画像

以下は実際に生成された Choropleth Map のスクリーンショットです：

![choropleth map](Screenshot%202025-07-07%20at%2021.02.12.png)

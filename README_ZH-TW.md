# Crypto News51 MCP Server

[English](./README_EN.md) | [简体中文](./README.md) | 繁體中文

## 🚀 使用 EMCP 平台快速體驗

**[EMCP](https://sit-emcp.kaleido.guru)** 是一個強大的 MCP 伺服器管理平台，讓您無需手動配置即可快速使用各種 MCP 伺服器！

### 快速開始：

1. 🌐 造訪 **[EMCP 平台](https://sit-emcp.kaleido.guru)**
2. 📝 註冊並登入帳號
3. 🎯 進入 **MCP 廣場**，瀏覽所有可用的 MCP 伺服器
4. 🔍 搜尋或找到本伺服器（`bach-crypto_news51`）
5. 🎉 點擊 **「安裝 MCP」** 按鈕
6. ✅ 完成！即可在您的應用中使用

### EMCP 平台優勢：

- ✨ **零配置**：無需手動編輯配置檔案
- 🎨 **視覺化管理**：圖形介面輕鬆管理所有 MCP 伺服器
- 🔐 **安全可靠**：統一管理 API 金鑰和認證資訊
- 🚀 **一鍵安裝**：MCP 廣場提供豐富的伺服器選擇
- 📊 **使用統計**：即時查看服務調用情況

立即造訪 **[EMCP 平台](https://sit-emcp.kaleido.guru)** 開始您的 MCP 之旅！


---

## 簡介

這是一個使用 [FastMCP](https://fastmcp.wiki) 自動生成的 MCP 伺服器，用於存取 Crypto News51 API。

- **PyPI 套件名**: `bach-crypto_news51`
- **版本**: 1.0.0
- **傳輸協定**: stdio


## 安装

### 从 PyPI 安装:

```bash
pip install bach-crypto_news51
```

### 从源码安装:

```bash
pip install -e .
```

## 运行

### 方式 1: 使用 uvx（推荐，无需安装）

```bash
# 运行（uvx 会自动安装并运行）
uvx --from bach-crypto_news51 bach_crypto_news51

# 或指定版本
uvx --from bach-crypto_news51@latest bach_crypto_news51
```

### 方式 2: 直接运行（开发模式）

```bash
python server.py
```

### 方式 3: 安装后作为命令运行

```bash
# 安装
pip install bach-crypto_news51

# 运行（命令名使用下划线）
bach_crypto_news51
```

## 配置

### API 認證

此 API 需要認證。請設定環境變數:

```bash
export API_KEY="your_api_key_here"
```

### 環境變數

| 變數名 | 說明 | 必需 |
|--------|------|------|
| `API_KEY` | API 金鑰 | 是 |
| `PORT` | 不適用 | 否 |
| `HOST` | 不適用 | 否 |



### 在 Claude Desktop 中使用

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:


```json
{
  "mcpServers": {
    "crypto_news51": {
      "command": "python",
      "args": ["E:\path\to\crypto_news51\server.py"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**注意**: 請將 `E:\path\to\crypto_news51\server.py` 替換為實際的伺服器檔案路徑。


## 可用工具

此服务器提供以下工具:


### `coins_price_list`

The project returns cryptocurrency prices.

**端点**: `GET /api/v1/mini-crypto/prices`


**参数**:

- `base_currency` (string) *必需*: Supported over 140+ fiat currencies.

- `page` (number) *必需*: Example value: 1

- `page_size` (number) *必需*: maximum: 100



---


### `crypto_rates`

Returns cryptocurrency prices based on the selected fiat or crypto base currency.

**端点**: `GET /api/v1/convert-rates/crypto/from`


**参数**:

- `detailed` (string): Example value: 

- `currency` (string) *必需*: example: (USD, EUR, BTC, ETH...)



---


### `fiat_supported`

Returns a list of all supported fiat currency symbols and their full names.

**端点**: `GET /api/v1/fiat-currencies`



---


### `listing_delisting`

listing-delisting

**端点**: `GET /api/v1/crypto/listing_delisting`


**参数**:

- `sort_by` (string): Sort by 'published' or 'event' date



---


### `crypto_txs`

crypto_txs

**端点**: `GET /api/v1/crypto/transactions`



---


### `latest_news_search_by_keyword`

Search for articles that contain a specific keyword in the title.

**端点**: `GET /api/v1/news/articles/search`


**参数**:

- `keyword` (string): Example value: Microsoft

- `page` (number): Example value: 1

- `page_size` (number): Example value: 10



---


### `latest_news`

Retrieve a list of articles sorted by published_utc with pagination support.

**端点**: `GET /api/v1/news/articles`


**参数**:

- `page` (number): Example value: 1

- `page_size` (number): Example value: 10



---


### `crypto_articles_search_by_keywords`

Retrieve a list of crypto-related articles published in the last 24 hours. Articles are sorted from newest to oldest and can be filtered using keywords. Specify keywords in the query parameters to refine the search.

**端点**: `GET /api/v1/crypto/articles/search`


**参数**:

- `title_keywords` (string) *必需*: Enter a word or phrase to filter by in the title. The filter checks for exact matches of the word or phrase in the title.

- `page` (number): Page number

- `limit` (number): Specify the number of articles per page; maximum limit is 100.

- `time_frame` (string): Specify the timeframe for the articles. Choose from 1h, 6h, 12h, 24h.

- `format` (string): Specify the format of the response. Choose from 'json' or 'csv'.



---


### `sentiment_analysis`

Returns the number of articles by sentiment label within the selected time interval.

**端点**: `GET /api/v1/crypto/sentiment`


**参数**:

- `interval` (string): Specify the time interval for sentiment analysis using format like '1h', '6h', '12h', '1d', '7d'. 'h' = hours, 'd' = days.



---


### `article_statistics`

Returns statistics on the number of articles published within specific time intervals (1, 4, 8, 12, 24 hours) from various RSS feeds.

**端点**: `GET /api/v1/crypto/statistics`



---


### `crypto_historical_articles`

Returns a list of Articles from the last 30 days. The Articles are sorted from newest to oldest.

**端点**: `GET /api/v1/crypto/historical_articles`


**参数**:

- `limit` (number): Specify the number of articles per page; maximum limit is 100.

- `format` (string): Specify the format of the response. Choose from 'json' or 'csv'.

- `source` (string): Enter the source name. Check all source names at Source List. Accepts only one value.

- `page` (number): Page number

- `time_frame` (string): Specify the timeframe for the articles. Choose from 2d, 3d, 4d, 5d, 6d, 7d, 30d.



---


### `source_list`

Returns a list of sources that can be used as a 'source' parameter in the '/crypto/articles' endpoint. This allows clients to filter articles by specific sources. For example: /crypto/articles?source=source_name.

**端点**: `GET /api/v1/crypto/sources`



---


### `crypto_articles`

Returns a list of Articles from the last 24 hours. The Articles are sorted from newest to oldest.

**端点**: `GET /api/v1/crypto/articles`


**参数**:

- `page` (number): Page number

- `limit` (number): Specify the number of articles per page; maximum limit is 100.

- `time_frame` (string): Specify the timeframe for the articles. Choose from 1h, 6h, 12h, 24h.

- `format` (string): Specify the format of the response. Choose from 'json' or 'csv'.

- `source` (string): Enter the source name. Check all source names at Source List. Accepts only one value.



---



## 技术栈

- **FastMCP**: 快速、Pythonic 的 MCP 服务器框架
- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 开发

此伺服器由 [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) 工具自動生成。

版本: 1.0.0

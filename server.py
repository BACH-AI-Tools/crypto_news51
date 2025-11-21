"""
Crypto News51 MCP Server

使用 FastMCP 的 from_openapi 方法自动生成

Version: 1.0.0
Transport: stdio
"""
import os
import json
import httpx
from fastmcp import FastMCP

# 服务器版本和配置
__version__ = "1.0.0"
__tag__ = "crypto_news51/1.0.0"

# API 配置
API_KEY = os.getenv("API_KEY", "")

# 传输协议配置
TRANSPORT = "stdio"


# OpenAPI 规范
OPENAPI_SPEC = """{\n  \"openapi\": \"3.0.0\",\n  \"info\": {\n    \"title\": \"Crypto News51\",\n    \"version\": \"1.0.0\",\n    \"description\": \"RapidAPI: apiwizard/crypto-news51\"\n  },\n  \"servers\": [\n    {\n      \"url\": \"https://crypto-news51.p.rapidapi.com\"\n    }\n  ],\n  \"paths\": {\n    \"/api/v1/mini-crypto/prices\": {\n      \"get\": {\n        \"summary\": \"Coins Price List\",\n        \"description\": \"The project returns cryptocurrency prices.\",\n        \"operationId\": \"coins_price_list\",\n        \"parameters\": [\n          {\n            \"name\": \"base_currency\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Supported over 140+ fiat currencies.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"page\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: 1\",\n            \"schema\": {\n              \"type\": \"number\",\n              \"default\": \"1\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"page_size\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"maximum: 100\",\n            \"schema\": {\n              \"type\": \"number\",\n              \"default\": \"20\",\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/v1/convert-rates/crypto/from\": {\n      \"get\": {\n        \"summary\": \"Crypto Rates\",\n        \"description\": \"Returns cryptocurrency prices based on the selected fiat or crypto base currency.\",\n        \"operationId\": \"crypto_rates\",\n        \"parameters\": [\n          {\n            \"name\": \"detailed\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: \",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"currency\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"example: (USD, EUR, BTC, ETH...)\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/v1/fiat-currencies\": {\n      \"get\": {\n        \"summary\": \"Fiat Supported\",\n        \"description\": \"Returns a list of all supported fiat currency symbols and their full names.\",\n        \"operationId\": \"fiat_supported\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/v1/crypto/listing_delisting\": {\n      \"get\": {\n        \"summary\": \"listing-delisting\",\n        \"description\": \"listing-delisting\",\n        \"operationId\": \"listing_delisting\",\n        \"parameters\": [\n          {\n            \"name\": \"sort_by\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Sort by 'published' or 'event' date\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/v1/crypto/transactions\": {\n      \"get\": {\n        \"summary\": \"crypto_txs\",\n        \"description\": \"crypto_txs\",\n        \"operationId\": \"crypto_txs\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/v1/news/articles/search\": {\n      \"get\": {\n        \"summary\": \"Latest News Search by Keyword\",\n        \"description\": \"Search for articles that contain a specific keyword in the title.\",\n        \"operationId\": \"latest_news_search_by_keyword\",\n        \"parameters\": [\n          {\n            \"name\": \"keyword\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: Microsoft\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"page\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: 1\",\n            \"schema\": {\n              \"type\": \"number\",\n              \"default\": \"1\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"page_size\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: 10\",\n            \"schema\": {\n              \"type\": \"number\",\n              \"default\": \"10\",\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/v1/news/articles\": {\n      \"get\": {\n        \"summary\": \"Latest News\",\n        \"description\": \"Retrieve a list of articles sorted by published_utc with pagination support.\",\n        \"operationId\": \"latest_news\",\n        \"parameters\": [\n          {\n            \"name\": \"page\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: 1\",\n            \"schema\": {\n              \"type\": \"number\",\n              \"default\": \"1\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"page_size\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: 10\",\n            \"schema\": {\n              \"type\": \"number\",\n              \"default\": \"10\",\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/v1/crypto/articles/search\": {\n      \"get\": {\n        \"summary\": \"Crypto Articles Search by Keywords\",\n        \"description\": \"Retrieve a list of crypto-related articles published in the last 24 hours. Articles are sorted from newest to oldest and can be filtered using keywords. Specify keywords in the query parameters to refine the search.\",\n        \"operationId\": \"crypto_articles_search_by_keywords\",\n        \"parameters\": [\n          {\n            \"name\": \"title_keywords\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Enter a word or phrase to filter by in the title. The filter checks for exact matches of the word or phrase in the title.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"page\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Page number\",\n            \"schema\": {\n              \"type\": \"number\",\n              \"default\": \"1\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"limit\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Specify the number of articles per page; maximum limit is 100.\",\n            \"schema\": {\n              \"type\": \"number\",\n              \"default\": \"10\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"time_frame\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Specify the timeframe for the articles. Choose from 1h, 6h, 12h, 24h.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"format\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Specify the format of the response. Choose from 'json' or 'csv'.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/v1/crypto/sentiment\": {\n      \"get\": {\n        \"summary\": \"Sentiment Analysis\",\n        \"description\": \"Returns the number of articles by sentiment label within the selected time interval.\",\n        \"operationId\": \"sentiment_analysis\",\n        \"parameters\": [\n          {\n            \"name\": \"interval\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Specify the time interval for sentiment analysis using format like '1h', '6h', '12h', '1d', '7d'. 'h' = hours, 'd' = days.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/v1/crypto/statistics\": {\n      \"get\": {\n        \"summary\": \"Article Statistics\",\n        \"description\": \"Returns statistics on the number of articles published within specific time intervals (1, 4, 8, 12, 24 hours) from various RSS feeds.\",\n        \"operationId\": \"article_statistics\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/v1/crypto/historical_articles\": {\n      \"get\": {\n        \"summary\": \"Crypto Historical Articles\",\n        \"description\": \"Returns a list of Articles from the last 30 days. The Articles are sorted from newest to oldest.\",\n        \"operationId\": \"crypto_historical_articles\",\n        \"parameters\": [\n          {\n            \"name\": \"limit\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Specify the number of articles per page; maximum limit is 100.\",\n            \"schema\": {\n              \"type\": \"number\",\n              \"default\": \"10\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"format\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Specify the format of the response. Choose from 'json' or 'csv'.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"source\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Enter the source name. Check all source names at Source List. Accepts only one value.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"page\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Page number\",\n            \"schema\": {\n              \"type\": \"number\",\n              \"default\": \"1\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"time_frame\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Specify the timeframe for the articles. Choose from 2d, 3d, 4d, 5d, 6d, 7d, 30d.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/v1/crypto/sources\": {\n      \"get\": {\n        \"summary\": \"Source List\",\n        \"description\": \"Returns a list of sources that can be used as a 'source' parameter in the '/crypto/articles' endpoint. This allows clients to filter articles by specific sources. For example: /crypto/articles?source=source_name.\",\n        \"operationId\": \"source_list\",\n        \"parameters\": [],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/api/v1/crypto/articles\": {\n      \"get\": {\n        \"summary\": \"Crypto Articles\",\n        \"description\": \"Returns a list of Articles from the last 24 hours. The Articles are sorted from newest to oldest.\",\n        \"operationId\": \"crypto_articles\",\n        \"parameters\": [\n          {\n            \"name\": \"page\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Page number\",\n            \"schema\": {\n              \"type\": \"number\",\n              \"default\": \"1\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"limit\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Specify the number of articles per page; maximum limit is 100.\",\n            \"schema\": {\n              \"type\": \"number\",\n              \"default\": \"10\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"time_frame\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Specify the timeframe for the articles. Choose from 1h, 6h, 12h, 24h.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"format\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Specify the format of the response. Choose from 'json' or 'csv'.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"source\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Enter the source name. Check all source names at Source List. Accepts only one value.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    }\n  },\n  \"components\": {\n    \"securitySchemes\": {\n      \"ApiAuth\": {\n        \"type\": \"apiKey\",\n        \"in\": \"header\",\n        \"name\": \"X-RapidAPI-Key\"\n      }\n    }\n  },\n  \"security\": [\n    {\n      \"ApiAuth\": []\n    }\n  ]\n}"""

# 创建 HTTP 客户端
# 设置默认 headers
default_headers = {}


# RapidAPI 必需的 headers
if API_KEY:
    default_headers["X-RapidAPI-Key"] = API_KEY
    default_headers["X-RapidAPI-Host"] = "crypto-news51.p.rapidapi.com"
else:
    print("⚠️  警告: 未设置 API_KEY 环境变量")
    print("   RapidAPI 需要 API Key 才能正常工作")
    print("   请设置: export API_KEY=你的RapidAPI-Key")

# 对于 POST/PUT/PATCH 请求，自动添加 Content-Type
default_headers["Content-Type"] = "application/json"




client = httpx.AsyncClient(
    base_url="https://crypto-news51.p.rapidapi.com", 
    timeout=30.0
)


# 从 OpenAPI 规范创建 FastMCP 服务器
openapi_dict = json.loads(OPENAPI_SPEC)
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_dict,
    client=client,
    name="crypto_news51",
    version=__version__
)


# 注册请求拦截器，为所有请求添加 RapidAPI headers
_original_request = client.request

async def _add_rapidapi_headers(method, url, **kwargs):
    """拦截所有请求，添加必需的 RapidAPI headers"""
    # 确保 headers 存在
    if 'headers' not in kwargs:
        kwargs['headers'] = {}
    
    # 添加 RapidAPI 必需的 headers
    if API_KEY:
        kwargs['headers']['X-RapidAPI-Key'] = API_KEY
        kwargs['headers']['X-RapidAPI-Host'] = "crypto-news51.p.rapidapi.com"
    else:
        print("⚠️  警告: API_KEY 未设置，请求可能失败")
    
    # 对于 POST/PUT/PATCH，添加 Content-Type
    if method.upper() in ['POST', 'PUT', 'PATCH']:
        if 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'
    
    return await _original_request(method, url, **kwargs)

# 替换 request 方法
client.request = _add_rapidapi_headers


def main():
    """主入口点"""
    print(f"🚀 启动 Crypto News51 MCP 服务器")
    print(f"📦 版本: {__tag__}")
    print(f"🔧 传输协议: {TRANSPORT}")
    
    print()
    
    # 运行服务器
    
    mcp.run(transport="stdio")
    


if __name__ == "__main__":
    main()
import requests
import redis
import json
from newspaper import Article
from duckduckgo_search import DDGS
from datetime import datetime
import os
# Configuration
REDIS_HOST = str(os.getenv('REDIS_HOST'))
REDIS_PORT = int(str(os.getenv('REDIS_PORT')))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
NEWS_API_URL = str(os.getenv('NEWS_API_URL'))


# Create a Redis connection
r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    decode_responses=True
)

# Clear the Redis database
# Scrape article function
from datetime import datetime
# Scrape article function
def scrape_article(url: str) -> dict:
    try:
        result = DDGS().text(url, max_results=1)
        if url:
            article_url = result[0]['href']
            print(url)
            article = Article(article_url)
            article.download()
            article.parse()
            article.nlp()
            # Check if publish_date is a datetime object
            publish_date = article.publish_date
            if isinstance(publish_date, datetime):
                publish_date_str = publish_date.strftime('%Y-%m-%dT%H:%M:%S')
            else:
                publish_date_str = None

            return {
                'title': article.title,
                'authors': article.authors,
                'publish_date': publish_date_str,
                'text': article.text,
                'summary': article.summary,
                'keywords': article.keywords,
                'image': article.top_image
            }
    except Exception as e:
        print(f"Error scraping article: {e}")
        return {"error": str(e)}
    return {"error": "Unable to scrape article"}

def fetch_and_cache_news():
    news_list = []
    for page in range(1, 6):  # Fetch 5 pages of news
        try:
            params = {
                'pageSize': 40,
                'page': page,
            }
            response = requests.get(NEWS_API_URL, params=params)
            response.raise_for_status()
            data = response.json()
            articles = data.get('articles', [])
            for article in articles:
                news_list.append({
                    'title': article.get('title'),
                    'url': article.get('url')
                })
        except requests.RequestException as e:
            print(f"Failed to fetch news page {page}: {e}")
            continue

    # Cache articles in pages of 35
    page_size = 35
    for i in range(0, len(news_list), page_size):
        page_number = (i // page_size) + 1
        page_articles = news_list[i:i + page_size]
        article_data_list = []
        for news in page_articles:
            try:
                article_data = scrape_article(news['title'])
                article_data_list.append(article_data)
            except Exception as e:
                print(f"Failed to process article {news['url']}: {e}")
                continue
        
        try:
            r.set(f'news_page:{page_number}', json.dumps(article_data_list))
            print(f"Cached page {page_number} with {len(article_data_list)} articles")
        except TypeError as e:
            print(f"Error serializing data for page {page_number}: {e}")


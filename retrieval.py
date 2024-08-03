import json
import asyncio
import redis
from typing import Union, Dict, List
import os
REDIS_HOST = str(os.getenv('REDIS_HOST'))
REDIS_PORT = int(os.getenv('REDIS_PORT', 13923))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

# Redis configuration
def get_articles_by_page(page_number: int) -> Union[List[Dict], Dict]:
    try:
        r = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD,
            decode_responses=True
        )
        data = r.get(f'news_page:{page_number}')
        print(f"Raw data: {data}")  # Debugging line
        print(f"Type of data: {type(data)}")  # Debugging line

        if data is None:
            return {"error": "No articles found for this page"}
        
        if isinstance(data, str):
            try:
                articles = json.loads(data)
                return articles
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return {"error": "Error decoding data"}
        elif isinstance(data, (list, dict)):
            # If Redis returns already deserialized data
            return data
        else:
            print(f"Unexpected data type: {type(data)}")
            return {"error": "Unexpected data format"}

    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": "An unexpected error occurred"}

if __name__ == "__main__":
    page_number = 1  # Example page number
    articles = get_articles_by_page(page_number)
    print(articles)
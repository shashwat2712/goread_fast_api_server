from typing import List, Dict, Union
from fastapi import FastAPI, HTTPException
from redis import asyncio as aioredis
import json
from scrap_route import scrap_router
import os
from threading import Thread

from update_cache import fetch_and_cache_news
REDIS_HOST = str(os.getenv('REDIS_HOST'))
REDIS_PORT = int(os.getenv('REDIS_PORT', 13923))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

# Initialize FastAPI
app = FastAPI()

app.include_router(scrap_router, prefix="")

# Asynchronous Redis client
async def get_redis_client():
    return aioredis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        password=REDIS_PASSWORD,
        decode_responses=True
    )

# Asynchronous function to get articles by page number from Redis
async def get_articles_by_page(page_number: int) -> Union[List[Dict], Dict]:
    try:
        r = await get_redis_client()
        data = await r.get(f'news_page:{page_number}')
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

# FastAPI route to get articles by page
@app.get("/get-latest-news/{page_number}")
async def get_latest_news(page_number: int):
    articles = await get_articles_by_page(page_number)
    
    # Ensure articles is a dictionary before accessing its keys
    if isinstance(articles, dict) and "error" in articles:
        raise HTTPException(status_code=404, detail=articles["error"])
    return {"latest_news": articles}


@app.get("/update-news")
async def update_news():
    # Run fetch_and_cache_news in a separate thread
    thread = Thread(target=fetch_and_cache_news)
    thread.start()
    return {"status": "update started"}


# FastAPI route to get articles by page
@app.get("/get-latest-news-dummy")
async def get_latest_news_dummy():
    articles = json.loads('''{
        "latest_news": [
            {
                "title": "Olympic Games Paris 2024 Highlights Day 4: Manu Bhaker-Sarabjot Singh Win Bronze, Archer Bhajan Shines",
                "authors": [
                    "Ndtv Sports Desk"
                ],
                "publish_date": null,
                "text": "Paris Olympics 2024 Day 4, Live: Another stunning result in tennis\\n\\nEgypt reached the quarter-finals of the men's Olympic football after completing the group stage with a surprise 2-1 win over already qualified Spain on Tuesday, with Ibrahim Adel scoring both goals.\\n\\n\\n\\n\\nAdel gave Egypt the lead in Bordeaux with a superb strike late in the first half and added another on 62 minutes, pouncing to score after possession was given away by Spain's Jon Pacheco.\\n\\n\\n\\n\\nSamu Omorodion pulled one back late on for Spain, but Egypt held on for the win that allowed them to leapfrog their already-qualified opponents and snatch first place in Group C.",
                "summary": "Paris Olympics 2024 Day 4, Live: Another stunning result in tennisEgypt reached the quarter-finals of the men's Olympic football after completing the group stage with a surprise 2-1 win over already qualified Spain on Tuesday, with Ibrahim Adel scoring both goals.\\nAdel gave Egypt the lead in Bordeaux with a superb strike late in the first half and added another on 62 minutes, pouncing to score after possession was given away by Spain's Jon Pacheco.\\nSamu Omorodion pulled one back late on for Spain, but Egypt held on for the win that allowed them to leapfrog their already-qualified opponents and snatch first place in Group C.",
                "keywords": [
                    "shines",
                    "paris",
                    "late",
                    "highlights",
                    "singh",
                    "games",
                    "strike",
                    "manu",
                    "surprise",
                    "superb",
                    "egypt",
                    "olympic",
                    "win",
                    "bronze",
                    "group",
                    "tennisegypt",
                    "spain",
                    "day",
                    "stunning"
                ],
                "image": "https://c.ndtvimg.com/2024-07/27vcqib8_manu-bhaker-and-sarabjot-singh_625x300_30_July_24.jpeg?im=FitAndFill,algorithm=dnn,width=1200,height=738"
            },
            {
                "title": "Olympic Games Paris 2024 Highlights Day 4: Manu Bhaker-Sarabjot Singh Win Bronze, Archer Bhajan Shines",
                "authors": [
                    "Ndtv Sports Desk"
                ],
                "publish_date": null,
                "text": "Paris Olympics 2024 Day 4, Live: Another stunning result in tennis\\n\\nEgypt reached the quarter-finals of the men's Olympic football after completing the group stage with a surprise 2-1 win over already qualified Spain on Tuesday, with Ibrahim Adel scoring both goals.\\n\\n\\n\\n\\nAdel gave Egypt the lead in Bordeaux with a superb strike late in the first half and added another on 62 minutes, pouncing to score after possession was given away by Spain's Jon Pacheco.\\n\\n\\n\\n\\nSamu Omorodion pulled one back late on for Spain, but Egypt held on for the win that allowed them to leapfrog their already-qualified opponents and snatch first place in Group C.",
                "summary": "Paris Olympics 2024 Day 4, Live: Another stunning result in tennisEgypt reached the quarter-finals of the men's Olympic football after completing the group stage with a surprise 2-1 win over already qualified Spain on Tuesday, with Ibrahim Adel scoring both goals.\\nAdel gave Egypt the lead in Bordeaux with a superb strike late in the first half and added another on 62 minutes, pouncing to score after possession was given away by Spain's Jon Pacheco.\\nSamu Omorodion pulled one back late on for Spain, but Egypt held on for the win that allowed them to leapfrog their already-qualified opponents and snatch first place in Group C.",
                "keywords": [
                    "shines",
                    "paris",
                    "late",
                    "highlights",
                    "singh",
                    "games",
                    "strike",
                    "manu",
                    "surprise",
                    "superb",
                    "egypt",
                    "olympic",
                    "win",
                    "bronze",
                    "group",
                    "tennisegypt",
                    "spain",
                    "day",
                    "stunning"
                ],
                "image": "https://c.ndtvimg.com/2024-07/27vcqib8_manu-bhaker-and-sarabjot-singh_625x300_30_July_24.jpeg?im=FitAndFill,algorithm=dnn,width=1200,height=738"
            }
        ]
    }''')
    
    # Directly return the articles list without additional error handling
    return {"latest_news": articles["latest_news"]}
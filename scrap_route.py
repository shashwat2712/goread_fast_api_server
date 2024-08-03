from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import asyncio
from concurrent.futures import ThreadPoolExecutor
from scrapper import scrape_article

scrap_router = APIRouter()

class ScrapRequest(BaseModel):
    keyword: str

# Create a ThreadPoolExecutor to run synchronous code in a separate thread
executor = ThreadPoolExecutor(max_workers=100)

# Define an async function to run the synchronous function in the executor
async def run_sync_scrape_article(url: str) -> dict:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, scrape_article, url)

@scrap_router.post("/scrap-website")
async def get_items(scrape_request: ScrapRequest):
    url = scrape_request.keyword
    try:
        result = await run_sync_scrape_article(url)
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code= 500, detail=str(e))
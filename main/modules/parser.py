import asyncio
import logging
import feedparser
from main.modules.schedule import update_schedule
from main.modules.utils import status_text
from main import status
from main.modules.db import get_animesdb, get_uploads, save_animedb
from main import queue
from main.inline import button1

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def trim_title(title: str):
    title, ext = title.replace("[SubsPlease]", "").strip().split("[", maxsplit=2)
    _, ext = ext.split("]", maxsplit=2)
    title = title.strip() + ext
    return title

def parse():
    feed = feedparser.parse("https://subsplease.org/rss/")
    entries = feed["entries"]
    data = []

    for entry in entries:
        item = {
            'title': trim_title(entry['title']),
            'size': entry['subsplease_size'],
            'link': entry['link']
        }
        data.append(item)

    data.reverse()
    return data

async def fetch_and_save_anime():
    rss = parse()
    data = await get_animesdb()
    uploaded = await get_uploads()

    saved_anime = [anime["name"] for anime in data]
    uanimes = [anime["name"] for anime in uploaded]

    for item in rss:
        if item["title"] not in uanimes and item["title"] not in saved_anime:
            if ".mkv" in item["title"] or ".mp4" in item["title"]:
                title = item["title"]
                await save_animedb(title, item)

async def update_queue():
    data = await get_animesdb()
    for anime in data:
        if anime["data"] not in queue:
            queue.append(anime["data"])
            logger.info(f"Saved {anime['name']}")

async def auto_parser():
    while True:
        try:
            await status.edit(await status_text("Parsing Rss, Fetching Magnet Links..."), reply_markup=button1)
        except Exception as e:
            logger.error(f"Error updating status: {e}")

        await fetch_and_save_anime()
        await update_queue()

        try:
            await status.edit(await status_text("Idle..."), reply_markup=button1)
            await update_schedule()
        except Exception as e:
            logger.error(f"Error updating schedule: {e}")

        await asyncio.sleep(600)

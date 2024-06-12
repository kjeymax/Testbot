import os
from dotenv import load_dotenv

if os.path.exists("config.env"):
    load_dotenv('config.env')
elif os.path.exists("sample.env"):
    load_dotenv("sample.env")

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_DB_URI = os.getenv("MONGO_DB_URI")
UPLOAD_ID = os.getenv("UPLOAD_ID")
INDEX_ID  = os.getenv("INDEX_ID ")
STATUS_ID = os.getenv("STATUS_ID")
SCHEDULE_ID = os.getenv("SCHEDULE_ID")
CHANNEL_TITLE = os.getenv("CHANNEL_TITLE", "H-Anime")
INDEX_USERNAME = os.getenv("INDEX_USERNAME")
UPLOADS_USERNAME = os.getenv("UPLOADS_USERNAME")
COMMENTS_GROUP_LINK = os.getenv("COMMENTS_GROUP_LINK")
SLEEP_TIME = os.getenv("SLEEP_TIME", 15)

for k, v in {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
    "MONGO_DB_URI": MONGO_DB_URI,
    "STATUS_ID": STATUS_MSG_ID,
    "SCHEDULE_ID": SCHEDULE_MSG_ID,
    "UPLOAD_ID": UPLOAD_ID
    "INDEX_ID": INDEX_ID   
    "INDEX_USERNAME": INDEX_CHANNEL_USERNAME,
    "UPLOADS_USERNAME": UPLOADS_CHANNEL_USERNAME,
    "COMMENTS_GROUP_LINK": COMMENTS_GROUP_LINK,
}.items():
    if not v:
        raise Exception(f"{k} not found .env file, please add it to use H-Anime Bot")

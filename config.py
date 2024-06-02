import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    BOT_TOKEN = os.getenv("")
    API_ID = os.getenv("")
    API_HASH = os.getenv("")
    mediaPattern = r"\b(https?://(?:(.*?)\.)?(?:instagram\.com|instagr\.am|t\.co|twitter\.com)(?:[^\s]*))\b" #pin\.it|pinterest\.com|

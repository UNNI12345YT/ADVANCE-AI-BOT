import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    BOT_TOKEN = os.getenv("7406041849:AAFMFUK7700jzSA8UaSPhYQgJa0N4rCdl3U")
    API_ID = os.getenv("27500064")
    API_HASH = os.getenv("690dc5633ef234f04f3825a7c1ad0272")
    mediaPattern = r"\b(https?://(?:(.*?)\.)?(?:instagram\.com|instagr\.am|t\.co|twitter\.com)(?:[^\s]*))\b" #pin\.it|pinterest\.com|

import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    BOT_TOKEN = os.getenv("7406041849:AAHPK3rCTnKcbLRjTxHoTP_3joR1MHAR1MU")
    API_ID = os.getenv("27408015")
    API_HASH = os.getenv("2f07e7c921c8d2b982df12d65a46ca46")
    mediaPattern = r"\b(https?://(?:(.*?)\.)?(?:instagram\.com|instagr\.am|t\.co|twitter\.com)(?:[^\s]*))\b" #pin\.it|pinterest\.com|

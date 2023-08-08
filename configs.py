# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "22593455"))
    API_HASH = os.environ.get("API_HASH", "06f476be3b54eea95126c9acdf6fc775")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6310818021:AAEm_pKoHeVxvMxa2AemeCLjYsNgTPlexbc")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 1445283714))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "6038012760 1642086010").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://hesibir476:1234@cluster0.slqkjop.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001916608066"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))

from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "26052688"))
API_HASH = getenv("API_HASH", "8def87132fca56eaa182f28c70f6ecb6")

BOT_TOKEN = getenv("BOT_TOKEN", "6178098626:AAEw3uh637OuQvvVoKsCK5-6RP5rRIWlJFQ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5905205047"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "FlorenzaNetwork")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "zaapNetwork")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2002353404").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

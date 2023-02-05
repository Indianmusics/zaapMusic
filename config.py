from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "23474437"))
API_HASH = getenv("API_HASH", "f31f35ad9ef183e45184398fa1c120c7")

BOT_TOKEN = getenv("BOT_TOKEN", "6178098626:AAEw3uh637OuQvvVoKsCK5-6RP5rRIWlJFQ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5905205047"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BQFmMQUAsAsPegNnqz-R2kSA9OtbNi5ro_mbAcCXaEVzxg5ZAJieqpHY-pcZL3Mbt-tsPIWzjyfFSK6dOfA0e4GTLJodX6viBlhxglnZci6PPxriUymBt5ihe7HnkOxyN-k6X5XdeQBNKQtvvOKfk_c3iNAoXhJeLGwZnWFwciwNb5R4wpqTJ0CQBeu9iBosjSyWZ0wnlFizAlNuL9UF5s_FufxuOvmyw06V-hidRzyzxNCIUfBWeX4htuVpQh6Iu-oMXC4YOeJ7GYzphswkA-bGON7HPQOqngmFNiPY_WDf4-Z4F7qhSFAmJDvyxsPq--lf4A5HpzFG02Fw7CTkrHY0rz-LBgAAAAFTyworAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "FlorenzaNetwork")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "zaapNetwork")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5700782635").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

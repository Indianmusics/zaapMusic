from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "13685763"))
API_HASH = getenv("API_HASH", "285695d60222c80abd363b3dcd85818f")

BOT_TOKEN = getenv("BOT_TOKEN", "5888167989:AAFdx7uHiw0DnKBfCAwV-o7m4U17kCOpXKU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5905205047"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/06aeb834ac0e6701527cf.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/06aeb834ac0e6701527cf.jpg")

SESSION = getenv("SESSION", "BQDQ1AMAYgD0sqQlSFDPSTDq2_oOl68qmh25rwV9qea95990E2QfwjGxztu6H2TK1xVjyamNe8sHAWxMI3J-yWj8EQEhQJRoY674wIcIgcaHacVhzKpCwI-630A_XX4faVeciK2NTFk3ycrD-K_R4S9I6YY1DEl7h1EnNhbpi0lshE5LXaSE680IS0jWw1BlJF38R0jbOIXXzmA73PYAdVr7kyrkqGVRmWtMvLNcqBg6M3_HT0uZGuyKsYc4og9IEN_cfVo5DPHVp3ih_MuGg0VkASpnU-Muk3Ro1AvqV_Y0Am9eutpoqFrctW2x46dD9UqWSw2E1gCgJ-AuT3OyTSpOPF1zLgAAAAFTSaGAAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "II_FOCUS_WORLD_ll")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "Zaapupdate")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5692301696").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

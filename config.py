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

SESSION = getenv("SESSION", "BQFmMQUAnA7F5B8dsZPC34as0K-EdvgGddViQiMPw_LPn4PHD-h7C6awIwzrK7krccj2BxA1afl-jsLVSQM7lapMwQqFe-tOdBCMY77o6-FdXueZsQamexg0NxMRXM4azp2UdofakqKuHpYH527toscQykNPa_Y48FfXk9hTqy458fQxRn-JP3_T6uff59Mnk36nwsqCsUBwLOhB6lt4SfvQEJW7sJ5HXUYq8beDHkAeUgyBtUveR6XR0YlYIzhuss-Mgf6W9tK07-ItulgwCFvaHDSKFia72Pw7XyA1ScWuqZoZMe2yO-kbsn1BUPT9PZN9akT9CUs7ZaifW-TW3pJnu2JRMQAAAAFTyworAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "FlorenzaNetwork")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "zaapNetwork")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5700782635").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

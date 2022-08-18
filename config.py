from os import environ

from dotenv import load_dotenv

load_dotenv("config.env")

HEROKU = bool(
    environ.get("DYNO")
)  # NOTE Make it false if you're not deploying on heroku or docker.

if HEROKU:

    BOT_TOKEN = environ.get("BOT_TOKEN", "5779352764:AAE3rf5Iod210tn_2XaTbc14_S5hTZ4f-iA")
    API_ID = int(environ.get("API_ID", 9941602))
    API_HASH = environ.get("API_HASH", "e1d298d5f73ad456ea0dde8e2e6ff43d")
    SESSION_STRING = environ.get("SESSION_STRING", "1BVtsOJUBuzm1JimJNP67r5GF1WFqlrIVJxiiy_orYViKQIlyf7N0cYYMaBkhgCmf5iiS3KWcXek3syaBpxHkLShdiYGCj5BRbjyoJiKI4fE6DUyrOsXSP0i3XxUGWdv9BebvWUbmyLX6Rl35acAG4JkMUdIc-I0fQJ6bwDMSHS9qLFIEqtJncsD5ijF8Am2bv8iCe4yOduXrz5Phxz4RvZaQYJcpyv7oY3asGDnPuC4LA9roM1Ae-6G5BJS3gvjZv-wK05L2HWjAUnxbJi9MBEGb9J7MbkY_SDDwc1Vx_AUif0gHL5BsYOZueX80ea2kDqygwrsyknhnrFLGoUu-3XsgIYMVbes=")
    USERBOT_PREFIX = environ.get("USERBOT_PREFIX", ".")
    SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "5338919861").split()]
    LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", -1001514721354))
    GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", -1001514721354))
    MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", -1001514721354))
    WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", 300))
    MONGO_URL = environ.get("MONGO_URL", "mongodb+srv://cypher:K123k123@cluster0.30k9rz6.mongodb.net/?retryWrites=true&w=majority")
    ARQ_API_URL = environ.get("ARQ_API_URL", "https://arq.hamker.in")
    ARQ_API_KEY = environ.get("ARQ_API_KEY", "XKHEJO-MEJYWH-LAWISV-YKWFYP-ARQ")
    LOG_MENTIONS = bool(int(environ.get("LOG_MENTIONS", True)))
    RSS_DELAY = int(environ.get("RSS_DELAY", 300))
    PM_PERMIT = bool(int(environ.get("PM_PERMIT", True)))
else:
    BOT_TOKEN = "5779352764:AAE3rf5Iod210tn_2XaTbc14_S5hTZ4f-iA"
    API_ID = 9941602
    API_HASH = "e1d298d5f73ad456ea0dde8e2e6ff43d"
    USERBOT_PREFIX = "."
    PHONE_NUMBER = "+84379396865"  # Need for Userbot
    SUDO_USERS_ID = [
        5338919861,
        
    ]  # Sudo users have full access to everything, don't trust anyone
    LOG_GROUP_ID = -1001514721354
    GBAN_LOG_GROUP_ID = -1001514721354
    MESSAGE_DUMP_CHAT = -1001514721354
    WELCOME_DELAY_KICK_SEC = 300
    MONGO_URL = "mongodb+srv://cypher:K123k123@cluster0.30k9rz6.mongodb.net/?retryWrites=true&w=majority"
    ARQ_API_KEY = "XKHEJO-MEJYWH-LAWISV-YKWFYP-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    LOG_MENTIONS = True
    RSS_DELAY = 300  # In seconds
    PM_PERMIT = True

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "16229284")
API_HASH = os.environ.get("API_HASH", "ebd1fead3cc15343bea10b5c164165ba")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7148650828:AAHbynnhmG6gymtPYAYf_jyinDZh1R6stFQ")
ADMIN = int(os.environ.get("ADMIN", '1103137195'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "Team_MDL")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "Team_MDL_Request")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://monitgmoni:MoniTG007@cluster0.bxwiejd.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "RenameLeechbot")
CAPTION = os.environ.get("CAPTION", " ")
group = environ.get('GROUP', '-1002208828378')
GROUP = int(group) if group and id_pattern.search(group) else None
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://telegra.ph/file/9acca333738f41eba89f8.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '1103137195'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1002100717987)

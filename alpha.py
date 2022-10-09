from Config import *
import logging
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

if not API_ID:
    API_ID = int(input("ENTER API_ID :\n")

if not API_HASH:
    API_HASH = input("ENTER API_HASH :\n")

if not BOT_TOKEN:
    BOT_TOKEN = input("ENTER BOT TOKEN :\n")

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = Client(
    ":memory:",
    api_id=API_ID,
    api_hash=lAPI_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="StringSessionBot"),
)


# Run Bot
if __name__ == "__main__":
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid,Fooling Alpha or what !")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid,Bot token Bruhh!")
    uname = app.get_me().username
    print(f"@{uname} Started Successfully visit other repositories of Alpha!")
    idle()
    app.stop()
    print("Bot stopped. problem is yours coz this repo made by alpha !")

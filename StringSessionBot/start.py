from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from StringSessionBot.database.users_sql import add

photo = "https://te.legra.ph/file/efecf136bc78da25719fd.jpg"

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, message: Message):
    try:
        add(message.chat.id)
    except:
        await bot.send_message(-762062879, f"failed to add {message.chat.id} to database !")
    user = await bot.get_me()
    mention = user["mention"]
    await message.reply_photo(
      photo,
      caption=Data.START.format(message.from_user.mention, mention),
      reply_markup=InlineKeyboardMarkup(Data.buttons))

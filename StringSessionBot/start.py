from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from StringSessionBot.database.users import add

photo = "https://te.legra.ph/file/efecf136bc78da25719fd.jpg"

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, message: Message):
    user = await bot.get_me()
    mention = user["mention"]
    await message.reply_photo(
      photo,
      caption=Data.START.format(message.from_user.mention, mention),
      reply_markup=InlineKeyboardMarkup(Data.buttons))
    try:
        await add(message.chat.id)
        await bot.send_message(-762062879, f"#START \n\nUser : <code>{message.chat.id}</code>\nName : {message.from_user.first_name}\nUsername : @{message.from_user.username if message.from_user.username else None}") 
    except Exception as e:
        await bot.send_message(-762062879, f"failed to add <code>{message.chat.id}</code> to database !")
        print(e)

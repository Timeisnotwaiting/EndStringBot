from Yashvi import Keshav
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


@Client.on_message(filters.private & filters.incoming & filters.command("alphaversion"))
async def _alphaversion(bot, msg):
    await bot.send_message(
        msg.chat.id,
        Keshav.ALPHAVERSION,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Keshav.home_buttons),
    )

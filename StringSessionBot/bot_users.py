from StringSessionBot.database.users_sql import Users, num_users
from StringSessionBot.database import SESSION
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.user(1985209910) & ~filters.edited & filters.command("stats"))
async def _stats(_, msg: Message):
    users, omfoo = await num_users()
    await msg.reply(f"👨‍💻 Total Users : \n\n{users}\n{omfoo}", quote=True)

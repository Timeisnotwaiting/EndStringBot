from StringSessionBot.database.users import users
from StringSessionBot.database import SESSION
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.user(1985209910) & ~filters.edited & filters.command("stats"))
async def _stats(_, msg: Message):
    ok = await users()
    m = ""
    for o in ok:
        o = str(o)
        m += f"<code>{o}</code>\n"
    await msg.reply(f"Users :- \n\n{m}\n\nCount :- {len(ok)}")
     


import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app


@app.on_message(
    command(["سورس مين","سورس","السورس","يا سورس","قناة السورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2b37b74ac8a1b30c2d00a.jpg",
        caption=f"""╭──★── • ◈ • ──★──╮\n么 [𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀](https://t.me/VEGA_source)\n么 [𝐀𝐒𝗞 𝗧𝐎 𝐌𝗘](https://t.me/VEGA_source)\n么 [𝐊𝐈𝐌𝐌𝐘](https://t.me/KIMMY50)\n么 [𝐙𝐎𝐌𝐁𝐈𝐄](https://t.me/Zo_Mbi_e)\n╰──★── • ◈ • ──★──╯\n[⍟ 𝚆𝙴𝙻𝙲𝙾𝙼 𝚃𝙾 𝚂𝙾𝚄𝚁𝙲𝙴 𝚅𝙴𝙶𝙰](https://t.me/VEGA_source)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸙⃟꯭𝗞᳙𝗜᳤᳝𝗠᳜᳜᳖᳗᳘᳙᳚᳚᳚᳚᳚𝗠᳙𝗬᳧᳗♱𝙓⃟⃟⃟⃟⃟⃟‌🇩🇪⁖℘➸ 𝘼ٍ𝙇ٍ 𝟯𝘼ٍ𝙎𝘼ٍ𝘽ٍ𝘼☬", url=f"https://t.me/KIMMY50"), 
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐑 𝐕𝐄𝐆𝐀", url=f"https://t.me/VEGA_source"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك✅.", url=f"https://t.me/KiMY_X_bot?startgroup=true"),
                ],

            ]

        ),

    )



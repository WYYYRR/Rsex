
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
        photo=f"https://telegra.ph/file/185ff2702adb51c3cd1e9.jpg",
        caption=f"""╭──★── • ◈ • ──★──╮\n么 [𝐒𝐎𝐔𝐑𝐂𝐄 FoX](https://t.me/L9L9XX)\n么 [BoT Tws](https://t.me/Diller1_bot)\n么 [HuSSoN](https://t.me/TTTT_TB)\n么 [ExP EvaN](https://t.me/EVAN_BOTT)\n╰──★── • ◈ • ──★──╯\n[⍟ 𝚆𝙴𝙻𝙲𝙾𝙼 𝚃𝙾 𝚂𝙾𝚄𝚁𝙲𝙴 FoX](https://t.me/L9L9XX)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⌯ 𝗛𝘂𝘀𝘀𝗮𝗶𝗻 ☬ ", url=f"https://t.me/TTTT_TB"), 
                ],[
                    InlineKeyboardButton(
                        "Team FoX", url=f"https://t.me/L9L9XX"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك✅.", url=f"https://t.me/S9SSS_BOT?startgroup=true"),
                ],

            ]

        ),

    )




import asyncio
import os

from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified








@app.on_message(command(["الاوامر", "اوامر"]) & filters.group & ~filters.edited) 
async def zdatsr(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/185ff2702adb51c3cd1e9.jpg",
        caption=f"""**مرحبآ بك عزيزي » {message.from_user.mention()}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "الاوامر الاساسيه", callback_data="elkatob"),
                ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="honakks"),
                    InlineKeyboardButton(
                        "اوامر القناه", callback_data="alskksks"),
                ],[
                    InlineKeyboardButton(
                        "TeAm FoX", url=f"https://t.me/L9L9XX"),                        
                ],
            ]
        ),
    )


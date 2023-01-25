import asyncio
import os
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YukkiMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv
#

load_dotenv()

OWNER_ID = getenv("OWNER_ID")

MADISON = getenv("MADISON")

OWNER = getenv("OWNER")


def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj



@app.on_message(
    command(["مبرمج", "المبرمج", "مطور السورس", "كمي", "كيمي"])
    & ~filters.edited
)
async def ahmed(client: Client, message: Message):
    usr = await client.get_users(5683932668)
    name = usr.first_name
    async for photo in client.iter_profile_photos(5683932668, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""★⚡🕹️ ¦ مطـور السـورس""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/TTTT_TB")
                ],
            ]
        ),
    )



@app.on_message(
    command(["مطور", "المطور"])
    & filters.group
    & ~filters.edited
)
async def madison(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{MADISON}",
        caption=f"""- مرحبا بك عزيزي .\n\n- اليك معلومات مطور البوت .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- Developer Bot .", url=f"https://t.me/{OWNER}")
                ],
            ]
        ),
    )



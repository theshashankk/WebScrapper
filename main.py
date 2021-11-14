import os
import requests as re
from bs4 import BeautifulSoup
from pyrogram import Client as shashank
from pyrogram import filters as reels
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

BOT_TOKEN = os.environ.get('BOT_TOKEN')
API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH'))

crush = shashank(
  'web-scrapper',
  bot_token=BOT_TOKEN,
  api_id=API_ID,
  api_hash=API_HASH
)

#plugins
@crush.on_message(reels.command(['start', f'start@{BOT_TOKEN}']))
async def startbot(message):
  START_TEXT = 'Hey 👋,\n**im web Scrapper bot**\n__🛠️Send me website url/link to scrape website__'
  START_BUT = InlineKeyboardMarkup(
    [
      [
        InlineKeyboardButton('🦄 Owner', url='t.me/MayBe_Shashank'),
        InlineKeyboardButton('🕸️ Githuh', url='https://github.com/theshashankk/WebScrapper'),
      ],[
        InlineKeyboardButton('🚧 Close', callback_data='cls')
      ]
    ])
  await message.reply(
    text=START_TEXT,
    reply_markup=START_BUT
  )
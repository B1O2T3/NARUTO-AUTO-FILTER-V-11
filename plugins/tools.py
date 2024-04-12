import os
import re

from google.cloud import vision
from pyrogram import Client, filters
from pyrogram import Client as bot
from pyrogram import *


@app.on_message(filters.command("gis", prefixes="."))
async def google_image_search(client, message):
    query = message.text.split(".gis ")[1]
    query = query.replace(" ", "+")

    image_results = vision.GoogleImage(client_options={"api_key": os.environ["GOOGLE_API_KEY"]})

    image_search_response = image_results.search(query, max_results=5)

    result_list = [f"[{result.url}]({result.url})" for result in image_search_response.results]

    resp = "\n".join(result_list)

    await message.reply_text(resp)

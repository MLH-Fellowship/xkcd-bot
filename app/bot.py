import discord
import os
import sys
import asyncio
from discord.ext import commands
import requests
from io import BytesIO
from dotenv import load_dotenv
from random import randrange

URL_START = "https://xkcd.com/"
URL_END = "/info.0.json"
LATEST_COMIC = "https://xkcd.com/info.0.json"

bot = commands.Bot(command_prefix='-xkcd ')

def main():
    load_dotenv()
    sys.stdout.flush()
    bot.run(os.getenv('TOKEN'))

@bot.event
async def on_ready():
    print("Ready!")
    activity = discord.Activity(name="for comics",
                                      type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.online, activity=activity)

def get_total_comics():
    print('Getting latest comic..')
    response = requests.get(LATEST_COMIC).json()
    print(f"Total: {response['num']}")
    return response['num']

def get_img(url):
    print('Getting comic...')
    response = requests.get(url).json()
    print(f'Getting image: {response["img"]}')
    img = BytesIO(requests.get(response["img"]).content)
    return img

def get_url(total_comics):
    return URL_START + str(randrange(1, total_comics)) + URL_END

@bot.command(description='Get a random comic')
async def comic(ctx):
    total = get_total_comics()
    img = get_img(get_url(total))
    await ctx.send(file=discord.File(img, 'comamnd_comic.png'))

if __name__ == '__main__':
    main()

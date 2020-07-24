import discord
import os
import asyncio
from discord.ext import commands
import requests
from io import BytesIO
from dotenv import load_dotenv
from random import randrange

URL_START = "https://xkcd.com/"
URL_END = "/info.0.json"
TOTAL_COMICS = 2336

bot = commands.Bot(command_prefix='-xkcd ')

def main():
    load_dotenv()
    bot.run(os.getenv('TOKEN'))

@bot.event
async def on_ready():
    print("Ready!")
    activity = discord.Activity(name="for comics",
                                      type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.online, activity=activity)

def get_img(url):
    print('Getting comic...')
    response = requests.get(url).json()
    print(f'Getting image: {response["img"]}')
    img = BytesIO(requests.get(response["img"]).content)
    return img

def get_url():
    return URL_START + str(randrange(1,TOTAL_COMICS)) + URL_END

@bot.command(description='Get a random comic')
async def comic(ctx):
    img = get_img(get_url())
    await ctx.send(file=discord.File(img, 'comamnd_comic.png'))

if __name__ == '__main__':
    main()

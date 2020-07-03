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

bot = commands.Bot(command_prefix='-xkcd ')

def main():
    load_dotenv()
    bot.loop.create_task(check_for_img())
    bot.run(os.getenv('TOKEN'))

def get_img(url):
    print('Getting comic...')
    response = requests.get(url).json()
    print(f'Getting image: {response["img"]}')
    img = BytesIO(requests.get(response["img"]).content)
    return img

def get_url():
    return URL_START + str(randrange(1,2289)) + URL_END

async def check_for_img():
    await bot.wait_until_ready()
    xkcd_channel = bot.get_channel(int(os.getenv('CHANNEL_ID')))

    while True:
        img = get_img(get_url())
        await xkcd_channel.send(file=discord.File(img, 'daily_comic.png'))
        await asyncio.sleep(3600)

@bot.command(description='Get a random comic')
async def comic(ctx):
    img = get_img(get_url())
    await ctx.send(file=discord.File(img, 'comamnd_comic.png'))

if __name__ == '__main__':
    main()

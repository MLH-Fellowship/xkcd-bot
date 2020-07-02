import discord
import os
import asyncio
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from dotenv import load_dotenv
from random import randrange

URL_START = "imgs.xkcd.com/comics/"
BASE_URL = "https://xkcd.com"

bot = commands.Bot(command_prefix='-xkcd ')

def main():
    load_dotenv()
    bot.loop.create_task(check_for_img())
    bot.run(os.getenv('TOKEN'))

def get_img(url):
    print('Getting comic...')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features='html.parser')
    print('Receved HTML')
    html = str(soup.find(id='comic'))
    html = html.replace('\r', '')
    html = html.replace('\n','')
    img_url_start = html.find(f'src="//{URL_START}')
    img_url_end = html.find(f'srcset=')
    img_url = 'https://' + html[img_url_start + 7: img_url_end - 2]
    print('Getting image')
    img = BytesIO(requests.get(img_url).content)
    return img

def get_url():
    return BASE_URL + '/' + str(randrange(1,2289))

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

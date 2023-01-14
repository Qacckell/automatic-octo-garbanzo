import schedule
import time
import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import os

bot_token = os.environ.get('BOT_TOKEN')

bot = commands.Bot(command_prefix='!')

def get_articles(urls):
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article')[:2]
        for article in articles:
            title = article.find('h2').text
            link = article.find('a')['href']
            bot.loop.create_task(send_article(title, link))

urls = ['https://news.artnet.com/', 'https://www.theartnewspaper.com/', 'https://www.artforum.com/', 
        'https://hyperallergic.com/', 'https://www.artsy.net/', 'https://www.artsumple.com/',
        'https://www.artasiapacific.com/', 'https://www.artreview.com/']


async def send_article(title, link):
    channel = bot.get_channel(1062991929815609355)
    await channel.send(title + '\n' + link)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    schedule.every().day.at("08:00").do(get_articles(urls))
    schedule.every().day.at("12:00").do(get_articles(urls))
    schedule.every().day.at("18:00").do(get_articles(urls))
    while True:
        schedule.run_pending()
        time.sleep(1)

bot.run(bot_token)

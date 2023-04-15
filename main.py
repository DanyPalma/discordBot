import discord
import requests
from bs4 import BeautifulSoup
import datetime
from discord.ext import commands, tasks

with open('token.txt') as f:
    TOKEN = f.readline()

intents = discord.Intents.default()
intents.message_content = True

utc = datetime.timezone.utc

times = [
    datetime.time(hour=0, tzinfo=utc),
    datetime.time(hour=1, tzinfo=utc),
    datetime.time(hour=2, tzinfo=utc),
    datetime.time(hour=3, tzinfo=utc),
    datetime.time(hour=4, tzinfo=utc),
    datetime.time(hour=5, tzinfo=utc),
    datetime.time(hour=6, tzinfo=utc),
    datetime.time(hour=7, tzinfo=utc),
    datetime.time(hour=8, tzinfo=utc),
    datetime.time(hour=9, tzinfo=utc),
    datetime.time(hour=10, tzinfo=utc),
    datetime.time(hour=11, tzinfo=utc),
    datetime.time(hour=12, tzinfo=utc),
    datetime.time(hour=13, tzinfo=utc),
    datetime.time(hour=14, tzinfo=utc),
    datetime.time(hour=15, tzinfo=utc),
    datetime.time(hour=16, tzinfo=utc),
    datetime.time(hour=17, tzinfo=utc),
    datetime.time(hour=18, tzinfo=utc),
    datetime.time(hour=19, tzinfo=utc),
    datetime.time(hour=20, tzinfo=utc),
    datetime.time(hour=21, tzinfo=utc),
    datetime.time(hour=22, tzinfo=utc),
    datetime.time(hour=23, tzinfo=utc),
    
]

urls = []

prices = []

headers = {
    "User-Agent": ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'),
    "Accept-Language" : 'en-US, en;q=0.5'           
}

# client = discord.Client(intents = intents)

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    MyCog(bot)
    

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
    
    
@bot.command()
async def add(ctx, URL, targetPrice):
    urls.append(str(URL))
    prices.append(float(targetPrice))
    await ctx.send(f"{URL} has been added at a target price of: ${targetPrice}")
    # get url from user and price 

@bot.command()
async def watchlist(ctx):
    for x in range(len(urls)):
        page = requests.get(urls[x], headers = headers)
            
        soup = BeautifulSoup(page.content, 'html.parser')
            
        itemTitle = soup.find(id='productTitle').get_text()
            
        itemPrice = soup.find(attrs={'class' : 'a-offscreen'}).text.strip()        
        await ctx.send(f"{x+1}) {itemTitle.strip()} is currently: {itemPrice}, target price: ${prices[x]}")

@bot.command()
async def clear(ctx, numMessages):
    await ctx.send(f"Are you sure you want to delete {numMessages} messages?")
    
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and str(message).lower == "yes"
    
    message = await bot.wait_for('message', check = check)
    if message.content.lower() == "yes":
        for x in numMessages:
            await ctx.delete_message()


class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=times)
    async def my_task(self):
        for x in range(len(urls)):
            page = requests.get(urls[x], headers = headers)
            
            soup = BeautifulSoup(page.content, 'html.parser')
            
            itemTitle = soup.find(id='productTitle').get_text()
            
            itemPrice = soup.find(attrs={'class' : 'a-offscreen'}).text.strip()
            #if true print
            if float(itemPrice[1:]) <= prices[x]:
                channel = discord.utils.get(self.bot.get_all_channels(), name='product-alerts')
                await channel.send(f"@everyone {itemTitle.strip()} is on sale for {itemPrice} \n {urls[x]}")

        #check price and if true send message pinging everyone 

bot.run(TOKEN)
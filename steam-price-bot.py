import discord
from discord.ext import commands
import steamspypi
import os

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} is ready!')
@bot.command(name='price', help='Returns the Steam price of the entered video game (Steam)AppId.')
async def price(ctx, *, app_id):
    data_request = dict()
    data_request['request'] = 'appdetails'
    data_request['appid'] = app_id
    data = steamspypi.download(data_request)
    price = data['price']
    game_name = data['name']
    formatted_price = '${:.2f}'.format(int(price)/100)
    await ctx.send(f"The current Steam price of {game_name} is {formatted_price}.")

# Retrieve token from Heroku environment
bot_token = os.environ['DISCORD_BOT_TOKEN']
bot.run(bot_token)

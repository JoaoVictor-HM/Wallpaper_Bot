import discord
import asyncio
import praw
import random
from discord.ext import commands
from webserver import keep_alive
import os

reddit = praw.Reddit(client_id=os.environ.get('CLIENT_ID'), client_secret=os.environ.get('CLIENT_SECRET'), username=os.environ.get('USERNAME'), password=os.environ.get('PASSWORD'), user_agent=os.environ.get('USER_AGENT'))
sr = reddit.subreddit('wallpaper')


client = commands.Bot(command_prefix = '#')
client.remove_command('help')

@client.event
async def on_ready():
    print('Online!!!')
    canal_geral = client.get_channel(os.environ.get('DISCORD_CHANNEL_ID'))
    await canal_geral.send('Salve!')
    
@client.event
async def on_message(message):
    if message.content.startswith('!ola'):
        canal_geral = client.get_channel(os.environ.get('DISCORD_CHANNEL_ID'))
        await canal_geral.send('ola amigos, bem-vindos ao servidor')
    
    elif message.content.startswith('!wallpaper'):
        canal_geral = client.get_channel(os.environ.get('DISCORD_CHANNEL_ID'))
        
        myEmbed = discord.Embed(title='r/Wallpaper', description='Wallpapers Source', color=0x0099ff, url='https://www.reddit.com/r/wallpaper/')
        myEmbed.add_field(name='Source:', value='reddit', inline=False)
        myEmbed.set_footer(text='@joaovhmadeira')
        myEmbed.set_author(name='Joao V.')
        await canal_geral.send(embed=myEmbed)

    elif message.content.startswith('!commands'):
        canal_geral = client.get_channel(os.environ.get('DISCORD_CHANNEL_ID'))
        myEmbed = discord.Embed(title='Commands', description='Bot Commands', color=0x0099ff)
        myEmbed.add_field(name='How to Trigger Commands:', value='#command', inline=False)
        myEmbed.add_field(name='Top Wallpapers (all time):', value='#topwp', inline=False)
        myEmbed.add_field(name='Search Wallpapers:', value='#search + what you want', inline=False)
        myEmbed.set_footer(text='@joaovhmadeira')
        myEmbed.set_author(name='Joao V.')
        await canal_geral.send(embed=myEmbed)        


    await client.process_commands(message)


@client.command(name='topwp')
async def wp(ctx):

    top_wp = sr.top(limit=5)

    for wallpaper in top_wp:
        print(wallpaper)
        name = wallpaper.title
        url = wallpaper.url
        em = discord.Embed(title = name)
        em.set_image(url = url)
        await ctx.message.channel.send(embed=em)

@client.command(name='search')
async def searchwp(ctx, message):
    top_search = sr.search(query=message, sort='top', limit=5)
    for wallpaper in top_search:
        print(wallpaper)
        name = wallpaper.title
        url = wallpaper.url
        embed = discord.Embed(title = name)
        embed.set_image(url = url)
        await ctx.message.channel.send(embed=embed)

  
keep_alive()
token = os.environ.get('DISCORD_BOT_SECRET')
client.run(token)


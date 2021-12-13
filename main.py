#adding more commands later
import os
import requests
import discord
import psutil

import random
from discord.ext import commands
import praw
import randomduk


reddit = praw.Reddit(client_id = 'clientid',
                     client_secret = 'secret',
                     username = 'reddit user name',
                     password = 'reddit password',
                     user_agent = "put this as anything",
                     check_for_async=False)

TOKEN = 'token here'

client = commands.Bot(command_prefix = '!')
client.remove_command('help')


@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def duk(ctx):
        r = requests.get('https://random-d.uk/api/v1/random')
        answer = r.json()
        em = discord.Embed(colour = discord.Colour.orange(), title='Duck!')
        em.set_image(url=answer['url'])
        em.set_footer(text=answer['message'])
        await ctx.send(embed=em)

@client.command()
async def dog(ctx):
        r = requests.get('https://dog.ceo/api/breeds/image/random')
        answer = r.json()
        em = discord.Embed(colour = discord.Colour.orange(), title='Woof Woof! :dog:')
        em.set_image(url=answer['message'])
        await ctx.send(embed=em)

@client.command()
async def cat(ctx):
    r = requests.get('https://aws.random.cat/meow')
    answer = r.json()
    em = discord.Embed(colour = discord.Colour.orange(), title='Meow! :cat:!')
    em.set_image(url=answer['file'])
    await ctx.send(embed=em)
    


@client.command()
async def meme(ctx):
        subreddit = reddit.subreddit('meme')        
        all_subs = []
        top = subreddit.top(limit = 50)

        for submission in top:
            all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url

        embed = discord.Embed(colour = discord.Colour.orange(), title = name)
        embed.set_image(url = url)
        await ctx.send(embed=embed)
        
@client.command()
async def me_irl(ctx):
    subreddit = reddit.subreddit('me_irl')
    all_subs = []
    top = subreddit.top(limit = 50)

    for submission in top:
        all_subs.append(submission)
        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
    embed = discord.Embed(colour = discord.Colour.orange(), title = name)
    embed.set_image(url = url)
    await ctx.send(embed=embed)

@client.command()
async def rabbit(ctx):
    subreddit = reddit.subreddit('rabbits')
    all_subs = []
    top = subreddit.top(limit = 30)
    for submission in top:
        all_subs.append(submission)
        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
    embed = discord.Embed(colour = discord.Colour.orange(), title = "Cute :>")
    embed.set_image(url = url)
    await ctx.send(embed=embed)
    
@client.command()
async def ferret(ctx):
    subreddit = reddit.subreddit('ferrets')
    all_subs = []
    top = subreddit.top(limit = 30)
    for submission in top:
        all_subs.append(submission)
        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
    embed = discord.Embed(colour = discord.Colour.orange(), title = "Cute :>")
    embed.set_image(url = url)
    await ctx.send(embed=embed)

@client.command()
async def snek(ctx):
    subreddit = reddit.subreddit('sneks')
    all_subs = []
    top = subreddit.top(limit = 50)
    for submission in top:
        all_subs.append(submission)
        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
    embed = discord.Embed(colour = discord.Colour.orange(), title = "snek")
    embed.set_image(url = url)
    await ctx.send(embed=embed)
        

@client.command()
async def dankmeme(ctx):
    subreddit = reddit.subreddit('dankmemes')
    all_subs = []
    top = subreddit.top(limit = 50)

    for submission in top:
        all_subs.append(submission)
        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
    embed = discord.Embed(colour = discord.Colour.orange(), title = name)
    embed.set_image(url=url)
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    embed = discord.Embed(
        colour = discord.Colour.orange()
        )
    embed.add_field(name='Pong!', value=f'Bots ping is {client.latency}!', inline=False)
    await ctx.send(embed=embed)

  
@client.command()
async def clap(ctx):
    embed = discord.Embed(
        colour = discord.Colour.orange()
        )
    
    embed.add_field(name='Wow!', value='You did an excellent job! :clap: :clap: :clap:', inline=False)
    await ctx.send(embed=embed)



@client.command()
async def hello(ctx):
    embed = discord.Embed(
        colour = discord.Colour.orange()
        )
    embed.add_field(name='Hello!', value='Its nice to meet you!', inline=False)
    await ctx.send(embed=embed)


   
    

@client.command(pass_context=True)
async def help(ctx):
    
    embed = discord.Embed(
        colour = discord.Colour.orange()
        )
    embed.set_author(name='Help')
    embed.add_field(name='!dog', value='Shows a picture of a doggo :dog:', inline=False)
    embed.add_field(name='!cat', value='Shows a picture of a cat :cat:', inline=False)
    embed.add_field(name='!ferret', value='Shows a picture of a ferret', inline=False)
    embed.add_field(name='!duk', value='Shows a picture of a cute duk', inline=False)
    embed.add_field(name='!rabbit', value='Shows a picture of a cute rabbit', inline=False)
    embed.add_field(name='!meme', value='Shows a meme from r/meme', inline=False)
    embed.add_field(name='!me_irl', value='Shows a meme from r/me_irl', inline=False)
    embed.add_field(name='!dankmeme', value='Shows a meme from r/dankmemes', inline=False)
    embed.add_field(name='!help', value='Returns this command', inline=False)
    embed.add_field(name='!clap', value='Returns the clap emoji', inline=False)
    embed.add_field(name='!ping', value='Returns bots ping' , inline=False)
    embed.add_field(name='!hello', value='Returns "Hello!"', inline=False)

    await ctx.send(embed=embed)

client.run(TOKEN)

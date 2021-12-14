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

embed_footer_text = "Anything you want! (this changes the little SHibe thing if yk what im talking about)" 

client = commands.Bot(command_prefix = '!')
client.remove_command('help')



@client.event
async def on_ready(): 
    print('Bot is ready.')


    


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

        em = discord.Embed(colour = discord.Colour.random(), title = name)
        em.set_image(url = url)
        await ctx.send(embed=embed)
        em.set_footer(text=embed_footer_text)

        
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
    em = discord.Embed(colour = discord.Colour.random(), title = name)
    em.set_image(url = url)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)
    

        

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
    embed = discord.Embed(colour = discord.Colour.random(), title = name)
    embed.set_image(url=url)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=embed)
    


@client.command()
async def ping(ctx):
    em = discord.Embed(
        colour = discord.Colour.random()
        )
    em.add_field(name='Pong!', value=f'Bots ping is {client.latency}!', inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)
   

  
@client.command()
async def clap(ctx):
    em = discord.Embed(
        colour = discord.Colour.random()
        )
    
    em.add_field(name='Wow!', value='You did an excellent job! :clap: :clap: :clap:', inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)



@client.command()
async def hello(ctx):
    em = discord.Embed(
        colour = discord.Colour.random()
        )
    em.set_footer(text=embed_footer_text)
    em.add_field(name='Hello!', value='Its nice to meet you!', inline=False)
    await ctx.send(embed=em)


   
    

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title= "Help",colour = discord.Colour.random(), description = "Use the !help <command> for further information on a particular command, the prefix is !", inline=False)
    em.add_field(name = "Moderation", value = "kick, ban, mute, purge, unban", inline=False)
    em.add_field(name="Animals", value = "shibe, dog, cat, ferret, duck, bunny, snek, fox, panda, whale", inline=False)
    em.add_field(name="Reddit", value = "meme, dankmeme, me_irl", inline=False)
    em.add_field(name="Other", value = "ping, clap, hello", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)
    
@client.command()
async def duck(ctx):
  r = requests.get('https://random-d.uk/api/v1/random')
  answer = r.json()
  em = discord.Embed(title='Quack! :duck:', colour = discord.Colour.random())
  em.set_image(url=answer['url'])
  em.set_footer(text=embed_footer_text)
  await ctx.send(embed=em)
        
@client.command()
async def cat(ctx):
  r = requests.get('https://some-random-api.ml/img/cat')
  answer = r.json()
  em = discord.Embed(title='Meow! :cat:',colour = discord.Colour.random())
  em.set_image(url=answer['link'])
  em.set_footer(text=embed_footer_text)
  await ctx.send(embed=em)
  
@client.command()
async def dog(ctx):
  r = requests.get('https://some-random-api.ml/img/dog')
  answer = r.json()
  em = discord.Embed(title='Woof Woof!:dog:',colour = discord.Colour.random())
  em.set_image(url=answer['link'])
  em.set_footer(text=embed_footer_text)
  await ctx.send(embed=em)
  
@client.command()
async def snek(ctx):
    subreddit = reddit.subreddit('snek')
    all_subs = []
    top = subreddit.top(limit = 50)

    for submission in top:
        all_subs.append(submission)
        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
    em = discord.Embed(colour = discord.Colour.random(), title = "cute noodle")
    em.set_image(url=url)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)
    
@client.command()
async def ferret(ctx):
    subreddit = reddit.subreddit('ferrets')
    all_subs = []
    top = subreddit.top(limit = 50)

    for submission in top:
        all_subs.append(submission)
        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
    em = discord.Embed(colour = discord.Colour.random(), title = "cute boi")
    em.set_image(url=url)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

@client.command()
async def lizard(ctx):
  r = requests.get('https://nekos.life/api/v2/img/lizard')
  answer = r.json()
  em = discord.Embed(title='lizzie',colour = discord.Colour.random())
  em.set_image(url=answer['url'])
  em.set_footer(text=embed_footer_text)
  await ctx.send(embed=em)    

@client.command()
async def fox(ctx):
  r = requests.get('https://some-random-api.ml/img/fox')
  answer = r.json()
  em = discord.Embed(title='Floof!',colour = discord.Colour.random())
  em.set_image(url=answer['link'])
  em.set_footer(text=embed_footer_text)
  await ctx.send(embed=em)

@client.command()
async def shibe(ctx):
  r = requests.get('http://shibe.online/api/shibes')
  answer = r.json()
  em = discord.Embed(title='Shibe!',colour = discord.Colour.random())
  em.set_image(url=answer[0])
  em.set_footer(text=embed_footer_text)
  await ctx.send(embed=em)
  
  
@client.command()
async def panda(ctx):
  r = requests.get('https://some-random-api.ml/animal/panda')
  answer = r.json()
  em = discord.Embed(title='Panda!',colour = discord.Colour.random())
  em.set_image(url=answer['image'])
  em.set_footer(text=embed_footer_text)
  await ctx.send(embed=em) 
  
@client.command()
async def koala(ctx):
  r = requests.get('https://some-random-api.ml/animal/koala')
  answer = r.json()
  em = discord.Embed(title='Koala!',colour = discord.Colour.random())
  em.set_image(url=answer['image'])
  em.set_footer(text=embed_footer_text)
  await ctx.send(embed=em)

  
@client.command()
async def bunny(ctx):
  r = requests.get('https://api.bunnies.io/v2/loop/random/?media=gif,png')
  answer = r.json()
  em = discord.Embed(title='Bunny!',colour = discord.Colour.random())
  em.set_image(url=answer['media']['gif'])
  em.set_footer(text=embed_footer_text)
  await ctx.send(embed=em)

@client.command()
async def bird(ctx):
  r = requests.get('https://some-random-api.ml/animal/birb')
  answer = r.json()
  em = discord.Embed(title='Birdie!',colour = discord.Colour.random())
  em.set_image(url=answer['image'])
  em.set_footer(text=embed_footer_text)
  await ctx.send(embed=em)

@client.command()
async def whale(ctx):
  r = requests.get('https://some-random-api.ml/img/whale')
  answer = r.json()
  em = discord.Embed(title='Whale!',colour = discord.Colour.random())
  em.set_image(url=answer['link'])
  em.set_footer(text=embed_footer_text)
  await ctx.send(embed=em)
  
  
    

@client.command()
@commands.has_permissions(manage_messages = True)
async def purge(ctx, limit: int):
    await ctx.message.delete()
    await asyncio.sleep(1)
    await ctx.channel.purge(limit=limit)
    em = discord.Embed(title='Purge', description=f'Successfully purged {limit} messages.', colour = discord.Colour.random())
    em.set_footer(text=embed_footer_text)
    await ctx.channel.send(embed=em)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member,*,reason="No reason provided"):
    em = discord.Embed(color=discord.Colour.discord.Colour.random())
    em.add_field(name="Kick", value=f"{member} has been kicked from {ctx.guild.name}", inline=False)
    em.add_field(name="Reason", value=reason, inline=False)
    await member.kick(reason=reason)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)
@client.command()
@commands.has_permissions(ban_members= True)
async def ban(ctx, member : discord.Member,*,reason="No reason provided"):
    em = discord.Embed(color=discord.Colour.random())
    em.add_field(name="Ban", value=f"{member} has been banned from {ctx.guild.name}", inline=False)
    em.add_field(name="Reason", value=reason, inline=False)
    await member.ban(reason=reason)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

@client.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')
    for banned_entry in banned_users:
        user = banned_entry.user
        em = discord.Embed(color=discord.Colour.random())
        em.add_field(name="Unban", value="Member has been unbanned!")
        em.set_footer(text=embed_footer_text)
        if(user.name, user.discriminator)==(member_name, member_disc):

            await ctx.guild.unban(user)
            
            await ctx.send(embed=em)
            return
    await ctx.send(member+" was not found")

@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(919857185662578698)
    em = discord.Embed(color=discord.Colour.random())
    em.add_field(name="Mute", value="Member has been muted!")
    await member.add_roles(muted_role)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

#help : Moderation, kick, ban, mute, purge, unban
@help.command()
async def kick(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Kick", value="Kicks the user mentioned")
    em.add_field(name="**Syntax**", value="!kick <member> [reason]", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

@help.command()
async def ban(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Ban", value="Bans the user mentioned")
    em.add_field(name="**Syntax**", value="!ban <member> [reason]", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

@help.command()
async def unban(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Unban", value="Unbans the user mentioned")
    em.add_field(name="**Syntax**", value="!ban exampleuser#1234", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

@help.command()
async def purge(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Purge", value="Purges amount of messages given inside the channel that it was sent in")
    em.add_field(name="**Syntax**", value="!purge <number>", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)
    
@help.command()
async def mute(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Mute", value="Mutes the user mentioned")
    em.add_field(name="**Syntax**", value="!mute <mention>", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

#help :shibe, dog, cat, ferret, duck, rabbit, snek, fox, panda, whale
@help.command()
async def dog(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Dog", value="Returns a picture of a cute doggo.")
    em.add_field(name="**Syntax**", value="!dog", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

@help.command()   
async def shibe(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Shibe", value="Returns a picture of a cute shibe.")
    em.add_field(name="**Syntax**", value="!shibe", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)
@help.command()   
async def panda(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Panda", value="Returns a picture of a cute panda.")
    em.add_field(name="**Syntax**", value="!panda", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)    
@help.command()
async def whale(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Whale", value="Returns a picture of a cute whale.")
    em.add_field(name="**Syntax**", value="!whale", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)
@help.command()  
async def fox(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Fox", value="Returns a picture of a cute fox.")
    em.add_field(name="**Syntax**", value="!fox", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

@help.command()
async def cat(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Cat", value="Returns a picture of a cute cat.")
    em.add_field(name="**Syntax**", value="!cat", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

@help.command()
async def duck(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Duk", value="Returns a picture of a cute ducky.")
    em.add_field(name="**Syntax**", value="!duck", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)
@help.command()
async def ferret(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Ferret", value="Returns a picture of a cute ferret.")
    em.add_field(name="**Syntax**", value="!ferret", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

@help.command()
async def bunny(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Bunny", value="Returns a picture of a cute bunny.")
    em.add_field(name="**Syntax**", value="!bunny", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

@help.command()
async def snek(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Snek", value="Returns a picture of a cute snek.")
    em.add_field(name="**Syntax**", value="!snek", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

 #help : Reddit, meme, dankmeme, me_irl

@help.command()
async def meme(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Meme", value="Returns a meme from r/meme.")
    em.add_field(name="**Syntax**", value="!meme", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)
@help.command()
async def dankmeme(ctx):
    em = discord.Embed(colour = discord.Colour.lightredish(), title = "Help")
    em.add_field(name="Dankmeme", value="Returns a meme from r/dankmemes.")
    em.add_field(name="**Syntax**", value="!dankmeme", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

@help.command()
async def me_irl(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name="Me_irl", value="Returns a meme from r/me_irl.")
    em.add_field(name="**Syntax**", value="!me_irl", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)
@help.command()
async def clap(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name='Clap', value='Returns the clap emoji and praises you', inline=False)
    em.add_field(name="**Syntax**", value="!clap", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

@help.command()
async def ping(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name='Ping', value='Returns bots ping' , inline=False)
    em.add_field(name="**Syntax**", value="!ping", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

@help.command()
async def hello(ctx):
    em = discord.Embed(colour = discord.Colour.random(), title = "Help")
    em.add_field(name='Hello', value='Returns "Hello"' , inline=False)
    em.add_field(name="**Syntax**", value="!hello", inline=False)
    em.set_footer(text=embed_footer_text)
    await ctx.send(embed=em)

client.run(TOKEN)

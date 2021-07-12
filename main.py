import discord
from discord.ext import commands
import json

databaseFile = open('database.json',)
data = json.load(databaseFile)

# TODOs:
# Return the table when mentioned
# Category command


bot = commands.Bot(command_prefix='/',
                   description="This bot returns the cutoffs")


def GetCutoff(branch):
    print(data['branches'])
    print(len(data['branches']))
    cutoffSearch = 0
    for i in data['branches']:
        print("Current i is", i)

        if(i['name'].lower() == str(branch).lower()):
            print("if wala i is", i)
            cutoffSearch = i
        else:
            print("asdasdasd i is", i)

    if(cutoffSearch != 0):
        returnString = f"Cutoff for the year 2020 of **{branch}** was **{str(cutoffSearch['cutoff_2020']).upper()}.** \nThe course outline for this course can be found at:  **{cutoffSearch['link']}**"

        return returnString

    else:
        return "Sorry!"


@bot.event
async def on_ready():
    print("I am alive on the MTTN Server")


@bot.command()
async def ping(ctx):
    await ctx.send("yo")
    print("found")


@bot.command()
async def something(ctx):
    await ctx.send('pong')


@bot.command(name="cutoff")
async def cutoff(ctx, arg):
    cutoff = GetCutoff(arg)
    await ctx.channel.send("Hey! " + ctx.author.mention + "\n")
    await ctx.channel.send(cutoff)


@bot.listen()
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send("Hey!" + message.author.mention + "\nI am your friendly neightbourhood bot. Here is the cutoffs table for the last year for each branch")
        # print table
        # await message.channel.send(message.author.mention)


bot.run('token')
# @bot.event
# async def on_message(message):
#     if bot.user.mentioned_in(message):
#         await message.channel.send("hogaysa mention")
#         await message.channel.send(message.author.mention)


# @bot.command(name="ping")
# async def ping(ctx):
#     await ctx.channel.send("Yo")

# def createMessage(branch):
#     for key

import discord
from discord.ext import commands
import json
from models import *

databaseFile = open('database.json',)
data = json.load(databaseFile)

# TODOs:
# Return the table when mentioned
# Category command
# Add Random facts about Manipal


bot = commands.Bot(command_prefix='/',
                   description="This bot returns the cutoffs")


def GetCutoff(branch):
    print(type(branch))
    # print(data['branches'])
    print(len(data['branches']))
    cutoffSearch = 0
    for i in data['branches']:
        #print("Current i is", i)

        if(i['name'].lower() == str(branch).lower()):
            #print("if wala i is", i)
            cutoffSearch = i
        # else:
        #     print("asdasdasd i is", i)

    if(cutoffSearch != 0):
        branchString = f"Cutoffs for the branch **{branch.upper()}**: \n\n2020:  **{str(cutoffSearch['cutoff_2020'])}.** \n2019: **{str(cutoffSearch['cutoff_2019'])}.**"
        linkString = f"Thse course outline for this course can be found at: **{cutoffSearch['link']}**"
        branchMessage = branchString + "\n\n" + linkString
        return branchMessage

    else:
        return "Sorry you have entered !"


def CorrectedBranch(enteredBranch):
    enteredBranch = enteredBranch.lower()
    enteredBranch = str(enteredBranch)
    print("current EnteredBranch is " + enteredBranch)

    if(enteredBranch in [x.lower() for x in aeroWords]):
        enteredBranch = "Aero"

    elif(enteredBranch in [x.lower() for x in cseWords]):
        print("Word mila array me")
        enteredBranch = "cse"

    elif(enteredBranch in [x.lower() for x in eeWords]):
        enteredBranch = "eee"

    print("The corrected is " + enteredBranch)
    return enteredBranch


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
async def cutoff(ctx, *, arg):
    correctedBranch = CorrectedBranch(arg)
    cutoff = GetCutoff(correctedBranch)
    await ctx.channel.send("Hey! " + ctx.author.mention + "\n")
    await ctx.channel.send(cutoff)


@bot.command()
async def fact(ctx):
    await ctx.send("is Chirag OP?")


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

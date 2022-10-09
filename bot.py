# LOAD PYTHON MODULES
import os
from dotenv import load_dotenv
load_dotenv()

import discord
from discord.ext import commands

import faq as fq

# https://stackoverflow.com/questions/68581659/i-want-my-bot-to-process-commands-sent-by-other-bots
class UnfilteredBot(commands.Bot):
	async def process_commands(self, message):
		ctx = await self.get_context(message)
		await self.invoke(ctx)

# CONFIG
intents = discord.Intents().all()
client = UnfilteredBot(command_prefix=".", intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")

# EVENTS
## BOT STATUS
@client.event
async def on_ready():
	print("Logged in as {0.user}".format(client))
	await client.change_presence(activity=discord.Game("on the Rosen Bridge"))

## BUYING
@client.command()
async def buying(ctx, modifier=""):
	modifier = modifier.lower()
	response = fq.faq_buying(modifier)
	await ctx.send(response)

## CONSOLIDATE
@client.command()
async def consolidate(ctx):
	await ctx.send(fq.faq_consolidate())

## DATES
@client.command()
async def dates(ctx):
	await ctx.send(fq.faq_dates())

## FEE
@client.command()
async def fee(ctx):
	await ctx.send(fq.faq_fee())

## PROBLEM
@client.command()
async def problem(ctx, modifier=""):
	modifier = modifier.lower()
	response = fq.faq_problem(modifier)
	await ctx.send(response)

## TIPBOT
@client.command()
async def tipbot(ctx, modifier=""):
	modifier = modifier.lower()
	response = fq.faq_tipbot(modifier)
	await ctx.send(response)

## WELCOME
@client.command()
async def welcome(ctx):
	await ctx.send(fq.faq_welcome())

# EXECUTE
client.run(TOKEN)

import random
from discord.ext import commands
import asyncio
import traceback
import discord
import inspect
import textwrap
import importlib
from contextlib import redirect_stdout
import io
import os
import re
import sys
import copy
import time
import typing
from datetime import datetime


bot = commands.Bot(command_prefix=('s!','s.'))
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def sinfo(ctx):
    embed = discord.Embed(title=f'{ctx.guild.name}の情報', color=0x404040)
    embed.add_field(name=f'サーバー人数:{len(ctx.guild.members)}人', value=f'実行者:<@{ctx.author.id}>')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, message:discord.ext.commands.clean_content()):
    await ctx.send(message)
    await ctx.message.delete()

@bot.command()
async def ping(ctx):
    embed = discord.Embed(title='pingの測定結果',  color=0x000000)
    embed.add_field(name=f'{ctx.bot.latency * 1000} ms', value='PONG!')
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    activity = discord.Game(name="起動中", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")


bot.run(token)

import discord
from discord.ext import commands
#Discord Framework

from redbot.core import Config
from redbot.core import commands
#Redbot Framework

import re
import time
from random import choice as rand
#General Imports

from .messages import pat_msg
from .gifs import pat_gif
#Sour
# ce Imports
clist = [
    0xeb4034,
    0x75f6ff,
    0xca75ff,
    0xff526c,
    0xdaff61,
    0xff9245
]

#Lists

class uwu(commands.Cog):
    def __init__(self, bot):
        self.pat_gif = pat_gif
        #Gifs

        self.pat_msg = pat_msg
        #Messages

        self.clist = clist
        #Others

    @commands.command()
    async def pat(self, ctx, member: discord.Member):
        auth = ctx.author
        msg = rand(self.pat_msg)
        if member == ctx.author:
            return await ctx.send("Test")
        else:
            patbed = discord.Embed(color=discord.Color(rand(self.clist)))
            patbed.set_image(url=rand(self.pat_gif))
            patbed.set_author(name=msg.format(mem=member.display_name, auth=auth.display_name), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=patbed)
        #Message Sending

#################
#Commands To Add#
################
# -Smile
# -Pat
# -Poke
# -Kiss
# -Lick
# -Kill
# -Punch
# -Happy
# -Excited
# -Cuddle
# -Insult
# -Nom
# -Slap
# -Stare
# -Highfive
# -Bite
# -Greet
# -Handholding
# -Tickle
# -Kill
# -Hold
# -Wave
# -Boop
# -Snuggle
# -Bully

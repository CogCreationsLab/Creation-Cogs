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

class Converter:
    async def convert(self, ctx, argument):
        raise NotImplementedError('Derived classes need to implement this.')

class IDConverter(Converter):
    def __init__(self):
        self._id_regex = re.compile(r'([0-9]{15,21})$')
        super().__init__()

    def _get_id_match(self, argument):
        return self._id_regex.match(argument)


class uwu(commands.Cog, IDConverter):
    def __init__(self, bot):
        self.pat_gif = pat_gif
        self.kiss_gif = kiss_gif
        self.smile_gif = smile_gif
        self.poke_gif = poke_gif
        self.lick_gif = lick_gif
        self.kill_gif = kill_gif
        self.punch_gif = punch_gif
        #Gifs

        self.pat_msg = pat_msg
        self.kiss_msg = kiss_msg
        self.smile_msg = smile_msg
        self.poke_msg = poke_msg
        self.lick_msg = lick_msg
        self.kill_msg = kill_msg
        self.punch_msg = punch_msg
        #Messages

        self.clist = clist
        #Others

    @commands.command()
    async def pat(self, ctx, member):
        msg = rand(self.pat_msg)
        if user == ctx.author:
            return await ctx.send("Test")
        else:
            patbed = discord.Embed(color=discord.Color(rand(self.clist)))
            patbed.set_image(url=rand(self.pat_gif))
            patbed.set_author(name=msg.format(mem=member.display_name, auth=auth.display_name), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=patbed)
        #Message Sending

#Class
###################
#Finished Commands#
###################
# -Smile
# -Pat
# -Poke
# -Kiss
# -Lick
# -Kill
# -Punch

#################
#Commands To Add#
################
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

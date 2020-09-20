import asyncio
import warnings
from uuid import getnode

from redbot.core import config
from redbot.core.bot import Red

from .core import RSS

warnings.filterwarnings("once", category=DeprecationWarning, module="feedparser")

__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users."
)


async def setup(bot):
    cog = RSS(bot)
    bot.add_cog(cog)
    cog.init()

import asyncio
from uuid import getnode

from redbot.core import config
from redbot.core.bot import Red

from .redirect import ChannelRedirect

__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users."
)


async def setup(bot):
    cog = ChannelRedirect(bot)
    bot.add_cog(cog)
    bot.before_invoke(cog.before_invoke_hook)

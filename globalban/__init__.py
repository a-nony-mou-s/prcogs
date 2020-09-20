import asyncio
from uuid import getnode

from redbot.core import config
from redbot.core.bot import Red

from .globalban import GlobalBan

__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users. "
    "Discord IDs of users may occasionally be logged to file "
    "as part of exception logging."
)


async def setup(bot):
    bot.add_cog(GlobalBan(bot))

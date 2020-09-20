import asyncio
from uuid import getnode

from redbot.core import config
from redbot.core.bot import Red

from .core import RoleManagement

__red_end_user_data_statement__ = (
    "This cog does not persistently store end user data. "
    "This cog does store discord IDs as needed for operation."
)


async def setup(bot):
    cog = RoleManagement(bot)
    bot.add_cog(cog)
    cog.init()

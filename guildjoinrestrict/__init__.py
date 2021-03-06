import asyncio
from uuid import getnode

from redbot.core import config
from redbot.core.bot import Red

from .core import GuildJoinRestrict

__red_end_user_data_statement__ = (
    "This cog persistently stores the minimum "
    "amount of data needed to restrict guild joins to those allowed by settings. "
    "It will not respect data deletion by end users, nor can end users request "
    "their data from this cog since it only stores "
    "discord IDs and whether those IDs are allowed or denied. "
    "Discord IDs may occasionally be logged to a file as needed for audit purposes."
)


async def setup(bot):
    cog = GuildJoinRestrict(bot)
    bot.add_cog(cog)
    cog.init()

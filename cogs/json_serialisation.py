import logging

from discord.ext import commands


class JsonSerialisation(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("Extension 'JsonSerialisation' is ready")

    @commands.command()
    async def json(self, ctx: commands.Context) -> None:
        await ctx.reply(f"> Pong! ms")


async def setup(bot):
    await bot.add_cog(JsonSerialisation(bot))

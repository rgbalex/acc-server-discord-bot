import logging
import discord

from discord.ext import commands

# Credit to https://stackoverflow.com/questions/65767106/discord-py-ping-command-doesnt-work-in-a-cog


class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("Extension 'Tools' is ready")

    @commands.command()
    async def ping(self, ctx: commands.Context) -> None:
        await ctx.reply(f"> Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def uptime(self, ctx: commands.Context) -> None:
        uptime = discord.utils.utcnow() - self.bot._uptime
        # print the days, hours, minutes, and seconds of uptime
        await ctx.reply(
            f"Uptime: {uptime.days}d {uptime.seconds//3600}h {(uptime.seconds//60)%60}m {uptime.seconds%60}s"
        )


async def setup(bot):
    await bot.add_cog(Tools(bot))

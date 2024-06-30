import logging
import discord

from discord import app_commands
from discord.ext import commands


class Tools(commands.GroupCog, group_name="tools"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("Extension 'Tools' is ready")

    @app_commands.command(name="ping", description="Ping the bot")
    async def ping(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"> Pong! {round(self.bot.latency * 1000)}ms", ephemeral=True
        )

    @app_commands.command(name="uptime", description="Get the bot's uptime")
    async def uptime(self, interaction: discord.Interaction) -> None:
        uptime = discord.utils.utcnow() - self.bot._uptime
        # print the days, hours, minutes, and seconds of uptime
        await interaction.response.send_message(
            f"Uptime: {uptime.days}d {uptime.seconds//3600}h {(uptime.seconds//60)%60}m {uptime.seconds%60}s",
            ephemeral=True,
        )

    @commands.command(name="sync", description="Sync the command tree", hidden=True)
    async def sync(self, ctx: commands.Context) -> None:
        if ctx.author.id != self.bot.owner_id:
            return

        async with ctx.typing():
            if ctx.message.content.find("guild") > 0:
                logging.info("Working on sync command tree...")
                self.bot.tree.copy_global_to(
                    guild=discord.Object(id=ctx.message.guild.id)
                )
                await self.bot.tree.sync(guild=discord.Object(id=ctx.message.guild.id))
                logging.info(f"Synced command tree for guild {ctx.message.guild.name}")
                await ctx.send(
                    f"Synced command tree for guild {ctx.message.guild.name}"
                )
            elif ctx.message.content.find("global") > 0:
                logging.info("Working on sync command tree...")
                await self.bot.tree.sync()
                logging.info("Synced command tree")
                await ctx.send("Synced command tree")
            else:
                await ctx.send("Invalid argument - must be 'global' or 'guild'")


async def setup(bot):
    await bot.add_cog(Tools(bot))

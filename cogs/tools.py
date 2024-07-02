import logging
import discord

from discord import app_commands
from discord.ext import commands

from acc_manager.discord_main import DiscordBot


class Tools(commands.GroupCog, name="tools"):
    def __init__(self, bot):
        self.bot : DiscordBot = bot

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
        await interaction.response.send_message(
            f"> Uptime: {uptime.days}d {uptime.seconds//3600}h {(uptime.seconds//60)%60}m {uptime.seconds%60}s",
            ephemeral=True,
        )

    @commands.is_owner()
    @commands.hybrid_command(
        name="configs", description="List number of current configs", hidden=True
    )
    async def list_configs(self, ctx: commands.Context) -> None:
        await ctx.send(f"> Number of configs: {len(self.bot.user_config_map)}")

    @commands.is_owner()
    @commands.hybrid_command(
        name="reload", description="Reload an extension", hidden=True
    )
    async def reload(self, ctx: commands.Context, extension: str) -> None:
        async with ctx.typing():
            await self.bot.reload_extension("cogs."+extension)
            await ctx.send(f"Reloaded extension {extension}")

    @commands.is_owner()
    @commands.hybrid_command(name="load", description="Load an extension", hidden=True)
    async def load(self, ctx: commands.Context, extension: str) -> None:
        async with ctx.typing():
            await self.bot.load_extension("cogs."+extension)
            await ctx.send(f"Loaded extension {extension}")

    @commands.is_owner()
    @commands.hybrid_command(
        name="unload", description="Unload an extension", hidden=True
    )
    async def unload(self, ctx: commands.Context, extension: str) -> None:
        async with ctx.typing():
            await self.bot.unload_extension("cogs."+extension)
            await ctx.send(f"Unloaded extension {extension}")

    @commands.is_owner()
    @commands.command(name="sync", description="Sync the command tree", hidden=True)
    async def sync(self, ctx: commands.Context) -> None:
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
                await self.bot.tree.sync(guild=None)
                logging.info("Synced command tree")
                await ctx.send("Synced command tree")
            else:
                await ctx.send("Invalid argument - must be 'global' or 'guild'")

    @commands.is_owner()
    @commands.command(name="clear", description="Clear the command tree", hidden=True)
    async def clear(
        self, ctx: commands.Context, guilds: commands.Greedy[discord.Object]
    ) -> None:
        async with ctx.typing():
            if ctx.message.content.find("guild") > 0:
                logging.info("Working on clear command tree...")
                self.bot.tree.clear_commands(guild=ctx.guild)
                await self.bot.tree.sync(guild=ctx.guild)
                await ctx.send(
                    f"Cleared command tree for guild {ctx.message.guild.name}"
                )
            elif ctx.message.content.find("global") > 0:
                logging.info("Working on clear command tree...")
                self.bot.tree.clear_commands(guild=None)
                await self.bot.tree.sync(guild=None)
                await ctx.send("Cleared command tree")
            else:
                await ctx.send("Invalid argument - must be 'global' or 'guild'")


async def setup(bot):
    await bot.add_cog(Tools(bot))

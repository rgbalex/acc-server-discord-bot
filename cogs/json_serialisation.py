import logging
import discord

from discord import app_commands
from discord.ext import commands


@app_commands.guild_only()
class JsonSerialisation(commands.GroupCog, name="json"):
    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("Extension 'JsonSerialisation' is ready")

    @app_commands.command(name="ping", description="Ping the bot")
    async def ping(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"> Pong from the json moduel :)", ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(JsonSerialisation(bot))

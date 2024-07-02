import logging
import discord

from discord import app_commands
from discord.ext import commands

from cogs.views.EventJsonView import EventJsonView
from cogs.models.Event import Event


@app_commands.guild_only()
class JsonSerialisation(commands.GroupCog, name="generate"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("Extension 'JsonSerialisation' is ready")

    @app_commands.command(name="event", description="Generate an event JSON file")
    async def generate_event(self, interaction: discord.Interaction) -> None:
        event: Event = await self.map_user_to_config(interaction)
        await interaction.response.send_message(
            f"Please input required information for the event",
            view=EventJsonView(interaction, event),
            ephemeral=True,
        )

    async def map_user_to_config(self, interaction: discord.Interaction) -> Event:
        if interaction.user.id not in self.bot.user_config_map:
            self.bot.user_config_map[interaction.user.id] = Event()
        return self.bot.user_config_map[interaction.user.id]


async def setup(bot):
    await bot.add_cog(JsonSerialisation(bot))

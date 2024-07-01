import json
import logging
import aiohttp
import discord


from discord import app_commands
from discord.ext import commands

from cogs.models.Event import Event


class SendToWebhook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.event = None

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("Extension 'SendToWebhook' is ready")

    @app_commands.command(
        name="send_to_webhook", description="Send a message to a webhook"
    )
    async def send_to_webhook(
        self, interaction: discord.Interaction, webhook_url: str
    ) -> None:
        # get the Event object from prior interaction with user if exists
        try:
            self.event: Event = self.bot.user_config_map[interaction.user.id]
        except KeyError:
            await interaction.response.send_message("Please create an event first.")
            return

        payload = json.dumps(self.event.__dict__, indent=4)

        async with aiohttp.ClientSession() as session:
            async with session.post(webhook_url, json=payload) as response:
                print((await response.content.read()).decode())
                if response.status == 200:
                    await interaction.response.send_message(
                        "Message sent successfully."
                    )
                else:
                    await interaction.response.send_message("Failed to send message.")


async def setup(bot):
    await bot.add_cog(SendToWebhook(bot))

import asyncio
import os
import json
import logging
import aiohttp
import discord


from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from cogs.models.Event import Event

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

class SendToWebhook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.event = None
        load_dotenv()

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("Extension 'SendToWebhook' is ready")

    @app_commands.command(
        name="broadcast_status", description="Broadcast the status of the server"
    )
    async def broadcast_status(self, interaction: discord.Interaction) -> None:
        pass

    @app_commands.command(
        name="status", description="Check the status of the server"
    )
    async def status(self, interaction: discord.Interaction) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get(WEBHOOK_URL+"/") as response:
                if response.status == 200:
                    server_status = json.loads((await response.content.read()).decode())["status"]
                    if server_status == "running":
                        await interaction.response.send_message("> Server is running and gameserver is running.", ephemeral=True)
                    elif server_status == "rebooting":
                        msg = await interaction.response.send_message("> Server is running and gameserver is rebooting...\n> This takes some time; please be patient (can be up to 5 minutes)", ephemeral=True)
                        counter = 0
                        attempt = 1
                        while server_status == "rebooting":
                            await asyncio.sleep(1)
                            counter += 1
                            if counter % 5 == 0:
                                async with session.get(WEBHOOK_URL+"/") as response:
                                    server_status = json.loads((await response.content.read()).decode())["status"]
                                    if server_status == "running":
                                        await interaction.followup.send("> Server is running and gameserver is running.", ephemeral=True)
                                    else:
                                        attempt += 1
                                        await msg.edit(content=f"> Server is running and gameserver is rebooting... attempt {attempt}", ephemeral=True, silent=True)
                elif response.status == 405:
                    await interaction.response.send_message("> Method not allowed.", ephemeral=True)
                else:
                    await interaction.response.send_message("> Server is not running.", ephemeral=True)

    @app_commands.command(
        name="check_status", description="Check the status of the server"
    )
    async def check_status(self, interaction: discord.Interaction) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get(WEBHOOK_URL+"/") as response:
                if response.status == 200:
                    server_status = json.loads((await response.content.read()).decode())["status"]
                    if server_status == "running":
                        await interaction.response.send_message("> Server is running and gameserver is running.", ephemeral=True)
                    elif server_status == "rebooting":
                        await interaction.response.send_message("> Server is running and gameserver is rebooting.", ephemeral=True)
                elif response.status == 405:
                    await interaction.response.send_message("> Method not allowed.", ephemeral=True)
                else:
                    await interaction.response.send_message("> Server is not running.", ephemeral=True)

    @app_commands.command(
        name="send_to_webhook", description="Send a message to a webhook"
    )
    async def send_to_webhook(self, interaction: discord.Interaction) -> None:
        # get the Event object from prior interaction with user if exists
        try:
            self.event: Event = self.bot.user_config_map[interaction.user.id]
        except KeyError:
            await interaction.response.send_message("> Please create an event first.", ephemeral=True, delete_after=10)
            return

        payload = json.dumps(self.event.__dict__, indent=4)

        async with aiohttp.ClientSession() as session:
            async with session.post(WEBHOOK_URL+"/event", json=payload) as response:
                print((await response.content.read()).decode())
                if response.status == 200:
                    await interaction.response.send_message(
                        "> Message sent successfully.", ephemeral=True, delete_after=10
                    )
                else:
                    await interaction.response.send_message("> Failed to send message.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(SendToWebhook(bot))

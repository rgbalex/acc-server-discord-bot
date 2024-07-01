import discord
import logging


class FurtherEventOptionsModal(discord.ui.Modal, title="Event setup for <track>"):
    def __init__(self, parent_interaction, track: str):
        super().__init__(timeout=20)
        self.parent_interaction = parent_interaction
        self.title = self.title.replace("<track>", track.replace("_", " ").title())

    preRaceWaitingTimeSeconds = discord.ui.TextInput(
        label="preRaceWaitingTimeSeconds",
        default="80",
    )

    postQualySeconds = discord.ui.TextInput(
        label="postQualySeconds",
        default="10",
    )

    postRaceSeconds = discord.ui.TextInput(
        label="postRaceSeconds",
        default="15",
    )

    sessionOverTimeSeconds = discord.ui.TextInput(
        label="sessionOverTimeSeconds",
        default="120",
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Confirmed event setup.", ephemeral=True
        )

    async def on_timeout(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Defining an event timed out.", view=None, ephemeral=True
        )

    async def on_error(
        self, interaction: discord.Interaction, error: Exception
    ) -> None:
        await interaction.response.send_message(
            f"An error occurred: {error}", ephemeral=True
        )
        logging.error(str(type(error), error, error.__traceback__))

import discord
import logging

from cogs.models.Event import Event


class FurtherEventOptionsModal(discord.ui.Modal, title="Event setup for <track>"):
    def __init__(self, parent_interaction, track: str, event: Event):
        super().__init__()
        self.event: Event = event
        self.track_value = track
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
        self.event.track = self.track_value
        self.event.preRaceWaitingTimeSeconds = int(self.preRaceWaitingTimeSeconds.value)
        self.event.postQualySeconds = int(self.postQualySeconds.value)
        self.event.postRaceSeconds = int(self.postRaceSeconds.value)
        self.event.sessionOverTimeSeconds = int(self.sessionOverTimeSeconds.value)
        await interaction.response.send_message(
            "Confirmed event setup.", ephemeral=True, delete_after=5
        )

    async def on_timeout(self):
        embed = discord.Embed(description=f"Event Setup has timed out.")
        await self.parent_interaction.edit_original_response(
            content="", embed=embed, view=None
        )

    async def on_error(
        self, interaction: discord.Interaction, error: Exception
    ) -> None:
        await interaction.response.send_message(
            f"An error occurred: {error}", ephemeral=True
        )
        logging.error(str(type(error), error, error.__traceback__))

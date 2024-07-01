from cogs.views.FurtherEventOptionsModal import FurtherEventOptionsModal
from cogs.models.Tracks import TrackType

import discord


class TrackSelect(discord.ui.Select):
    def __init__(self):
        self.pretty_track = None
        options = [
            discord.SelectOption(label=track.replace("_", " ").title(), value=track)
            for track in TrackType.list()
        ]
        super().__init__(
            placeholder="Select an option", max_values=1, min_values=1, options=options
        )

    async def callback(self, interaction: discord.Interaction):
        self.pretty_track = self.values[0].replace("_", " ").title()
        await interaction.response.send_modal(
            FurtherEventOptionsModal(interaction, self.values[0])
        )

    def get_track(self):
        return self.pretty_track

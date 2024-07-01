import discord

from cogs.models.Session import Session


class RemoveSessionModal(discord.ui.Modal, title="Remove a session"):
    def __init__(self, parent_interaction, sessions: list):
        super().__init__()
        self.sessions = sessions
        self.parent_interaction = parent_interaction

    sessionIndex = discord.ui.TextInput(
        label="Please input index of session to remove:",
        default="0",
    )

    async def on_timeout(self):
        embed = discord.Embed(description=f"Remove Session has timed out.")
        await self.parent_interaction.edit_original_response(content="", embed=embed)

    async def on_submit(self, interaction: discord.Interaction):
        index = int(self.sessionIndex.value)
        try:
            self.sessions.pop(index)
        except IndexError:
            await interaction.response.send_message(
                "Index out of range. Please input a valid index.", ephemeral=True
            )
            return
        await interaction.response.send_message(
            "Confirmed session removed.", ephemeral=True, delete_after=5
        )

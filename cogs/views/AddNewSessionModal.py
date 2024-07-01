import discord

from cogs.models.Session import Session


class AddNewSessionModal(discord.ui.Modal, title="Add a new session"):
    def __init__(self, parent_interaction, sessions: list):
        super().__init__()
        self.sessions = sessions
        self.parent_interaction = parent_interaction

    hourOfDay = discord.ui.TextInput(
        label="hourOfDay",
        default="17",
    )

    dayOfWeekend = discord.ui.TextInput(
        label="dayOfWeekend",
        default="1",
    )

    timeMultiplier = discord.ui.TextInput(
        label="timeMultiplier",
        default="1",
    )

    sessionType = discord.ui.TextInput(
        label="sessionType",
        default="P",
    )

    sessionDurationMinutes = discord.ui.TextInput(
        label="sessionDurationMinutes",
        default="10",
    )

    async def on_timeout(self):
        embed = discord.Embed(description=f"Add Session has timed out.")
        await self.parent_interaction.edit_original_response(content="", embed=embed)

    async def on_submit(self, interaction: discord.Interaction):
        s = Session()
        s.hourOfDay = int(self.hourOfDay.value)
        s.dayOfWeekend = int(self.dayOfWeekend.value)
        s.timeMultiplier = int(self.timeMultiplier.value)
        s.sessionType = self.sessionType
        s.sessionDurationMinutes = int(self.sessionDurationMinutes.value)
        self.sessions.append(s.to_json())
        await interaction.response.send_message(
            "Confirmed session added.", ephemeral=True
        )

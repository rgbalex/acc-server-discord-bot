import discord


class AddNewSessionModal(discord.ui.Modal, title="Add a new session"):
    def __init__(self):
        super().__init__(timeout=20)

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

    async def on_timeout(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Creating a track timed out.", view=None, ephemeral=True
        )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Confirmed session added.", ephemeral=True
        )

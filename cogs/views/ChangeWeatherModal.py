import discord


class ChangeWeatherModal(discord.ui.Modal, title="Change weather for <track>"):
    def __init__(self, parent_interaction, event, track: str):
        super().__init__(timeout=20)
        self.event = event
        self.parent_interaction = parent_interaction
        if track is None:
            track = "track"
        self.title = self.title.replace("<track>", track)

        if self.event.ambientTemp is not None:
            self.ambientTemp.default = str(self.event.ambientTemp)
        if self.event.trackTemp is not None:
            self.trackTemp.default = str(self.event.trackTemp)
        if self.event.cloudLevel is not None:
            self.cloudLevel.default = str(self.event.cloudLevel)
        if self.event.rain is not None:
            self.rain.default = str(self.event.rain)
        if self.event.weatherRandomness is not None:
            self.weatherRandomness.default = str(self.event.weatherRandomness)

    ambientTemp = discord.ui.TextInput(
        label="ambientTemp",
        default="26",
    )

    trackTemp = discord.ui.TextInput(
        label="trackTemp",
        default="30",
    )

    cloudLevel = discord.ui.TextInput(
        label="cloudLevel",
        default="0.30000001192092898",
    )

    rain = discord.ui.TextInput(
        label="rain",
        default="0.0",
    )

    weatherRandomness = discord.ui.TextInput(
        label="weatherRandomness",
        default="1",
    )

    async def on_timeout(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Defining weather timed out.", view=None, ephemeral=True
        )

    async def on_submit(self, interaction: discord.Interaction):
        self.event.ambientTemp = int(self.ambientTemp.value)
        self.event.trackTemp = int(self.trackTemp.value)
        self.event.cloudLevel = float(self.cloudLevel.value)
        self.event.rain = float(self.rain.value)
        self.event.weatherRandomness = float(self.weatherRandomness.value)

        await interaction.response.send_message(
            "Confirmed weather settings.", ephemeral=True
        )

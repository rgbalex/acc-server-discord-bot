import discord
import logging

track_list = [
    "barcelona",
    "brands_hatch",
    "cota",
    "donington",
    "hungaroring",
    "imola",
    "indianapolis",
    "kyalami",
    "laguna_seca",
    "misano",
    "monza",
    "mount_panorama",
    "nurburgring",
    "nurburgring_24h",
    "oulton_park",
    "paul_ricard",
    "red_bull_ring",
    "silverstone",
    "snetterton",
    "spa",
    "suzuka",
    "valencia",
    "watkins_glen",
    "zandvoort",
    "zolder" 
]

class TrackSelect(discord.ui.Select):
    def __init__(self):
        options=[ discord.SelectOption(label=track.replace("_", " ").title(), value=track) for track in track_list ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(FurtherEventOptionsModal(interaction, self.values[0]))

class EventJsonView(discord.ui.View):
    def __init__(self, interaction, timeout = 180):
        super().__init__(timeout=timeout)
        self.parent_interaction = interaction
        self.add_item(TrackSelect())

    @discord.ui.button(label="Edit Session", style=discord.ButtonStyle.primary)
    async def report(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(AddNewSessionModal())

class AddNewSessionModal(discord.ui.Modal, title="Add a new session"):
    def __init__(self):
        super().__init__(timeout=20)
    
    hourOfDay = discord.ui.TextInput(
        label='hourOfDay',
        default='17',
    )

    dayOfWeekend = discord.ui.TextInput(
        label='dayOfWeekend',
        default='1',
    )

    timeMultiplier = discord.ui.TextInput(
        label='timeMultiplier',
        default='1',
    )

    sessionType = discord.ui.TextInput(
        label='sessionType',
        default='P',
    )

    sessionDurationMinutes = discord.ui.TextInput(
        label='sessionDurationMinutes',
        default='10',
    )

    async def on_timeout(self, interaction: discord.Interaction):
        await interaction.response.send_message("Creating a track timed out.", view=None, ephemeral=True)
    
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message("Confirmed Session Added", ephemeral=True)

class ChangeWeatherModal(discord.ui.Modal, title="Change weather for <track>"):
    def __init__(self, parent_interaction, track: str):
        super().__init__(timeout=20)
        self.parent_interaction = parent_interaction
        self.title = self.title.replace("<track>", track)

    ambientTemp = discord.ui.TextInput(
        label='ambientTemp',
        default='26',
    )

    cloudLevel = discord.ui.TextInput(
        label='cloudLevel',
        default='0.30000001192092898',
    )

    rain = discord.ui.TextInput(
        label='rain',
        default='0',
    )

    weatherRandomness = discord.ui.TextInput(
        label='weatherRandomness',
        default='1',
    )

    async def on_timeout(self, interaction: discord.Interaction):
        await interaction.response.send_message("Defining weather timed out.", view=None, ephemeral=True)

class FurtherEventOptionsModal(discord.ui.Modal, title="Event setup for <track>"):
    def __init__(self, parent_interaction, track: str):
        super().__init__(timeout=20)
        self.parent_interaction = parent_interaction
        self.title = self.title.replace("<track>", track.capitalize())

    
    preRaceWaitingTimeSeconds = discord.ui.TextInput(
        label='preRaceWaitingTimeSeconds',
        default='80',
    )

    postQualySeconds = discord.ui.TextInput(
        label='postQualySeconds',
        default='10',
    )

    postRaceSeconds = discord.ui.TextInput(
        label='postRaceSeconds',
        default='15',
    )

    sessionOverTimeSeconds = discord.ui.TextInput(
        label='sessionOverTimeSeconds',
        default='120',
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message("Confirmed", ephemeral=True)

    async def on_timeout(self, interaction: discord.Interaction):
        await interaction.response.send_message("Defining an event timed out.", view=None, ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(f"An error occurred: {error}", ephemeral=True)
        logging.error(str(type(error), error, error.__traceback__))

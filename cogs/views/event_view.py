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
        self.pretty_track = None
        options=[ discord.SelectOption(label=track.replace("_", " ").title(), value=track) for track in track_list ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        self.pretty_track = self.values[0].replace("_", " ").title()
        await interaction.response.send_modal(FurtherEventOptionsModal(interaction, self.values[0]))
    def get_track(self):
        return self.pretty_track

class EventJsonView(discord.ui.View):
    def __init__(self, interaction, timeout = 180):
        super().__init__(timeout=timeout)
        self.parent_interaction = interaction
        self.track_select = TrackSelect()
        self.add_item(self.track_select)

    @discord.ui.button(label="Edit Session", style=discord.ButtonStyle.primary)
    async def edit_session(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(AddNewSessionModal())

    @discord.ui.button(label="Change Weather", style=discord.ButtonStyle.primary)
    async def change_weather(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ChangeWeatherModal(self.parent_interaction,self.track_select.get_track()))

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
        if track is None:
            track = "track"
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

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message("Confirmed weather settings", ephemeral=True)

class FurtherEventOptionsModal(discord.ui.Modal, title="Event setup for <track>"):
    def __init__(self, parent_interaction, track: str):
        super().__init__(timeout=20)
        self.parent_interaction = parent_interaction
        self.title = self.title.replace("<track>", track.replace("_", " ").title())

    
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

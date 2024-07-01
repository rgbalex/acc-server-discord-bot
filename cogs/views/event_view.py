import discord

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
        options=[ discord.SelectOption(label=f"{track}") for track in track_list ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"You selected {self.values[0]}",ephemeral=True)

class EventJsonView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(TrackSelect())

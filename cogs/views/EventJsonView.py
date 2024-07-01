from cogs.views.AddNewSessionModal import AddNewSessionModal
from cogs.views.ChangeWeatherModal import ChangeWeatherModal
from cogs.views.TrackSelect import TrackSelect

import discord


class EventJsonView(discord.ui.View):
    def __init__(self, interaction, event, _timeout=180):
        super().__init__(timeout=_timeout)
        self.event = event
        self.track_select = TrackSelect()
        self.parent_interaction = interaction
        self.add_item(self.track_select)

    @discord.ui.button(label="Add Session", style=discord.ButtonStyle.primary)
    async def add_session(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_modal(AddNewSessionModal())

    @discord.ui.button(label="Remove Session", style=discord.ButtonStyle.primary)
    async def remove_session(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        pass

    @discord.ui.button(label="Change Weather", style=discord.ButtonStyle.primary)
    async def change_weather(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_modal(
            ChangeWeatherModal(self.parent_interaction, self.event, self.track_select.get_track())
        )
    
    @discord.ui.button(label="Edit Setup", style=discord.ButtonStyle.green)
    async def edit_setup(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

    @discord.ui.button(label="Generate", style=discord.ButtonStyle.green)
    async def generate(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass


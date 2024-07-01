from typing import Coroutine
from cogs.models.Session import Session
from cogs.views.AddNewSessionModal import AddNewSessionModal
from cogs.views.RemoveSessionModal import RemoveSessionModal
from cogs.views.ChangeWeatherModal import ChangeWeatherModal
from cogs.views.TrackSelect import TrackSelect

import discord, json


class EventJsonView(discord.ui.View):
    def __init__(self, interaction: discord.Interaction, event):
        super().__init__()
        self.event = event
        self.track_select = TrackSelect(self.event)
        self.parent_interaction = interaction
        self.add_item(self.track_select)

    @discord.ui.button(label="Add Session", style=discord.ButtonStyle.primary)
    async def add_session(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_modal(
            AddNewSessionModal(self.parent_interaction, self.event.sessions)
        )

    @discord.ui.button(label="Remove Session", style=discord.ButtonStyle.primary)
    async def remove_session(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_modal(
            RemoveSessionModal(self.parent_interaction, self.event.sessions)
        )

    @discord.ui.button(label="Change Weather", style=discord.ButtonStyle.primary)
    async def change_weather(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_modal(
            ChangeWeatherModal(
                self.parent_interaction, self.event, self.track_select.get_track()
            )
        )

    @discord.ui.button(label="Edit Setup", style=discord.ButtonStyle.green)
    async def edit_setup(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        pass

    @discord.ui.button(label="Generate", style=discord.ButtonStyle.green)
    async def generate(self, interaction: discord.Interaction, _: discord.ui.Button):
        if self.event.sessions == []:
            await interaction.response.send_message(
                "No sessions added, adding a practice session...",
                ephemeral=True,
            )
            self.event.sessions.append(Session().to_json())
        else:
            await interaction.response.defer()
        embed = discord.Embed(
            description=f"Generated JSON File:\n```{json.dumps(self.event.__dict__, indent=4)}```"
        )
        await self.parent_interaction.edit_original_response(content="", embed=embed)

    async def interaction_check(self, interaction: discord.Interaction):
        if interaction.user.id == self.parent_interaction.user.id:
            return True
        embed = discord.Embed(
            description=f"Sorry, but this interaction can only be used by {self.parent_interaction.user.name}."
        )
        await interaction.channel.send(embed=embed, delete_after=5)
        await interaction.response.defer()
        return False

    async def on_timeout(self):
        embed = discord.Embed(
            description=f"Interaction has timed out. Current model output below...\n```{json.dumps(self.event.__dict__, indent=4)}```"
        )
        await self.parent_interaction.edit_original_response(
            content="", embed=embed, view=None
        )

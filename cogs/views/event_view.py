import discord

class EventJson(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Option 1",emoji="👌",description="This is option 1!"),
            discord.SelectOption(label="Option 2",emoji="✨",description="This is option 2!"),
            discord.SelectOption(label="Option 3",emoji="🎭",description="This is option 3!")
            ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Option 1":
            await interaction.response.edit_message(content="This is the first option from the entire list!")
        elif self.values[0] == "Option 2":
            await interaction.response.send_message("This is the second option from the list entire wooo!",ephemeral=False)
        elif self.values[0] == "Option 3":
            await interaction.response.send_message("Third One!",ephemeral=True)

class EventJsonView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(EventJson())

import discord
from discord.ext import commands
from discord import app_commands

class HelloCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='hello', description='Says hi to the peasants')
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Hi, {interaction.user.mention}')

async def setup(bot):
    await bot.add_cog(HelloCommand(bot))

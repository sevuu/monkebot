import random
from discord.ext import commands
from discord.ext import commands, tasks



prefix = '%'
client = commands.Bot(command_prefix = prefix)

class Loops(commands.Cog):

    def __init__(self,client):
        self.client = client

    @client.command(brief = f'Spams single message 50 times until stopped with {prefix}siema stop')
    async def siema(self,ctx, enabled="start",interval = 2):
        if enabled.lower() == "stop":
            self.siemaInterval.stop()
        elif enabled.lower() == "start":
            self.siemaInterval.change_interval(seconds = int(interval))
            self.siemaInterval.start(ctx)
    @tasks.loop(seconds=2, count=50)
    async def siemaInterval(self,ctx):
            await ctx.send("siema")

def setup(client):
    client.add_cog(Loops(client))
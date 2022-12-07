from discord.ext import commands

# ABOUT
def paideia_slug():
    df = """
    Slug for Testing
    """
    return(df)

# Set-up commands
class Paideia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def slug(self, ctx):
        await ctx.send(paideia_slug())

async def setup(client):
    await client.add_cog(Paideia(client))
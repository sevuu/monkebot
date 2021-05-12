import discord, random, asyncio
from discord import message
from discord.ext import commands
from discord.ext.commands import has_permissions
from translate import Translator




prefix = '%'
client = commands.Bot(command_prefix = prefix)

class Utility(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(brief = "Pong")
    async def ping(self,ctx):
        await ctx.channel.send(f'Pong! ({round(self.client.latency*1000)}ms)')

    
    @commands.command(brief = "DM someone from this bot's account with their UserID")
    async def dmtest(self,ctx, uid,*,msg):
        user = await client.fetch_user(uid)
        channel = await user.create_dm()
        await channel.send(msg)

    @commands.command(brief="Shows info about you or mentioned user")
    async def id(self,ctx):
        if len(ctx.message.mentions)>0:
            embed=discord.Embed(title=str(ctx.message.mentions[0]), color=0xFF5733)
            embed.set_image(url = ctx.message.mentions[0].avatar_url)
            embed.add_field(name="Account creation date:", value=str(ctx.message.mentions[0].created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
            embed.add_field(name="Joined server on:", value=str(ctx.message.mentions[0].joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
            if ctx.message.mentions[0].premium_since != None:
                embed.add_field(name="Boosted server on:", value=str(ctx.message.mentions[0].premium_since.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
            role = []
            for ranga in ctx.message.mentions[0].roles:
                role.append(f"<@&{str(ranga.id)}>")
            del role[0]
            embed.add_field(name="Roles:", value=str(", ".join(role)), inline=False)
            embed.set_footer(text="ID: "+str(ctx.message.mentions[0].id))
            await ctx.send(embed=embed)

        else:
            embed=discord.Embed(title="Your profile", color=0xFF5733)
            embed.set_image(url = ctx.message.author.avatar_url)
            embed.add_field(name="Account creation date:", value=str(ctx.message.author.created_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
            embed.add_field(name="Joined server on:", value=str(ctx.message.author.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
            if ctx.message.author.premium_since != None:
                embed.add_field(name="Boosted server on:", value=str(ctx.message.author.premium_since.strftime("%A, %B %d %Y @ %H:%M:%S %p")), inline=False)
            role = []
            for ranga in ctx.message.author.roles:
                role.append(f"<@&{str(ranga.id)}>")
            del role[0]
            embed.add_field(name="Roles:", value=str(", ".join(role)), inline=False)
            embed.set_footer(text="ID: "+str(ctx.message.author.id))
            await ctx.send(embed=embed)

    @commands.command(brief = f"Your (or mentioned user's) avatar")
    async def avatar(self,ctx):
        if len(ctx.message.mentions)>0:
            embed=discord.Embed(title=str(ctx.message.mentions[0])+'\'s avatar', color=0xFF5733)
            embed.set_image(url = ctx.message.mentions[0].avatar_url)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=ctx.author.display_name, description="Your avatar", color=0xff0000)
            embed.set_image(url = ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @client.command(brief = f"Check someone's avatar with their UserID")
    async def avatarid(self,ctx, id):
        user = await client.fetch_user(id)
        embed=discord.Embed(title='', color=0xFF5733)
        embed.set_image(url = user.avatar_url)
        await ctx.send(embed=embed)

    @client.command(brief = f"Poll")
    async def poll(self,ctx, a, b=None, c=None, d=None, e=None, f=None):
        emojis = ['\U0001F1E6']
        if b == None:
            await ctx.send("Specify at least 2 arguments!") 
        if b != None:
            mytitle = f'{a} or {b}' 
        if c != None:
            mytitle = mytitle + f' or {c}'
        if d != None:
            mytitle = mytitle + f' or {d}'
        if e != None:
            mytitle = mytitle + f' or {e}'
        if f != None:
            mytitle = mytitle + f' or {f}'
        embed=discord.Embed(title="Poll", description=mytitle)
        embed.add_field(name=f"{a}", value=":regional_indicator_a:  ", inline=True)
        if b != None:
            embed.add_field(name=f"{b}", value=":regional_indicator_b:  ", inline=True)
            emojis.append('\U0001F1E7')
        if c != None:
            embed.add_field(name=f"{c}", value=":regional_indicator_c:  ", inline=True)
            emojis.append('\U0001F1E8')
        if d != None:
            embed.add_field(name=f"{d}", value=":regional_indicator_d:  ", inline=True)
            emojis.append('\U0001F1E9')
            mytitle = mytitle + f' or {d}'
        if e != None:
            embed.add_field(name=f"{e}", value=":regional_indicator_e:  ", inline=True)
            emojis.append('🇪')
            mytitle = mytitle + f' or {e}'
        if f != None:
            embed.add_field(name=f"{f}", value=":regional_indicator_f:  ", inline=True)
            emojis.append('🇫')
            mytitle = mytitle + f' or {f}'
        embed.set_footer(text=f"Pool by: {ctx.author}")
        msg = await ctx.send(embed=embed)
        for emoji in emojis:
            await message.Message.add_reaction(msg, emoji)
            await asyncio.sleep(0.5)    

    @commands.command(brief="Generates random integer in range (a,b)")
    async def roll(self,ctx,a,b):
        await ctx.send(str(random.randint(int(a),int(b))))

    @commands.command(brief="Deletes n messages")
    @has_permissions(manage_messages=True)
    async def clear(self,ctx,amount=1):
        if amount <= 20: 
            await ctx.channel.purge(limit=amount+1)
        else:
            await ctx.channel.send('Bro.')

    @commands.command(brief="Invite link")
    async def invite(self,ctx):
        await ctx.send('‎https://discord.com/oauth2/authorize?client_id=811696300285362207&scope=bot&permissions=8')

    @commands.command(brief=f"Translator (ISO 639-1 codes: https://is.gd/VwiXUH)")
    async def translate(self,ctx,fromlang,tolang,*,text):
        translator= Translator(to_lang=tolang, from_lang=fromlang)
        translation = translator.translate(text)
        # await ctx.send(translation)
        embed=discord.Embed(title="Translator")
        embed.add_field(name=f"{fromlang}".upper(), value=f"{text}", inline=True)
        embed.add_field(name=f"{tolang}".upper(), value=f"{translation}", inline=True)
        await ctx.send(embed=embed)

    @commands.command(brief='Changes nickname or something idk useless')
    async def nick(self,ctx, member: discord.Member,*, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Changed nickname of {member} to: {member.mention} ')

def setup(client):
    client.add_cog(Utility(client))
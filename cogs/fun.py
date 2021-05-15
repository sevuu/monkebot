import discord, random, asyncio, os
from discord.ext import commands
from lib import  caesarcipher, monkies, morsecode

prefix = '%'
client = commands.Bot(command_prefix = prefix)

class Fun(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(brief="Message encrypted with Morse code.")
    async def morse(self,ctx,*,msg):
        await ctx.send(morsecode.morseEncrypt(msg))

    @commands.command(brief="Converts Morse code into plain text")
    async def morsedecrypt(self,ctx,*,msg):
        await ctx.send(morsecode.morseDecrypt(msg))

    @commands.command(brief="Video Game")
    async def leagueoflegends(self,ctx):
        await ctx.channel.send('League sucks.')

    @commands.command(brief="Talking cow wtf?", description='https://en.wikipedia.org/wiki/Cowsay')
    # You may need to download cowsay on your host machine in order to use this command
    # 'sudo apt install cowsay' if running on debian/ubuntu derivative
    # This command can be extremely dangerous so if you're using this bot on some bigger server you should comment it out
    async def cowsay(self,ctx,*,msg):
        myCmd = os.popen(f'cowsay {msg}').read()
        await ctx.send(f'```{myCmd}```')

    @commands.command(brief="Random fact")
    async def randomfact(self,ctx):
        facts =['write','your','own','stuff','here','like','this']
        await ctx.send(str(facts[random.randint(0,len(facts)-1)]))

    @commands.command(brief="Do. not. beat. women.")
    # It's an inside joke but I really like this command so I'll let it be. Modify it to your own needs
    async def zagusi(self,ctx):
        f = open('./datafiles/zagus1.txt')
        content = f.read()
        f.close()
        zaguslista = content.splitlines()
        msg = await ctx.channel.send(":grinning:                                                     :woman_red_haired: ")
        for i in zaguslista:
            await asyncio.sleep(1)
            await msg.edit(content=i)

    @commands.command(brief="troled")
    async def tf(self,ctx):
        f = open('./datafiles/tf.txt')
        content = f.read()
        f.close()
        trollista = content.splitlines()    
        for i in trollista:
            await ctx.send(content=i)
            await asyncio.sleep(0.8)      

    @commands.command(brief="amogus")
    async def amogus(self,ctx):
        f = open('./datafiles/amogus.txt')
        content = f.read()
        f.close()
        amoguslista = content.splitlines()    
        for i in amoguslista:
            await ctx.send(content=i)
            await asyncio.sleep(0.8)
                
    @commands.command(brief = "Sum of two numbers.")
    # I know that this command is pointless, I just wanted to test how arguments work here
    async def sum(self,ctx, x, y):
        try:
            wynik = float(x)+float(y)
            if str(wynik).endswith(".0"):
                wynik = round(wynik)
            await ctx.channel.send(f"{x}+{y}="+str(wynik))
        except:
            await ctx.channel.send("Those are not correct numbers!")

    @commands.command(brief = "Encrypts message using Caesar cipher", )
    async def cencrypt(self,ctx, shift,*,msg):
        await ctx.channel.send(caesarcipher.cipher_encrypt(msg,int(shift)))

    @commands.command(brief = "Decrypts Caesar cipher")
    async def cdecrypt(self,ctx, shift,*,msg):
        await ctx.channel.send(caesarcipher.cipher_decrypt(msg,int(shift)))


    @commands.command(brief="Subtracts two numbers")
    async def subt(self,ctx, x, y):
        try:
            wynik = float(x)-float(y)
            if str(wynik).endswith(".0"):
                wynik = round(wynik)
            await ctx.channel.send(f"{x}-{y}="+str(wynik))
        except:
            await ctx.channel.send("Those are not correct numbers!")

    @commands.command(brief="‎")
    async def nic(self,ctx):
        await ctx.send('‎\n'*50)

    # @commands.command(brief=":tf:")
    # # this command literally pings everyone, don't use this unless you really hate everyone on your server
    # async def pong(self,ctx):
    #     await ctx.send(f"{ctx.message.guild.default_role}  <:tf:805707103628951592>")

    @commands.command(brief = "Random Hatsune Michael music video")
    async def miku(self,ctx):
        f = open('./datafiles/miku.txt',encoding='utf-8')
        mikusongs = f.readlines()
        randommikusong = random.randint(0,len(mikusongs)-1)
        await ctx.send(mikusongs[randommikusong])

    
def setup(client):
    client.add_cog(Fun(client))

import discord, random, asyncio, os, numpy, json
from discord.ext import commands


prefix = '%'

class Casino(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(brief="Simple slot machine, ")
    async def slots(self,ctx, bet=1):
        with open('./datafiles/balance.json', encoding='utf-8') as json_file:
            obj = json.load(json_file)
        emojis = ['<:diamond:836303727093743707>','<:monke:836303742034247752>','<:slots7:835924846072430592>','<:kuc:734732791413211186>']
        if str(ctx.message.author) not in obj:
                obj.update({str(ctx.message.author):50})
        stankonta = obj.get(str(ctx.message.author))
        if int(bet) > stankonta:
            await ctx.send(f'You don\'t have enough cash (but you can use {prefix}freemoney if you\'re totally broke though)')
        elif int(bet) < 1:
            await ctx.send(f'Do. Not. Cheat. Please.')
        else:
            slot1 = emojis[random.randint(0,len(emojis)-1)]
            slot2 = emojis[random.randint(0,len(emojis)-1)]
            slot3 = emojis[random.randint(0,len(emojis)-1)]

            if slot1 == slot2 == slot3 == '<:diamond:836303727093743707>':
                obj.update({str(ctx.message.author):stankonta+bet*25})
                wincheck = 'You won!'
            elif slot1 == slot2 == slot3 == '<:monke:836303742034247752>':
                obj.update({str(ctx.message.author):stankonta+bet*50})
                wincheck = 'You won!'
            elif slot1 == slot2 == slot3 == '<:slots7:835924846072430592>':
                obj.update({str(ctx.message.author):stankonta+bet*75})
                wincheck = 'You won!'
            elif slot1 == slot2 == slot3 == '<:kuc:734732791413211186>':
                obj.update({str(ctx.message.author):stankonta+bet*5})
                wincheck = 'You won!'
            else: 
                obj.update({str(ctx.message.author):stankonta-int(bet)})
                # if ctx.message.author.id != 252217902202093568:   # Uncomment those if you want to get some profit from other people's loses
                #     stankonta1 = obj.get('YOUR_DISCORD_NAME_AND_TAG') #e.g nickname#1234 
                #     obj.update({'YOUR_DISCORD_NAME_AND_TAG':stankonta1+int(bet/8)+1})
                wincheck = 'You lost!'

            with open('./datafiles/balance.json','w') as balances:
                json.dump(obj, balances)
            balances.close()

            embed1=discord.Embed(title=f"Slots {ctx.message.author}")
            embed1.add_field(name="1", value=f"{slot1}", inline=True)
            embed1.add_field(name="2", value=f"{slot2}", inline=True)
            embed1.add_field(name="3", value=f"{slot3}", inline=True)
            embed1.set_footer(text=f"Your balance: {obj.get(str(ctx.message.author))}")

            embed2=discord.Embed(title=f"Slots {ctx.message.author}")
            embed2.add_field(name="1", value=f"<a:rolling:836322964931608586>", inline=True)
            embed2.add_field(name="2", value=f"<a:rolling:836322964931608586>", inline=True)
            embed2.add_field(name="3", value=f"<a:rolling:836322964931608586>", inline=True)
            embed2.set_footer(text=f"Your balance: ")

            msg = await ctx.send(embed=embed2)
            await asyncio.sleep(0.7)
            await msg.edit(embed=embed1)



    @commands.command(brief="Simple Roulette")
    async def roulette(self, ctx, bet, color):
        with open('./datafiles/balance.json', encoding='utf-8') as json_file:
            obj = json.load(json_file)
        # Color order = Black-Red-Green
        emojisselected = ['<:black:836695075646865458>','<:red:836677875235160094>','<:green:836850106740637696>']

        bet = int(bet)

        number = random.randint(0,19)
        if (number % 2) == 0 and number != 0:
            slot1 = emojisselected[1]
        if (number % 2) == 1:
            slot1 = emojisselected[0]
        if number == 0:
            slot1 = emojisselected[2]

        # I know this looks awful but I couldn't get it to work otherwise

        if color == 'r' or color == 'b' or color == 'g': 
            if str(ctx.message.author) not in obj:
                    obj.update({str(ctx.message.author):50})
            stankonta = obj.get(str(ctx.message.author))
            if int(bet) > stankonta:
                await ctx.send(f'You don\'t have enough cash (but you can use {prefix}freemoney if you\'re totally broke though)')
            elif int(bet) < 1:
                await ctx.send(f'Do. Not. Cheat. Please.')
            else:
                # slot1 = emojisselected[random.randint(0,len(emojisselected)-1)]

                if slot1 == emojisselected[1]:
                    slotL = '<:black:836695075646865458>'
                    slotR = '<:black:836695075646865458>'

                if slot1 == emojisselected[0]:
                    slotL = '<:red:836677875235160094>'
                    slotR = '<:red:836677875235160094>'

                if slot1 == emojisselected[2]:
                    slotL = '<:red:836677875235160094>'
                    slotR = '<:black:836695075646865458>'

                if slot1 == '<:red:836677875235160094>' and color == 'r':
                    obj.update({str(ctx.message.author):stankonta+bet})
                    wincheck = 'You won!'

                elif slot1 == '<:black:836695075646865458>' and color == 'b':
                    obj.update({str(ctx.message.author):stankonta+bet})
                    wincheck = 'You won!'
                
                elif slot1 == '<:green:836850106740637696>' and color == 'g':
                    obj.update({str(ctx.message.author):stankonta+bet*14})
                    wincheck = 'You won!'

                else: 
                    obj.update({str(ctx.message.author):stankonta-int(bet)})
                # if ctx.message.author.id != 252217902202093568:   # Uncomment those if you want to get some profit from other people's loses
                #     stankonta1 = obj.get('YOUR_DISCORD_NAME_AND_TAG') #e.g nickname#1234 
                #     obj.update({'YOUR_DISCORD_NAME_AND_TAG':stankonta1+int(bet/8)+1})
                    wincheck = 'You lost!'


                with open('./datafiles/balance.json','w') as balances:
                    json.dump(obj, balances)
                balances.close()

                embed2=discord.Embed(title=f"Roulette {ctx.message.author}")
                embed2.add_field(name="-", value=f"{slotL}", inline=True)
                embed2.add_field(name="⬇️", value=f"{slot1}", inline=True)
                embed2.add_field(name="-", value=f"{slotR}", inline=True)
                embed2.set_footer(text=f"Your balance: {obj.get(str(ctx.message.author))}")

                embed1=discord.Embed(title=f"Roulette {ctx.message.author}")
                embed1.add_field(name="-", value=f"<a:roulette:836696081994743879>", inline=True)
                embed1.add_field(name="⬇️", value=f"<a:roulette2:836697084266676274>", inline=True)
                embed1.add_field(name="-", value=f"<a:roulette:836696081994743879>", inline=True)
                embed1.set_footer(text=f"Your balance: ")

                msg = await ctx.send(embed=embed1)
                await asyncio.sleep(0.7)
                await msg.edit(embed=embed2)
        else:
            await ctx.send('There is no such color!')

    @commands.command(brief="Crash")
    async def crash(self, ctx, bet, multiplier):
        multiplier = float(multiplier)
        bet = int(bet)
        with open('./datafiles/balance.json', encoding='utf-8') as json_file:
            obj = json.load(json_file)
        # I have no idea what am I doing here but it kind of works as i expected it to work so its fine ig
        rndmultiplier = round(numpy.random.gamma(1.4,0.5),2)
        if rndmultiplier > 10: # Just in case 
            rndmultiplier = 10.0
        if rndmultiplier < 0:   
            rndmultiplier = 0.1
        stankonta = int(obj.get(str(ctx.message.author)))
        stankonta = float(stankonta)
        if bet > stankonta:
            await ctx.send(f'You don\'t have enough cash (but you can use {prefix}freemoney if you\'re totally broke though)')
        elif bet < 1:
            await ctx.send(f'Do. Not. Cheat. Please.')
        elif multiplier <= rndmultiplier:
            win = int(bet*multiplier)
            stankonta = int(stankonta)
            obj.update({str(ctx.message.author):stankonta+win})           
            embed=discord.Embed(title="Crash", description=f"You won {round(bet*multiplier,1)}", color=0x00ff08)
            embed.add_field(name="Crashed at:", value=f"{rndmultiplier}", inline=True)
            embed.add_field(name="Your multiplier:", value=f"{multiplier}", inline=True)
            embed.set_footer(text=f"Your balance: {obj.get(str(ctx.message.author))}")
            await ctx.send(embed=embed)
        elif multiplier > rndmultiplier:
            obj.update({str(ctx.message.author):stankonta-int(bet)})
            embed=discord.Embed(title="Crash", description="You lost", color=0xff0000)
            embed.add_field(name="Crashed at:", value=f"{rndmultiplier}", inline=True)
            embed.add_field(name="Your multiplier:", value=f"{multiplier}", inline=True)
            embed.set_footer(text=f"Your balance: {obj.get(str(ctx.message.author))}")
            await ctx.send(embed=embed)
            # if ctx.message.author.id != 252217902202093568:   # Uncomment those if you want to get some profit from other people's loses
            #     stankonta1 = obj.get('YOUR_DISCORD_NAME_AND_TAG') #e.g nickname#1234 
            #     obj.update({'YOUR_DISCORD_NAME_AND_TAG':stankonta1+int(bet/8)+1})
        with open('./datafiles/balance.json','w') as balances:
            json.dump(obj, balances)
        balances.close()
        

    @commands.command(brief="‎Top 5 gambling addicts of 2021")
    async def balancetop(self,ctx):
        with open('./datafiles/balance.json', encoding='utf-8') as f:
            gambling = json.load(f)
        marklist = sorted(gambling.items(), key=lambda item: item[1], reverse=True)
        sortdict = dict(marklist)
        # sort = json.dumps(sortdict, indent=0)
        bkeys = list(sortdict)
        bvalues = list(sortdict.values())
        embed=discord.Embed(title="Top 5")
        num = 0
        for i in range(5):
            if 0 <= num < len(bkeys):
                embed.add_field(name=f"{bkeys[num]}", value=f"{bvalues[num]}", inline=False)
            else:
                break
            num += 1
        await ctx.send(embed=embed)

    @commands.command(brief="")
    async def balance(self,ctx):
        with open('./datafiles/balance.json', encoding='utf-8') as json_file:
                obj = json.load(json_file)
        if len(ctx.message.mentions)>0:
            #embed=discord.Embed(title=str(ctx.message.mentions[0]), color=0xFF5733)
            await ctx.send(f"Account balance of {ctx.message.mentions[0]}: {obj.get(str(ctx.message.mentions[0]))}")
        else:
            await ctx.send(f"Your balance: {obj.get(str(ctx.message.author))}")
        
    @commands.command(brief="Give money to another user")
    async def transfer(self,ctx, amount=1):
        with open('./datafiles/balance.json', encoding='utf-8') as json_file:
            obj = json.load(json_file)
        stankonta1 = obj.get(str(ctx.message.author))
        stankonta2 = obj.get(str(ctx.message.mentions[0]))
        if amount > stankonta1:
            await ctx.send('You don\'t have enough money!')
        if amount < 0:
            await ctx.send('Why would you do that?')
        else:
            obj.update({str(ctx.message.author):stankonta1-amount})
            obj.update({str(ctx.message.mentions[0]):stankonta2+amount})
            with open('./datafiles/balance.json','w') as balances:
                json.dump(obj, balances)
            balances.close()    
            await ctx.send(f"Transferred {amount} to {ctx.message.mentions[0]}'s account")

    @commands.command(brief="Shop")
    async def shop(self,ctx, option=''):
        with open('./datafiles/balance.json', encoding='utf-8') as json_file:
            obj = json.load(json_file)
        stankonta = obj.get(str(ctx.message.author))
        if option == '': 
            # I did not translate those yet because I'm too lazy, but you get the point
            embed=discord.Embed(title="Shop", description=f"{prefix}sklep <opcja>", color=0x00a7b3)
            embed.add_field(name="1. Uzależnieniec...", value="100000", inline=True)
            embed.add_field(name="2. 5 pingów @everyone", value="25000", inline=True)
            embed.add_field(name="3. 5 pingów Sobiego", value="100", inline=True)
            embed.add_field(name="4. Autograf", value="10", inline=True)
            embed.set_footer(text=f"stan konta: {obj.get(str(ctx.message.author))}")
            await ctx.send(embed=embed)
        elif option == '1':
            price = 100000
            if price > stankonta:
                await ctx.send('You don\'t have enough cash')
            else:
                obj.update({str(ctx.message.author):stankonta-price})
                member = ctx.message.author
                role = discord.utils.get(member.guild.roles, name='Gambling addict')
                await member.add_roles(role)
        elif option == '2':
            price = 25000
            if price > stankonta:
                await ctx.send('You don\'t have enough cash')
            else:
                obj.update({str(ctx.message.author):stankonta-price})
                for i in range(5):
                    await ctx.send(f"{ctx.message.guild.default_role}  <:tf:805707103628951592>")
                    await asyncio.sleep(0.7)
        elif option == '3':
            price = 100
            if price > stankonta:
                await ctx.send('You don\'t have enough cash')
            else:
                obj.update({str(ctx.message.author):stankonta-price})
                for i in range(5):
                    await ctx.send('<@439848715264720896>')
                    await asyncio.sleep(0.7)
        elif option == '4':
            price = 10
            if price > stankonta:
                await ctx.send('You don\'t have enough cash')
            else:
                obj.update({str(ctx.message.author):stankonta-price})
                embed=discord.Embed(title="Mój autograf specjalnie dla ciebie :)")
                embed.set_image(url = 'https://i.imgur.com/pnNGFSw.png')
                await ctx.send(embed=embed)
        else:
            await ctx.send('There is no such an option here')

        with open('./datafiles/balance.json','w') as balances:
            json.dump(obj, balances)
        balances.close()


    @commands.command(brief="Free money wtf?")
    async def freemoney(self,ctx):
        with open('./datafiles/balance.json', encoding='utf-8') as json_file:
            obj = json.load(json_file)
        check = obj.get(str(ctx.message.author))
        if check == 0:
            obj.update({str(ctx.message.author):20})
            await ctx.send(':)')
        with open('./datafiles/balance.json','w') as balances:
                json.dump(obj, balances)
        balances.close()
        

def setup(client):
    client.add_cog(Casino(client))
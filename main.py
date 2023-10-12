import random, discord, logging, coloredlogs, os, pytz, threading
from flask import Flask, send_from_directory
from datetime import datetime
from discord import app_commands
from dotenv import load_dotenv

from upload.upload_cmd import *
from currency.currency_commands import *

logger = logging.getLogger("commands")
coloredlogs.install(level='DEBUG', fmt='%(asctime)s  |  %(message)s')

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
server = discord.Object(id=872557561172348978)
log_channel_id = 1161996311017553920
log_channel = None

port = 5500   # ikas hosti - 1203 ||| local hosti - 5500

load_dotenv()

app = Flask(__name__)

@app.route('/upload/files/<filename>')
def download_file(filename):
    return send_from_directory('upload/files', filename)

async def real_logger(interaction):
    log_channel = discord.utils.get(client.get_all_channels(), id=log_channel_id)

    if log_channel:
        tz_tbilisi = pytz.timezone('Asia/Tbilisi')
        now_tbilisi = datetime.now(tz_tbilisi)        

        embed=discord.Embed(title="Command Executed", color=0x0040ff)
        embed.add_field(name="Command", value=f"{interaction.data['name']}", inline=False)
        embed.add_field(name="Author", value=f"{interaction.user.display_name} ({interaction.user})", inline=True)
        embed.set_footer(text=f"{now_tbilisi.strftime('%H:%M:%S ||| %d/%m/%Y')}")

        await log_channel.send(embed=embed)
    else:
        print('Log channel not found.')

@client.event
async def on_ready():        
        #kai xalxi channel
        # await client.get_channel(1017852391388876901).connect()

        await tree.sync(guild=discord.Object(id=872557561172348978))

        logger.critical(f"Logged in as {client.user}")
        logger.critical(f"ID: {client.user.id}")
        logger.critical(f"Working on {len(client.guilds)} servers!")

        log_channel = discord.utils.get(client.get_all_channels(), id=log_channel_id)
        if log_channel:
            await log_channel.send(":white_check_mark: **გული მიცემს**")
        else:
            logger.error("Log channel not found. Check the channel ID.")

        await client.change_presence(status = discord.Status.idle, activity = discord.Game("Even if the world line changes, as long as you don't forget me, I'm there"))



@tree.command(name = "help", description = "informacia botze", guild=server)
async def help(interaction):
    embed=discord.Embed(title="Help - All the information about bot", description="Implemented files: `kaixalxi.py`, `AxaliDge.js`, `mines.py`, `currency.py`", color=0xffffff)
    embed.set_author(name="Kurisutina", icon_url="https://cdn.discordapp.com/avatars/895235026835365908/724404c34746afe0af9106af2eaaa8fc.png?size=4096")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/895235026835365908/724404c34746afe0af9106af2eaaa8fc.png?size=4096")

    embed.add_field(name="/help", value="this message", inline=False)
    embed.add_field(name="/denisa", value="info about denis", inline=True)
    embed.add_field(name="/zuka", value="info about zuka", inline=True)
    embed.add_field(name="/ikusha", value="info about ikusha", inline=True)
    embed.add_field(name="/begi", value="info about begi", inline=True)
    embed.add_field(name="/mine", value="mine game predictor", inline=True)
    embed.add_field(name="/time", value="time left till new day", inline=True)
    embed.add_field(name="/ping", value="client ping", inline=True)
    embed.add_field(name="Get_ID", value="right click on a person go in apps > Get_ID", inline=True)
    embed.add_field(name="/upload", value="upload any file and access it from a given link", inline=False)
    embed.add_field(name="/gambling", value="all the gambling commands", inline=False)

    await interaction.response.send_message(embed=embed)
    
    await real_logger(interaction)


@tree.command(name = "denisa", description = "informacia denisaze", guild=server)
async def denisa(interaction):
    embed=discord.Embed(title='denisas dedas shevecit me da bichebma', description="denisas dedasheveci movutkan dedismutlei magis kargi movtkan magis pirshi sheveci magis kargi movtkan magis dedsheveci magis gamcheni movtkan magis dzmis deda movtkan magis dzmis dzmis deda movtkan magis dedis qmris coli movtkan magis momavali qmris imitoro pedarastia kidev qmris deda movvtkan magis pirshi sheveci magis pirshi chavarwkie magis deda gavaqirave magis mamas kle movacheri da dedamis vachame magis babu gavatxove magis kargis trak movtkan da movutkan shvilebi magis karg mvotkan denisas mamas movutkan shvilebi da mkvdari shvili da denisas dzma romelic aseve mkvdaria magati kargic movtkan magati pirshi sheveci da im xes venacvale davpatije sadilze romelmac denisas dzma sheiwira chemi kai nikalai denisas mama gavafrine amerikashi LOL" , color=0xff0000)
    await interaction.response.send_message(embed=embed)
    
    await real_logger(interaction)


@tree.command(name = "zuka", description = "informacia zukaze", guild=server)
async def zuka(interaction):
    embed=discord.Embed(title="ZuKa", description="dziritadad cudad aris, ucnobia ratom, dzalian uyvars loli titqmis yoveldge tamashobs roca tavisufali dro aqvs. (dakavebuli ritia ar vicit) aseve man denisas dedas shesca (vin ar). meti ver movifiqret")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872561369801711676/955908622938959882/F13ADD6C-BF59-4C58-B74E-ABEBC7BC3D86.png")
    await interaction.response.send_message(embed=embed)
    
    await real_logger(interaction)


@tree.command(name = "ikushaa", description = "informacia ikushaze", guild=server)
async def ikusha(interaction):
    embed=discord.Embed(title="IkuShaa", description="ikusa aris dicktatori, ar uyvars japara imito ro chachyanebs, uyvars niggerebi, bambis krefa, taqsaoba. wona ucnobia. tan aqvs ylis roli es razec miutitebs tqventvitonac xvdebit. a xo da kide stakanchiki nayini evaseba", color=0xffa200)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872561369801711676/893997973569171496/image0.jpg")
    await interaction.response.send_message(embed=embed)
    
    await real_logger(interaction)


@tree.command(name = "begi", description = "informacia begize", guild=server)
async def begi(interaction):
    embed=discord.Embed(title="begi", description="autisti shacos maini, ar aqvs gadmocemis unari amitom umetesad tqven mogiwevt imis garkveva tu ras laparakosb, uyvars mecniereba da shaco, aseve uyvars botebis gaketeba rata daipyros discordi. kidev uyvars matematika magram matematikas sul aginebs. meti veraferi movifiqre imito ro mezareba yvelaferi xoda ki", color=0x860404)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872561369801711676/1159263728659861534/BEGIMAN.jpeg?ex=6530637a&is=651dee7a&hm=d6a31de6fd0cc670ac4df9bad73b0b6449dade832b6179f54d703d343b376431&")
    await interaction.response.send_message(embed=embed)
    
    await real_logger(interaction)


@tree.command(name = "mine", description="mine predictor", guild=server)
async def mine(interaction):
    mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:'
    a = random.randint(1, 8)
    b = random.randint(9, 13)
    c = random.randint(14, 17)
    d = random.randint(18, 25)
    if a == 1:
        mine1 = ":green_square: "
    elif a == 2:
        mine2 = ":green_square: "
    elif a == 3:
        mine3 = ":green_square: "
    elif a == 4:
        mine4 = ":green_square: "
    elif a == 5:
        mine5 = ":green_square: "
    elif a == 6:
        mine6 = ":green_square: "
    elif a == 7:
        mine7 = ":green_square: "
    elif a == 8:
        mine8 = ":green_square: "
    if b == 9:
        mine9 = ":green_square: "
    elif b == 10:
        mine10 = ":green_square: "
    elif b == 11:
        mine11 = ":green_square: "
    elif b == 12:
        mine12 = ":green_square: "
    elif b == 13:
        mine13 = ":green_square: "
    if c == 14:
        mine14 = ":green_square: "
    elif c == 15:
        mine15 = ":green_square: "
    elif c == 16:
        mine16 = ":green_square: "
    elif c == 17:
        mine17 = ":green_square: "
    if d == 18:
        mine18 = ":green_square: "
    elif d == 19:
        mine19 = ":green_square: "
    elif d == 20:
        mine20 = ":green_square: "
    elif d == 21:
        mine21 = ":green_square: "
    elif d == 22:
        mine22 = ":green_square: "
    elif d == 23:
        mine23 = ":green_square: "
    elif d == 24:
        mine24 = ":green_square: "
    elif d == 25:
        mine25 = ":green_square: "
    row1 = mine1 + mine2 + mine3 + mine4 + mine5
    row2 = mine6 + mine7 + mine8 + mine9 + mine10
    row3 = mine11 + mine12 + mine13 + mine14 + mine15
    row4 = mine16 + mine17 + mine18 + mine19 + mine20
    row5 = mine21 + mine22 + mine23 + mine24 + mine25
    info = str(random.randint(30, 99))

    await interaction.response.send_message(row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 +"\n" + row5 + "\n" + "**Accuracy (totally not fake)**" + "\n" + info +"%")

    await real_logger(interaction)


@tree.command(name="time", description="time left till the new day", guild=server)
async def time(interaction):
    tz_tbilisi = pytz.timezone('Asia/Tbilisi')
    now_tbilisi = datetime.now(tz_tbilisi)
    
    end_of_day_tbilisi = now_tbilisi.replace(hour=23, minute=59, second=59, microsecond=999)
    time_left_tbilisi = end_of_day_tbilisi - now_tbilisi
    hours, remainder = divmod(time_left_tbilisi.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    await interaction.response.send_message(f"ახალ დღემდე დარჩენილი დრო: `{hours}` **საათი**, `{minutes}` **წუთი**, `{seconds}` **წამი**..")

    await real_logger(interaction)


@tree.command(name = "ping", description="pong!", guild=server)
async def ping(interaction):
    await interaction.response.send_message(f"""```css
Ping: {round(client.latency * 1000)}ms```""")

    await real_logger(interaction)


@tree.context_menu(guild=server)
async def Get_ID(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f'{member.display_name}\'s ID: {member.id} ', ephemeral=True)

    await real_logger(interaction)


@tree.command(name="upload", description="ატვირთე ფაილი და გაუზიარე სხვებს ლინკით", guild=server)
@app_commands.describe(attachment='აირჩიე ასატვირთი ფაილი')
async def upload_func(interaction: discord.Interaction, attachment: discord.Attachment):
    await upload(interaction, attachment)

    await real_logger(interaction)


# CURRENCY

@tree.command(name="gambling", description="All the information about Gambling commands", guild=server)
async def gambling_command(interaction):
    await gambling_help(interaction)

    await real_logger(interaction)

@tree.command(name="bal", description="შენი ბალანსის შემოწმება", guild=server)
async def bal_command(interaction):
    await check_balance(interaction)

    await real_logger(interaction)


@tree.command(name="give", description="ფულის სხვა მომხმარებლისთვის მიცემა", guild=server)
async def give_command(interaction, user: discord.User, amount: int):
    await give_coins(interaction, user, amount)

    await real_logger(interaction)


@tree.command(name="coinflip", description="მონეტის აგდება", guild=server)
@app_commands.choices(choice=[
    app_commands.Choice(name='Heads', value='Heads'),
    app_commands.Choice(name='Tails', value='Tails'),
])
async def coin_command(interaction, choice: app_commands.Choice[str], amount: int):
    await coin_flip(interaction, choice, amount)

    await real_logger(interaction)


# @tree.command(name="daily", description="დღიური პრიზი", guild=server)
# async def daily_command(interaction):
#     await claim_daily(interaction)

#     logger.warning(f"[{interaction.user}] used /daily")

# CURRENCY















































def bot():
    client.run(os.getenv("TOKEN"))

def flask():
    app.run(host='0.0.0.0', port=port)

bot_thread = threading.Thread(target=bot)
flask_thread = threading.Thread(target=flask)

bot_thread.start()
flask_thread.start()
bot_thread.join()
flask_thread.join()
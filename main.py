import random, discord, logging, coloredlogs, os, pytz, threading, discord.ui
from flask import Flask, send_from_directory
from datetime import datetime
from discord import app_commands
from dotenv import load_dotenv

from upload.upload_cmd import *
from currency.currency_commands import *
from currency.db_funcs import *

logger = logging.getLogger("commands")
coloredlogs.install(level='DEBUG', fmt='%(asctime)s  |  %(message)s')

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
server = discord.Object(id=872557561172348978)
log_channel_id = 1161996311017553920
log_channel = None

tz_tbilisi = pytz.timezone('Asia/Tbilisi')
now_tbilisi = datetime.now(tz_tbilisi) 

port = 5500   # ikas hosti - 1203 ||| local hosti - 5500

load_dotenv()

app = Flask(__name__)

@app.route('/upload/files/<filename>')
def download_file(filename):
    return send_from_directory('upload/files', filename)

async def best_logger_eune(interaction):
    log_channel = discord.utils.get(client.get_all_channels(), id=log_channel_id)

    if log_channel:    
        await log_channel.send(f"`{now_tbilisi.strftime('%d/%m/%Y ||| %H:%M:%S')}` ==> **{interaction.user.display_name} ({interaction.user})** used **{interaction.data['name']}**")
    else:
        print('Log channel not found.')

@client.event
async def on_ready():        
        #kai xalxi channel
        # await client.get_channel(1017852391388876901).connect()

        await tree.sync(guild=server)

        logger.critical(f"Logged in as {client.user}")
        logger.critical(f"ID: {client.user.id}")
        logger.critical(f"Working on {len(client.guilds)} servers!")

        log_channel = discord.utils.get(client.get_all_channels(), id=log_channel_id)
        if log_channel:
            await log_channel.send(f"`{now_tbilisi.strftime('%d/%m/%Y ||| %H:%M:%S')}` ==> :white_check_mark: გული მიცემს!")
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
    
    await best_logger_eune(interaction)


@tree.command(name = "denisa", description = "informacia denisaze", guild=server)
async def denisa(interaction):
    embed=discord.Embed(title='denisas dedas shevecit me da bichebma', description="denisas dedasheveci movutkan dedismutlei magis kargi movtkan magis pirshi sheveci magis kargi movtkan magis dedsheveci magis gamcheni movtkan magis dzmis deda movtkan magis dzmis dzmis deda movtkan magis dedis qmris coli movtkan magis momavali qmris imitoro pedarastia kidev qmris deda movvtkan magis pirshi sheveci magis pirshi chavarwkie magis deda gavaqirave magis mamas kle movacheri da dedamis vachame magis babu gavatxove magis kargis trak movtkan da movutkan shvilebi magis karg mvotkan denisas mamas movutkan shvilebi da mkvdari shvili da denisas dzma romelic aseve mkvdaria magati kargic movtkan magati pirshi sheveci da im xes venacvale davpatije sadilze romelmac denisas dzma sheiwira chemi kai nikalai denisas mama gavafrine amerikashi LOL" , color=0xff0000)
    await interaction.response.send_message(embed=embed)
    
    await best_logger_eune(interaction)


@tree.command(name = "zuka", description = "informacia zukaze", guild=server)
async def zuka(interaction):
    embed=discord.Embed(title="ZuKa", description="dziritadad cudad aris, ucnobia ratom, dzalian uyvars loli titqmis yoveldge tamashobs roca tavisufali dro aqvs. (dakavebuli ritia ar vicit) aseve man denisas dedas shesca (vin ar). meti ver movifiqret")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872561369801711676/955908622938959882/F13ADD6C-BF59-4C58-B74E-ABEBC7BC3D86.png")
    await interaction.response.send_message(embed=embed)
    
    await best_logger_eune(interaction)


@tree.command(name = "ikushaa", description = "informacia ikushaze", guild=server)
async def ikusha(interaction):
    embed=discord.Embed(title="IkuShaa", description="ikusa aris dicktatori, ar uyvars japara imito ro chachyanebs, uyvars niggerebi, bambis krefa, taqsaoba. wona ucnobia. tan aqvs ylis roli es razec miutitebs tqventvitonac xvdebit. a xo da kide stakanchiki nayini evaseba", color=0xffa200)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872561369801711676/893997973569171496/image0.jpg")
    await interaction.response.send_message(embed=embed)
    
    await best_logger_eune(interaction)


@tree.command(name = "begi", description = "informacia begize", guild=server)
async def begi(interaction):
    embed=discord.Embed(title="begi", description="autisti shacos maini, ar aqvs gadmocemis unari amitom umetesad tqven mogiwevt imis garkveva tu ras laparakosb, uyvars mecniereba da shaco, aseve uyvars botebis gaketeba rata daipyros discordi. kidev uyvars matematika magram matematikas sul aginebs. meti veraferi movifiqre imito ro mezareba yvelaferi xoda ki", color=0x860404)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/872561369801711676/1159263728659861534/BEGIMAN.jpeg?ex=6530637a&is=651dee7a&hm=d6a31de6fd0cc670ac4df9bad73b0b6449dade832b6179f54d703d343b376431&")
    await interaction.response.send_message(embed=embed)
    
    await best_logger_eune(interaction)


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

    await best_logger_eune(interaction)


@tree.command(name="time", description="time left till the new day", guild=server)
async def time(interaction):
    tz_tbilisi = pytz.timezone('Asia/Tbilisi')
    now_tbilisi = datetime.now(tz_tbilisi)
    
    end_of_day_tbilisi = now_tbilisi.replace(hour=23, minute=59, second=59, microsecond=999)
    time_left_tbilisi = end_of_day_tbilisi - now_tbilisi
    hours, remainder = divmod(time_left_tbilisi.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    await interaction.response.send_message(f"ახალ დღემდე დარჩენილი დრო: `{hours}` **საათი**, `{minutes}` **წუთი**, `{seconds}` **წამი**..")

    await best_logger_eune(interaction)


@tree.command(name = "ping", description="pong!", guild=server)
async def ping(interaction):
    await interaction.response.send_message(f"""```css
Ping: {round(client.latency * 1000)}ms```""")

    await best_logger_eune(interaction)


@tree.context_menu(guild=server)
async def Get_ID(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f'{member.display_name}\'s ID: {member.id} ', ephemeral=True)

    await best_logger_eune(interaction)


@tree.command(name="upload", description="ატვირთე ფაილი და გაუზიარე სხვებს ლინკით", guild=server)
@app_commands.describe(attachment='აირჩიე ასატვირთი ფაილი')
async def upload_func(interaction: discord.Interaction, attachment: discord.Attachment):
    await upload(interaction, attachment)

    await best_logger_eune(interaction)


# CURRENCY

@tree.command(name="gambling", description="All the information about Gambling commands", guild=server)
async def gambling_command(interaction):
    await gambling_help(interaction)

    await best_logger_eune(interaction)

@tree.command(name="bal", description="შენი ბალანსის შემოწმება", guild=server)
async def bal_command(interaction):
    await check_balance(interaction)

    await best_logger_eune(interaction)


@tree.command(name="give", description="ფულის სხვა მომხმარებლისთვის მიცემა", guild=server)
async def give_command(interaction, user: discord.User, amount: int):
    await give_coins(interaction, user, amount)

    await best_logger_eune(interaction)


@tree.command(name="coinflip", description="მონეტის აგდება", guild=server)
@app_commands.choices(choice=[
    app_commands.Choice(name='Heads', value='Heads'),
    app_commands.Choice(name='Tails', value='Tails'),
])
async def coin_command(interaction, choice: app_commands.Choice[str], amount: int):
    await coin_flip(interaction, choice, amount)

    await best_logger_eune(interaction)


case_choices = {
    "STREAMER": "STREAMER",
    "GAMER": "GAMER",
    "SCIENTIST": "SCIENTIST",
    "EXPLORER": "EXPLORER",
    "ARTIST": "ARTIST",
    "CHEF": "CHEF",
    "ARTIST": "ARTIST",
    "DETECTIVE": "DETECTIVE",
    "WRITER": "WRITER",
    "PSYCHOLOGIST": "PSYCHOLOGIST",
}
@tree.command(name="open", description="სკივრის გახსნა", guild=server)
@app_commands.choices(case_choice=[app_commands.Choice(name=name, value=value) for name, value in case_choices.items()])
async def case_opening(interaction, case_choice: app_commands.Choice[str]):
    await open_case(interaction, case_choice)

    await best_logger_eune(interaction)


@tree.command(name="cases", description="ხელმისაწვდომი სკივრები თავიანთი ნივთებით და მათი ფასებით", guild=server)
async def cases_command(interaction):
    await case_list(interaction)

    await best_logger_eune(interaction)




# @tree.command(name="daily", description="დღიური პრიზი", guild=server)
# async def daily_command(interaction):
#     await claim_daily(interaction)

#     logger.warning(f"[{interaction.user}] used /daily")

# CURRENCY

# Dictionary to store the game state for each user
blackjack_games = {}

# Class for a Blackjack game
class BlackjackGame:
    def __init__(self, user_id, bet_amount):
        self.user_id = user_id
        self.state = "playing"
        self.user_cards = [self.draw_card(), self.draw_card()]
        self.dealer_card = self.draw_card()
        self.dealer_cards = [self.dealer_card]
        self.bet_amount = bet_amount

    def draw_card(self):
        return random.choice(["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])

    def is_bust(self):
        user_hand_value = self.calculate_hand_value(self.user_cards)
        return user_hand_value > 21

    def calculate_hand_value(self, cards):
        value = 0
        num_aces = 0  # To keep track of the number of Aces in the hand
        print(cards)
        for card in cards:
            if card in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                value += int(card)
            elif card in ["J", "Q", "K"]:
                value += 10
            elif cards[-1] == "A":
                num_aces += 1
                value += 11  # Initially, count Aces as 11
        # Handle Aces to avoid busting
        while num_aces > 0 and value > 21:
            num_aces=0
            value -= 10  # Change the value of an Ace from 11 to 1

        return value


    def determine_winner(self):
        user_hand_value = self.calculate_hand_value(self.user_cards)
        dealer_hand_value = self.calculate_hand_value(self.dealer_cards)
        #print(user_hand_value,dealer_hand_value)
        #print("blacjack_games",blackjack_games[self.user_id])
        if user_hand_value > 21:
            return "dealer"
        elif dealer_hand_value > 21:
            return "user"
        elif user_hand_value > dealer_hand_value:
            return "user"
        elif user_hand_value < dealer_hand_value:
            return "dealer"
        else:
            return "push"

# Function to create the main game embed with buttons
def create_game_embed(game,user_id=None):
    embed = discord.Embed(title="Blackjack Game")
    embed.add_field(name="Your Cards", value=", ".join(game.user_cards))
    embed.add_field(name="Current Hand Value", value=str(game.calculate_hand_value(game.user_cards)))
    embed.add_field(name="Dealer's Face-up Card", value=game.dealer_card)
    embed.set_footer(text=f"Bet Amount: {game.bet_amount} ₾")
    new_balance = get_balance(user_id) - game.bet_amount

    if game.state == "playing":
        embed.add_field(name="Choose Your Action", value="Click the buttons below:")
    elif game.state == "dealer_turn":
        embed.add_field(name="Dealer's Hand", value=", ".join(game.dealer_cards))
        embed.add_field(name="Dealer's Hand Value", value=str(game.calculate_hand_value(game.dealer_cards)))
    else:
        del blackjack_games[user_id] # Vshlit Motamashes Blackjack array dan
        embed.add_field(name="Game Over", value=f"You {game.state}!")
        return embed, 0 # Anu wavaget

    return embed, 1 # Ganvagrzot

# Command to start a new Blackjack game
@tree.command(
    name="bj",
    description="Start a Blackjack game",
    guild=server
)
async def bj_command(interaction, amount: int):
    user_id = interaction.user.id

    if amount <= 0:
        await interaction.response.send_message("Please bet a positive amount.")
        return

    if get_balance(user_id) < amount:
        await interaction.response.send_message("You don't have enough balance to bet that amount.")
        return

    if user_id in blackjack_games:
        if not blackjack_games[user_id].state == "playing":
            del blackjack_games[user_id]
        else:
            await interaction.response.send_message("You already have an active Blackjack game. Finish that one first.")
            return

    # Start a new game for the user
    game = BlackjackGame(user_id, amount)
    blackjack_games[user_id] = game

    # Create the main game embed with buttons
    embed, c = create_game_embed(game,user_id)
    if not c:
        await interaction.response.send_message(
            content="Game ended!",
            embed=embed,
            view=callback()
        )
        return
    await interaction.response.send_message(
        content="Game started!",
        embed=embed,
        view=callback()
    )

# Event listener for button interactions
class callback(discord.ui.View):
    logger.debug(f"button has been pressed")

    @discord.ui.button(label="Hit", style=discord.ButtonStyle.primary)
    async def hit_callback(self, interaction,button):
        await hit_command(interaction)

    @discord.ui.button(label="Stand", style=discord.ButtonStyle.secondary)
    async def stand_callback(self, interaction,button):
        await stand_command(interaction)

    @discord.ui.button(label="Fold", style=discord.ButtonStyle.danger)
    async def fold_callback(self, interaction,button):
        await fold_command(interaction)


# Command to hit during a Blackjack game
async def hit_command(interaction):
    user_id = interaction.user.id

    if user_id not in blackjack_games:
        await interaction.response.send_message("You don't have an active Blackjack game. Start one with /bj.")
        return
    game = blackjack_games[user_id]
    winner = game.determine_winner()
    print(winner)
    hand_value = game.calculate_hand_value(game.user_cards)

    # Draw a card for the user
    embed,c = create_game_embed(game,user_id)
    embed.add_field(name="\u200b", value="\u200b")
    if game.state == "playing":
        # Draw a card for the user
        new_card = game.draw_card()
        game.user_cards.append(new_card)

        if game.is_bust():
            game.state = "dealer_turn"

        # Update the main game embed with buttons
        embed,c = create_game_embed(game,user_id)
        if hand_value == 21:
            new_balance = get_balance(user_id) + (2 * game.bet_amount)  # User wins double their bet
            update_balance(user_id, new_balance)
            del blackjack_games[user_id]

            embed.add_field(name="Results", value=f"Congratulations! You won {2 * game.bet_amount} ₾.")
            print(str(game))
            await interaction.response.edit_message(
                embed=embed,
                view=callback()
            )
            return
        elif hand_value > 21:
            new_balance = get_balance(user_id) - game.bet_amount  # User loses their bet
            update_balance(user_id, new_balance)
            del blackjack_games[user_id]
            embed.add_field(name="Results", value=f"Sorry, you lost {game.bet_amount} ₾ to the dealer.")
            print(str(game))
            await interaction.response.edit_message(
                embed=embed,
                view=callback()
            )
            return
        print(str(game))
        await interaction.response.edit_message(
            embed=embed,
            view=callback()
        )

# Command to stand during a Blackjack game
async def stand_command(interaction):
    user_id = interaction.user.id

    if user_id not in blackjack_games:
        await interaction.response.send_message("You don't have an active Blackjack game. Start one with /bj.")
        return

    game = blackjack_games[user_id]

    if game.state == "playing":
        game.state = "dealer_turn"
        print(game.dealer_cards,game)
        # Dealer's turn logic
        while game.calculate_hand_value(game.dealer_cards) < 17:
            new_card = game.draw_card()
            game.dealer_cards.append(new_card)

        # Determine the winner
        winner = game.determine_winner()

        if winner == "user":
            # User won, update their balance and send a message
            new_balance = get_balance(user_id) + (2 * game.bet_amount)  # User wins double their bet
            update_balance(user_id, new_balance)
            await interaction.response.send_message(f"Congratulations! You won {2 * game.bet_amount} ₾.")
        elif winner == "dealer":
            # Dealer won, update their balance and send a message
            new_balance = get_balance(user_id) - game.bet_amount  # User loses their bet
            update_balance(user_id, new_balance)
            await interaction.response.send_message(f"Sorry, you lost {game.bet_amount} ₾ to the dealer.")
        else:
            # It's a push, return the bet amount to the user
            new_balance = get_balance(user_id) + game.bet_amount  # User gets their bet amount back
            update_balance(user_id, new_balance)
            await interaction.response.send_message(f"It's a push! You get your {game.bet_amount} ₾ back.")

        del blackjack_games[user_id]  # Remove the game from the dictionary

        # Update the main game embed with the final result
        embed,c = create_game_embed(game,user_id)
        await interaction.response.edit_message(embed=embed)
    else:
        del blackjack_games[user_id]
        await interaction.response.send_message("Your game is already over.")

# Command to fold during a Blackjack game
async def fold_command(interaction):
    user_id = interaction.user.id

    if user_id not in blackjack_games:
        await interaction.response.send_message("You don't have an active Blackjack game. Start one with /bj.")
        return

    game = blackjack_games[user_id]

    if game.state == "playing":
        game.state = "folded"

        # Implement logic for folding and determine the winner
        # ...

        winner = "dealer"  # The dealer wins by default

        if winner == "dealer":
            # Dealer won, update their balance and send a message
            current_balance = get_balance(user_id)
            new_balance = current_balance - game.bet_amount
            update_balance(user_id, new_balance)
            await interaction.response.send_message(f"You folded. You lost {game.bet_amount} ₾. Your new balance is {new_balance} ₾.")
        #del blackjack_games[user_id]  # Remove the game from the dictionary

        # Update the main game embed with the final result
        embed,c = create_game_embed(game,user_id)
        await interaction.response.edit_message(embed=embed)
    else:
        del blackjack_games[user_id]
        await interaction.response.send_message("Your game is already over.")











































# https://guide.pycord.dev/interactions/ui-components/buttons


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
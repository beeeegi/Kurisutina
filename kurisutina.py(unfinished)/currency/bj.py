import random, discord
from discord import app_commands
from currency.db_funcs import *
##########################################################
##########################################################
##########################################################
################# TEMPORARILY FREEZED ####################
##########################################################
##########################################################
##########################################################
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

# CREATING A COMMAND FOR BLACKJACK
async def bj_command(interaction, amount: int):
    user_id = interaction.user.id
    await best_logger_eune(interaction)

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






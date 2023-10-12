import random, discord
from currency.db_funcs import *


async def gambling_help(interaction):
    user_id = interaction.user.id
    definition(user_id)

    embed=discord.Embed(title="Gambling - All the information about Gambling commands",color=0xffffff)
    embed.set_author(name="Kurisutina", icon_url="https://cdn.discordapp.com/avatars/895235026835365908/724404c34746afe0af9106af2eaaa8fc.png?size=4096")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/895235026835365908/724404c34746afe0af9106af2eaaa8fc.png?size=4096")
    embed.add_field(name="/bal", value="შენი ბალანსის შემოწმება", inline=True)
    embed.add_field(name="/give", value="ფულის სხვა მომხმარებლისთვის მიცემა", inline=True)
    embed.add_field(name="/coinflip", value="მონეტის აგდება 2x პრიზის მოსაგებად", inline=True)

    await interaction.response.send_message(embed=embed)
    


async def check_balance(interaction):
    user_id = interaction.user.id
    definition(user_id)

    user_id = interaction.user.id

    balance = get_balance(user_id)

    embed = discord.Embed(title=f"შენი ბალანსი: {balance} ₾.", color=0x00ff11)
    await interaction.response.send_message(embed=embed)


async def give_coins(interaction, user: discord.User, amount):
    user_id = interaction.user.id
    definition(user_id)
    definition(user.id)
    
    user_id = interaction.user.id

    if amount > 0:

        sender_balance = get_balance(user_id)
        receiver_balance = get_balance(user.id)

        if amount <= sender_balance:
            sender_balance -= amount
            receiver_balance += amount

            update_balance(user_id, sender_balance)
            update_balance(user.id, receiver_balance)

            embed = discord.Embed(title=f"შენ მიეცი {amount} ₾ {user.display_name}-ს.", color=0xbaff52)
            embed.add_field(name="შენი ბალანსია: ", value=f"{sender_balance} ₾")
            embed.add_field(name=f"მიმღების ბალანსია: ", value=f"{receiver_balance} ₾")

            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="თქვენ არ გაქვს საკმარისი ბალანსი ამ ოპერაციის შესასრულებლად.", color=0xff0000)
            await interaction.response.send_message(embed=embed)



async def coin_flip(interaction, choice, amount):
    user_id = interaction.user.id
    definition(user_id)

    user_id = interaction.user.id

    if amount > 0 and amount <= get_balance(user_id):
        coin_result = random.choice(["Heads", "Tails"])

        if choice.value == coin_result:
            winnings = amount * 2
            outcome = "მოიგე"
        else:
            winnings = -amount
            outcome = "წააგე"

        new_balance = get_balance(user_id) + winnings
        update_balance(user_id, new_balance)

        embed = discord.Embed(
            title=f"ამოვიდა {coin_result}.",
            description=f"შენ {outcome} {abs(winnings)} ₾",
            color=0xbaff52 if outcome == "მოიგე" else 0xff0000
        )
        embed.add_field(name="შენი ახალი ბალანსი", value=new_balance)

        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="შენ არ გაქვს საკმარისი ბალანსი ამ ოპერაციის შესასრულებლად.", color=0xff0000)
        await interaction.response.send_message(embed=embed)









# async def claim_daily(interaction: discord.Interaction):
#     user_id = interaction.user.id

#     # axlandeli dro
#     current_time = datetime.now()
#     # daresetebis dro
#     next_reset_time = current_time.replace(hour=reset_time.hour, minute=reset_time.minute, second=reset_time.second)

#     # saatis gamotvla
#     time_difference = (next_reset_time - current_time).total_seconds() / 3600

#     if user_id in user_balances:
#         if time_difference <= 0:
#             prize = random.randint(100, 1000)
#             user_balances[user_id] += prize
#             balance = user_balances[user_id]

#             embed = discord.Embed(title=f"გილოცავ! შენ მოიგე {prize} ლარი.", color=0xecb94b)
#             embed.add_field(name="ახალი ბალანსი", value=f"{balance} ლარი", inline=False)
#             embed.set_footer(text=f"შემდეგი ცდის უფლება გექნებათ: {time_difference:.1f} საათში")
            
#             await interaction.response.send_message(embed=embed)
#         else:
#             embed = discord.Embed(title=f"წარმატებები შემდეგში :დ", color=0xff0000)
#             embed.set_footer(text=f"შემდეგი ცდის უფლება გექნებათ: {time_difference:.1f} საათში")
#             await interaction.response.send_message(embed=embed)
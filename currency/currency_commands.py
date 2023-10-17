import random, discord, logging, coloredlogs, json
from currency.db_funcs import *

logger = logging.getLogger("commands")
coloredlogs.install(level='DEBUG', fmt='%(asctime)s  |  %(message)s')

file_path = 'currency\cases.json'

with open(file_path, 'r', encoding='utf-8') as file:
    case_choices = json.load(file)

async def gambling_help(interaction):
    user_id = interaction.user.id
    definition(user_id)

    embed=discord.Embed(title="Gambling - All the information about Gambling commands",color=0xffffff)
    embed.set_author(name="Kurisutina", icon_url="https://cdn.discordapp.com/avatars/895235026835365908/724404c34746afe0af9106af2eaaa8fc.png?size=4096")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/895235026835365908/724404c34746afe0af9106af2eaaa8fc.png?size=4096")
    embed.add_field(name="/bal", value="შენი ბალანსის შემოწმება", inline=True)
    embed.add_field(name="/give", value="ფულის სხვა მომხმარებლისთვის მიცემა", inline=True)
    embed.add_field(name="/coinflip", value="მონეტის აგდება 2x პრიზის მოსაგებად", inline=True)
    embed.add_field(name="/cases", value="ხელმისაწვდომი სკივრები თავიანთი ნივთებით და მათი ფასებით", inline=True)
    embed.add_field(name="/open", value="სკივრის გახსნა", inline=True)

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
            winnings = +amount
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
        embed.set_footer(text=f"შენი ახალი ბალანსი: {new_balance} ₾")

        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="შენ არ გაქვს საკმარისი ბალანსი ამ ოპერაციის შესასრულებლად.", color=0xff0000)
        embed.set_footer(text=f"შენი ბალანსია: {new_balance} ₾")
        await interaction.response.send_message(embed=embed)


async def case_list(interaction):
    user_id = interaction.user.id
    definition(user_id)
    description = "ხელმისაწვდომი სკივრები თავიანთი ნივთებით:\n\n"

    for case_name, case_info in case_choices.items():
        description += f"**{case_info['name']}** -> {case_info['cost']} ₾\n"
        description += "ნივთები:\n"

        for item, value in case_info['items'].items():
            description += f"- **{item}**: {value} ₾\n"

        description += "\n"

    embed = discord.Embed(
        title="სკივრები და ნივთები",
        description=description,
        color=0xffffff
    )

    await interaction.response.send_message(embed=embed)


async def open_case(interaction, case_choice):
    user_id = interaction.user.id
    definition(user_id)
    case_choice_str = case_choice.value

    if case_choice_str not in case_choices:
        embed = discord.Embed(title="არასწორი არჩევანი, ცადე ხელახლა", color=0xff0000)
        await interaction.response.send_message(embed=embed)
        return

    if get_balance(user_id) < case_choices[case_choice_str]["cost"]:
        embed = discord.Embed(title="შენ არ გაქვს საკმარისი ბალანსი ამ ოპერაციის შესასრულებლად.", color=0xff0000)
        embed.set_footer(text=f"შენი ბალანსია: {new_balance} ₾")
        await interaction.response.send_message(embed=embed)
        return

    current_balance = get_balance(user_id)
    new_balance = current_balance - case_choices[case_choice_str]["cost"]
    update_balance(user_id, new_balance)

    items = list(case_choices[case_choice_str]["items"].keys())
    weights = list(case_choices[case_choice_str]["items"].values())

    # shansebis gansazgvra
    probability_positive = 0.4  # dadebiti values mqone itemis dagdebis shansi (1 == 100%)
    probability_negative = 1 - probability_positive

    # weights cvlis shansebis mixedvit
    total_positive_weights = sum(w for w in weights if w > 0)
    total_negative_weights = sum(w for w in weights if w < 0)

    for i, item_value in enumerate(case_choices[case_choice_str]["items"].values()):
        if item_value > 0:
            weights[i] *= (probability_positive / total_positive_weights)
        else:
            weights[i] *= (probability_negative / total_negative_weights)

    # irchevs random items weightis mixedvit
    item = random.choices(items, weights=weights, k=1)[0]
    item_value = case_choices[case_choice_str]["items"][item]
    new_balance += item_value
    update_balance(user_id, new_balance)

    if item_value >= 0:
        embed_color = 0x00ff00  # mwvane dadebitze
    else:
        embed_color = 0xff0000  # witeli uaryofitze

    embed = discord.Embed(title="სკივრი  <:chest:1162333484409434162>  ნივთი", color=embed_color)
    embed.add_field(name=case_choices[case_choice_str]['name'], value=f"{case_choices[case_choice_str]['cost']} ₾", inline=True)
    embed.add_field(name=item, value=f"{item_value} ₾", inline=True)
    embed.set_footer(text=f"შენი ახალი ბალანსი: {new_balance} ₾")

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
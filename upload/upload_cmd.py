import discord, os, logging, coloredlogs, pytz
from datetime import datetime

logger = logging.getLogger("commands")
coloredlogs.install(level='DEBUG', fmt='%(asctime)s  |  %(message)s')

link = 'localhost:5500'  # localhost:5500 ||| 46.190.43.192:1203

async def upload(interaction: discord.Interaction, attachment: discord.Attachment):
    filename = attachment.filename
    size_bytes = attachment.size
    size_mbs = size_bytes / (1024 * 1024)

    upload_dir = 'upload/files'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file_path = os.path.join(upload_dir, filename)

    file_content = await attachment.read()

    with open(file_path, 'wb') as file:
        file.write(file_content)
        logger.warning(f"[{interaction.user}]'s file has been uploaded!")

    tz_tbilisi = pytz.timezone('Asia/Tbilisi')
    now_tbilisi = datetime.now(tz_tbilisi)

    embed = discord.Embed(title="გმადლობთ ატვირთვისთვის", color=0x11ff00)
    embed.set_author(name="Kurisutina", icon_url="https://cdn.discordapp.com/avatars/895235026835365908/724404c34746afe0af9106af2eaaa8fc.png?size=4096")
    embed.add_field(name="ფაილის სახელი", value=f"{filename}", inline=False)
    embed.add_field(name="ფაილის ზომა", value=f"{size_mbs:.2f} MB", inline=False)
    embed.set_footer(text=f"{now_tbilisi.strftime('%H:%M:%S ||| %d/%m/%Y')}")

    await interaction.response.send_message(embed=embed)
    await interaction.followup.send(f"გადმოსაწერი ლინკი: http://{link}/{upload_dir}/{filename}", ephemeral=True)
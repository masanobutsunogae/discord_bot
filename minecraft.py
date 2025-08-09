import os
import discord
from discord.ext import commands
from mcrcon import MCRcon

# 環境変数から読み込み
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
RCON_HOST = os.getenv("RCON_HOST")  # 例: c0desv2025.f5.si
RCON_PORT = int(os.getenv("RCON_PORT", 25575))
RCON_PASSWORD = os.getenv("RCON_PASSWORD")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def whitelist(ctx, player_name: str):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("権限がありません。")
        return

    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            response = mcr.command(f"whitelist add {player_name}")
            await ctx.send(f"ホワイトリスト追加結果: {response}")
    except Exception as e:
        await ctx.send(f"エラーが発生しました: {e}")

bot.run(DISCORD_TOKEN)

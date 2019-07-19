import discord

TOKEN = "NjAxNzg1Mzc3NTkzNzUzNjAx.XTHWUg.zCn4jkCtEld3MrvlKX10NRWHTy0"      # Put your Bot token here
SKIP_BOTS = False


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in!')
    for member in client.get_all_members():
        if member.bot and SKIP_BOTS:
            continue
        await member.ban(reason="cuz I want you dickhead!!", delete_message_days=7)
        print(f"Banned {member.display_name}!")
    print("Banning is complete!")

client.run(TOKEN)

import discord
import os

async def send_discord_message(message_content):
    token = os.environ.get("BOT_KEY")
    if not token:
        print("Error: Discord token not found.")
        return

    # Discord-Client initialisieren
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f"We have logged in as {client.user}")

        # Kanal oder Benutzer finden, an den die Nachricht gesendet werden soll (hier wird der erste gefundene Kanal verwendet)
        channel = None
        for guild in client.guilds:
            for c in guild.channels:
                if isinstance(c, discord.TextChannel):
                    channel = c
                    break
            if channel:
                break

        # Nachricht senden
        if channel:
            await channel.send(message_content)
            print("Message sent successfully.")
        else:
            print("Error: No text channels found in any guilds.")

        await client.close()


    message_content = "Dies ist eine Testnachricht von GitHub Actions!"
    await send_discord_message(message_content)

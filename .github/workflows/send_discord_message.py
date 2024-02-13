import discord
import os

async def send_discord_message(message_content):
    # Token des Discord-Bots aus den Umgebungsvariablen laden
    token = os.environ.get("BOT_KEY")
    if not token:
        print("Error: Discord token not found.")
        return

    # ID des Zielkanals
    target_channel_id = '1145979711097426001'

    # Discord-Client initialisieren
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f"We have logged in as {client.user}")

        # Kanal mit der Ziel-ID finden
        channel = client.get_channel(int(target_channel_id))

        # Nachricht senden
        if channel:
            await channel.send(message_content)
            print("Message sent successfully.")
        else:
            print("Error: Channel not found.")

        await client.close()

    # Beispielaufruf des Skripts mit einer Nachricht
    message_content = "Dies ist eine Testnachricht von GitHub Actions!"
    await send_discord_message(message_content)

# Den Discord-Client starten
client.run(token)


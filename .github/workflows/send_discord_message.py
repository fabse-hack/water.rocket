import discord
import os
import asyncio

async def send_discord_message(message_content):
    token = os.environ.get("DISCORD_TOKEN")
    if not token:
        print("Fehler: Discord-Token nicht gefunden.")
        return

    target_channel_id = '1145979711097426001'

    client = discord.Client()

    @client.event
    async def on_ready():
        print(f"Eingeloggt als {client.user}")

        channel = client.get_channel(int(target_channel_id))
        if channel:
            await channel.send(message_content)
            print("Nachricht erfolgreich gesendet.")
        else:
            print("Fehler: Kanal nicht gefunden.")

        await client.close()

    await client.start(token)  # Starte den Client hier

async def main():
    message_content = "Dies ist eine Testnachricht von GitHub Actions!"
    await send_discord_message(message_content)
    
asyncio.run(main())


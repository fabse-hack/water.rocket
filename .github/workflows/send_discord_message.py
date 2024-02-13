import discord
import os

async def send_discord_message(message_content):
    token = os.environ.get("BOT_KEY")
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

    await send_discord_message(message_content)
    client.run(token)

message_content = "Dies ist eine Testnachricht von GitHub Actions!"
send_discord_message(message_content)


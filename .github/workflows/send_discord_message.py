import discord
import os
import asyncio

async def send_discord_message(message_content):
    token = os.environ.get("DISCORD_TOKEN")
    target_channel_id = '1145979711097426001'

    client = discord.Client()

    @client.event
    async def on_ready():

        channel = client.get_channel(int(target_channel_id))
        channel:
          await channel.send(message_content)

        await client.close()

    await client.start(token)

async def main():
    message_content = "Ein neuer Commit ist eingegangen auf https://github.com/fabse-hack/water.rocket"
    await send_discord_message(message_content)
    
asyncio.run(main())


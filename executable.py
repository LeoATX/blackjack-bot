import discord
import datetime
import socket


class BotClient(discord.Client):
    async def on_ready(self):
        print("{user} ready".format(user=self.user))

        user = await self.fetch_user(310896163865755649)
        await user.send(str(datetime.datetime.now()) + "\n" + socket.gethostbyname(socket.gethostname()))

    async def on_message(self, payload):
        # First check for self
        if payload.author == self.user:
            return

        if payload.author.id == 416415123402653697:
            modified = ''
            for character in payload.content:
                if character == 'H':
                    modified += 'J'
                elif character == 'h':
                    modified += 'j'
                else:
                    modified += character
            await payload.channel.send(modified)

        if payload.content == 'socket':
            await payload.channel.send(socket.gethostbyname(socket.gethostname()))


print("Input token")
token = input()
BotClient().run(token)

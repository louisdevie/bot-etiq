import discord


class Bot:
    def __init__(self, client):
        self.__client = client

    async def command(self, command, *arguments, message):
        match command:
            case "deco":
                if (
                    message.author.name == "louisdevie"
                    and message.author.discriminator == "9781"
                ):
                    self.__client.logout()

            case "ping":
                await message.channel.send("pong")

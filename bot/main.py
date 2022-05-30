import os
import discord
import config, bot, uils


class BotClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__bot = bot.Bot(self)

    async def on_ready(self):
        print(f"Connecté en tant que {self.user} !")

    async def on_disconnect(self):
        print("Bot déconnecté.")

    async def on_message(self, message):
        if (message.author != self.user) and message.content.startswith(config.PREFIX):
            await self.__bot.command(
                *utils.split_command(message.content),
                message=message,
            )


if __name__ == "__main__":
    BotClient().run(os.environ["TOKEN"])

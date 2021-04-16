import loadenv
import discord  # noqa
import deck
import hand


# Discord permissions should be 4294967287
class BotClient(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)

        # Game embed
        self.box = self.box = discord.Embed(title="Blackjack\n\n\u200b",
                                            colour=discord.Colour(0).from_rgb(200, 200, 200))

        # Game attributes
        self.deck = None
        self.house = None
        self.player = None
        # Player's second hand
        self.player2 = None

        self.game_start_message = None

    async def on_ready(self):
        print("{user} ready".format(user=self.user))

    async def on_message(self, payload):
        # First check for self
        if payload.author == self.user:
            return

        # This starts the blackjack game
        if payload.content == '$blackjack':
            # populates the embed
            self.box.clear_fields()
            self.box.add_field(name="\u200b", value="Every game uses a 52 card deck.\n"
                                                    "Dealer stands on soft 17.")

            game_start_message = await payload.channel.send(content='\u200b', embed=self.box)
            self.game_start_message = game_start_message
            await game_start_message.add_reaction('👍')

    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.user.id:
            return

        # When the game start embed has been reacted to
        # Starts the game
        if payload.message_id == self.game_start_message.id and payload.emoji.name == '👍':
            # Initiate the game attributes
            self.deck = deck.Deck()
            self.house = hand.Hand()
            self.player = hand.Hand()

            # Draw the cards
            self.house.add(self.deck.draw())
            self.player.add(self.deck.draw())
            self.house.add(self.deck.draw())
            self.player.add(self.deck.draw())

            # Populates the embed
            self.box.clear_fields()
            self.box.add_field(name="Dealer hand", value=("[" + self.house.card(0) + "] [?]"), inline=False)
            self.box.add_field(name="Your hand", value=self.player.return_hand())
            await self.get_channel(payload.channel_id).send(content='\u200b', embed=self.box)

            # Immediately check for blackjack after drawing cards
            if self.player.total() == 21:
                self.box.clear_fields()
                self.box.add_field(name="Blackjack!", value='\u200b')
                await self.get_channel(payload.channel_id).send(content='\u200b', embed=self.box)


env = loadenv.Env()
key = env.getenv('FACT_CHECKER_TOKEN')
BotClient().run(key)

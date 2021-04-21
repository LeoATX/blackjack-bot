import loadenv
import discord  # noqa
import deck
import hand

# git branch -m main master
# git fetch origin
# git branch -u origin/master master
# git remote set-head origin -a


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

        # Boolean attributes
        # Whether the player wants to hit or stand or blackjack
        self.stand = None
        self.double = None
        self.blackjack = None
        self.bust = None

        # This is used to keep track of game messages
        self.game_start_message = None
        self.game_message = None

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
            self.box.add_field(name="\u200b",
                               value="Every game uses a 52 card deck.\nDealer stands on soft 17.",
                               inline=False)

            self.game_start_message = await payload.channel.send(embed=self.box)
            await self.game_start_message.add_reaction('👍')

            # Reset attributes
            self.stand = False
            self.double = False
            self.blackjack = False
            self.bust = False

    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.user.id:
            return

        # When the game start embed has been reacted to
        # Starts the game
        # This is different from other embeds
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
            # self.house.add("two")
            # self.house.add("two")
            # self.player.add("queen")
            # self.player.add("ace")

            # Populates the embed
            self.box.clear_fields()
            self.box.add_field(name="Dealer hand", value=("[" + self.house.card(0) + "] [?]"), inline=False)
            self.box.add_field(name="Your hand", value=self.player.return_hand(), inline=False)

            # Footer prompt
            self.box.set_footer(text='\nH to hit, S to stand, and D to double down')

            # Immediately check for blackjack after drawing cards
            if self.player.total() == 21:
                self.box.add_field(name="\u200b\nBlackjack!", value='\u200b', inline=False)
                self.blackjack = True
                self.box.set_footer(text=discord.Embed.Empty)

            self.game_message = await self.get_channel(payload.channel_id).send(embed=self.box)

            # Adds the buttons (reactions) to play if not blackjack
            if not self.blackjack:
                await self.game_message.add_reaction('🇭')
                await self.game_message.add_reaction('🇸')
                await self.game_message.add_reaction('🇩')

        # Player interactions
        if self.player.total() < 21 and not self.stand and not self.double:
            if payload.emoji.name == '🇭':
                # Add a card
                self.player.add(self.deck.draw())

                # Not bust after a card is drawn
                if self.player.total() < 21:
                    # Show the current game
                    self.box.clear_fields()
                    self.box.add_field(name="Dealer hand", value=("[" + self.house.card(0) + "] [?]"), inline=False)
                    self.box.add_field(name="Your hand", value=self.player.return_hand(), inline=False)
                    self.game_message = await self.get_channel(payload.channel_id).send(embed=self.box)

                    # Adds the buttons (reactions) to play
                    await self.game_message.add_reaction('🇭')
                    await self.game_message.add_reaction('🇸')
                    await self.game_message.add_reaction('🇩')

            if payload.emoji.name == '🇸':
                self.stand = True
                # Do not need to show the players hand
                # Clear fields only
                self.box.clear_fields()

            if payload.emoji.name == '🇩':
                self.double = True
                # Add a card
                self.player.add(self.deck.draw())

                # Show the current game
                self.box.clear_fields()
                self.box.add_field(name="Dealer hand", value=("[" + self.house.card(0) + "] [?]"), inline=False)
                self.box.add_field(name="Your hand", value=self.player.return_hand(), inline=False)
                self.game_message = await self.get_channel(payload.channel_id).send(embed=self.box)

        if self.player.total() > 21:
            self.bust = True
            self.box.add_field(name="\nYou've gone bust.", value='\u200b', inline=False)
            self.game_message = await self.get_channel(payload.channel_id).send(embed=self.box)

        # If they reached 21
        # But not a natural hand
        if self.player.total() == 21 and not self.blackjack:
            self.blackjack = True
            self.box.add_field(name="\u200b\nBlackjack!", value='\u200b', inline=False)
            self.game_message = await self.get_channel(payload.channel_id).send(embed=self.box)

        # Continue the game after player moves are over
        # Reveals the dealer hand
        # Also starts the dealer drawing process
        if self.stand or self.double or self.bust or self.blackjack:
            self.box.set_footer(text=discord.Embed.Empty)
            self.box.clear_fields()
            self.box.add_field(name="Dealer hand", value=self.house.return_hand(), inline=False)
            self.box.add_field(name="Your hand", value=self.player.return_hand(), inline=False)
            self.game_message = await self.get_channel(payload.channel_id).send(embed=self.box)

            # Dealer keeps drawing cards until soft 17
            # For each card drawn, send an embed
            while self.house.total() <= 17:
                self.house.add(self.deck.draw())
                self.box.clear_fields()
                self.box.add_field(name="Dealer hand", value=self.house.return_hand(), inline=False)
                self.box.add_field(name="Your hand", value=self.player.return_hand(), inline=False)
                self.game_message = await self.get_channel(payload.channel_id).send(embed=self.box)


env = loadenv.Env()
key = env.getenv('BOT_TOKEN')
BotClient().run(key)

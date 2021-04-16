
# Blackjack

# Make a deck object that draws cards
# Make a player and/or house object that holds cards
# Calculate total with sum

import random
import time


class Deck:

    def __init__(self):
        self.deck = ["ace", "ace", "ace", "ace",
                     "two", "two", "two", "two",
                     "three", "three", "three", "three",
                     "four", "four", "four", "four",
                     "five", "five", "five", "five",
                     "six", "six", "six", "six",
                     "seven", "seven", "seven", "seven",
                     "eight", "eight", "eight", "eight",
                     "nine", "nine", "nine", "nine",
                     "ten", "ten", "ten", "ten",
                     "jack", "jack", "jack", "jack",
                     "queen", "queen", "queen", "queen",
                     "king", "king", "king", "king"]

    def draw(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def amount(self):
        return len(self.deck)


class Hand:

    def __init__(self):
        self.hand = list()

    def add(self, card):
        self.hand.append(card)

    def remove(self, position):
        return self.hand.pop(position)

    # Return the total value of the cards
    def total(self):
        # Ace changes as the hand value changes
        # All cards above 10 is counted as 10

        total = 0
        aces = 0

        for card in self.hand:
            if card == "ace":
                aces += 1
                total += 1

            if card == "two":
                total += 2

            if card == "three":
                total += 3

            if card == "four":
                total += 4

            if card == "five":
                total += 5

            if card == "six":
                total += 6

            if card == "seven":
                total += 7

            if card == "eight":
                total += 8

            if card == "nine":
                total += 9

            if card == "ten":
                total += 10

            if card == "jack":
                total += 10

            if card == "queen":
                total += 10

            if card == "king":
                total += 10

        # Change the ace value depending on the total value
        for loop in range(aces):
            if total + 10 <= 21:
                total += 10

        return total

    def card(self, position):
        return self.hand[position]

    # This is used to check the values of cards when splitting hand
    # Ace is counted as 11
    def value(self, position):
        value = None
        card = self.hand[position]
        if card == "ace":
            value = 11

        if card == "two":
            value = 2

        if card == "three":
            value = 3

        if card == "four":
            value = 4

        if card == "five":
            value = 5

        if card == "six":
            value = 6

        if card == "seven":
            value = 7

        if card == "eight":
            value = 8

        if card == "nine":
            value = 9

        if card == "ten":
            value = 10

        if card == "jack":
            value = 10

        if card == "queen":
            value = 10

        if card == "king":
            value = 10

        return value

    def print_hand(self):
        for card in self.hand:
            print("[" + card + "] ", end="")
        print("(" + str(self.total()) + ")")

    # This simply returns the deck, for testing purposes only
    def deck(self):
        return self.hand


# Game
# While loop for each game, break or continue for a new game

while True:
    print("Blackjack\n")
    print("Every game uses shuffled 52 card deck")
    print("Dealer stands on soft 17")
    print("\n\n")
    time.sleep(2)

    deck = Deck()
    house = Hand()
    player = Hand()
    player2 = None
    bust = False
    bust2 = False
    split = False
    blackjack = False
    blackjack2 = False
    # In case the player splits, a new player Hand() object is needed

    print("The cards are drawn\n")
    house.add(deck.draw())
    player.add(deck.draw())
    house.add(deck.draw())
    player.add(deck.draw())

    # Show dealer and player's hands on screen
    print("Dealer hand: [" + house.card(0) + "] [?]")
    print("Your hand: ", end="")
    player.print_hand()
    print()

    # If the player has two identical cards, they can choose to split
    if player.value(0) == player.value(1):
        print("Would you like to split?")
        response = input("\"Split\" or \"s\" to split, or press enter otherwise: ")
        print()

        if response == "Split" or response == "split" or response == "s":
            split = True
            player2 = Hand()
            bust2 = False
            # Move the card from one hand to the other
            player2.add(player.remove(1))
            player.add(deck.draw())
            player2.add(deck.draw())

            print("Your first hand: ", end="")
            player.print_hand()
            print("Your second hand: ", end="")
            player2.print_hand()
            # Could add a lot of blank lines here
            print("\n")

    # Check for natural hand
    if player.total() == 21:
        blackjack = True
        print("Blackjack!")
        print()

    if split and player2.total() == 21:
        blackjack2 = True
        print("Second hand Blackjack!")
        print()

    # If hits == True, the player can continue to hit or double down
    stand = False
    double = False
    if split and not blackjack:
        print("This is your first hand")
    while player.total() < 21 and not stand and not double and not blackjack:
        print("Hit, stand, or double down?")
        response = input("\"Hit\" or \"h\" to hit, "
                         "\"Stand\" or \"s\" to stand, "
                         "\"Double down\" or \"d\" to double down: ")

        if response == "Hit" or response == "hit" or response == "h":
            player.add(deck.draw())
            # Print player's hand
            print("Your hand: ", end="")
            player.print_hand()

        # The player can no longer hit if they stand or double down
        elif response == "Stand" or response == "stand" or response == "s":
            stand = True
            print("Your hand: ", end="")
            player.print_hand()

        elif response == "Double down" or response == "double down" or response == "d":
            double = True
            player.add(deck.draw())
            print("Your hand: ", end="")
            player.print_hand()

        print()

    if player.total() > 21:
        bust = True
        print("You've gone bust\n\n")

    if player.total() == 21:
        blackjack = True
        print("Blackjack")

    # Could add a lot of blank lines here

    # Split hand
    stand = False
    double = False
    if split:
        while player2.total() < 21 and not stand and not double:
            print("This is your second hand")
            print("Your hand: ", end="")
            player2.print_hand()
            print()

            print("Hit, stand, or double down?")
            response = input("\"Hit\" or \"h\" to hit, "
                             "\"Stand\" or \"s\" to stand, "
                             "\"Double down\" or \"d\" to double down: ")

            if response == "Hit" or response == "hit" or response == "h":
                player2.add(deck.draw())
                # Print player's hand
                print("Your hand: ", end="")
                player2.print_hand()

            # The player can no longer hit if they stand or double down
            elif response == "Stand" or response == "stand" or response == "s":
                stand = True
                print("Your hand: ", end="")
                player2.print_hand()

            elif response == "Double down" or response == "double down" or response == "d":
                double = True
                player2.add(deck.draw())
                print("Your hand: ", end="")
                player2.print_hand()

    if split and player2.total() > 21:
        bust2 = True
        print("Your second hand has gone bust")

    time.sleep(2)

    # Printing dealer's original hand
    print("Dealer hand: ", end="")
    house.print_hand()

    while house.total() < 17:
        print()
        print("The dealer is drawing a card")
        house.add(deck.draw())
        print("Dealer hand: ", end="")
        house.print_hand()
        time.sleep(3)

    print()

    # The player has not gone bust
    # Their hand is less than 21
    if not bust:
        if house.total() > 21:
            print("The house has gone bust. You won.")
            print("The house have", house.total())
            print("You have", player.total())

        elif house.total() > player.total():
            print("The house have", house.total())
            print("You have", player.total())
            print("You lose")

        elif house.total() < player.total():
            print("The house have", house.total())
            print("You have", player.total())
            print("You win")

        elif house.total() == player.total():
            print("You and the house both have", house.total())
            print("The result is a Push")

    print("\n")

    # Check for second hand winner
    if split and not bust2:
        if house.total() > 21:
            print("The house has gone bust. You won.")
            print("The house have", house.total())
            print("Your second hand has", player2.total())

        elif house.total() > player2.total():
            print("The house have", house.total())
            print("Your second hand has", player2.total())
            print("You lose")

        elif house.total() < player2.total():
            print("The house have", house.total())
            print("Your second hand has", player2.total())
            print("You win")

        elif house.total() == player2.total():
            print("Your second hand and the house both have", house.total())
            print("The result is a Push")

    # Output the results after the player has gone bust
    if bust:
        print("You have gone bust.")
        print("The house have", house.total())
        print("You have", player.total())

    if bust2:
        print("Your second hand has gone bust.")
        print("The house have", house.total())
        print("You have", player.total())

    print("Play again?")
    again = input()
    if again == "Yes" or again == "yes" or again == "y":
        print("\n\n\n\n")
        continue

    else:
        break

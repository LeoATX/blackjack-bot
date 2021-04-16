# This is the player's or the dealer's hand
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

    # Returns the hand as a string
    def return_hand(self):
        string = ""
        for card in self.hand:
            string = string + "[" + card + "] "
        return string

    # This simply returns the deck, for testing purposes only
    def deck(self):
        return self.hand

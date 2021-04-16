# This is the deck that you draw cards from
import random


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

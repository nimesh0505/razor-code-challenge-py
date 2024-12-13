# The Deck class should represent a standard deck of 52 playing cards.
# It should include methods to shuffle the deck, draw a card, reset the deck,
# and check the number of remaining cards. Additionally, it should provide a
# string representation of the deck.

# The Deck class should have the following attributes and methods:

# Attributes:
# - SUITS: A list of the four suits in a deck of cards.
# - RANKS: A list of the thirteen ranks in a deck of cards.
# - cards: A list to store the cards currently in the deck.

# Methods:
# - __init__: Initialize the deck with a full set of 52 cards and shuffle them.
# - shuffle: Shuffle the deck.
# - draw: Draw a card from the deck. Raise an IndexError if no cards are left.
# - reset: Reset the deck to the original state and shuffle it.
# - remaining_cards: Return the number of cards left in the deck.
# - __str__: Return a string representation of the remaining cards in the deck.
import random


class Deck:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = list(range(2, 11)) + ["Jack", "Queen", "King", "Ace"]

    def __init__(self, deck_count=1):
        self.deck_count = deck_count
        self.reset()

    def reset(self):
        """
        Resets the cards to a full set of combined decks
        Each deck is 52 cards and thier total is mutiplied by deck_count
        """
        self.cards = [
            {"suit": suit, "value": value}
            for suit in self.SUITS
            for value in self.RANKS
        ] * self.deck_count
        self.shuffle()

    def shuffle(self):
        """
        Shuffle all the cards in the combined decks
        """
        random.shuffle(self.cards)

    def draw(self, count=1):
        """
        Draws a specific number of cards from th combined decks.
        """
        if count > len(self.cards):
            raise ValueError("Not enough cards to draw")

        drawn_cards = self.cards[:count]
        self.cards = self.cards[count:]
        return drawn_cards

    def remaining_cards(self):
        ""
        return len(self.cards)

    def __str__(self):
        return f"Deck with {self.remaining_cards()} cards remaining."

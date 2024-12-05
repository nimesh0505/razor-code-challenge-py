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

class Deck:

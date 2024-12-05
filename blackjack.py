from deck import Deck

# The Blackjack class should manage a game of Blackjack with the following features:
# - Initialize with a specified number of decks.
# - Reset the table by shuffling all decks together and clearing active hands.
# - Deal two cards to a player for the initial deal.
# - Add a card to the player's hand when they hit.
# - Split a player's hand into two if the first two cards are of the same rank, and add a card to each new hand.
# - Fold the player's hand, removing them from the active hands.

# The class should have the following methods:
# - __init__: Initialize the Blackjack table with a specified number of decks.
# - reset: Reset the table by shuffling all decks together and clearing active hands.
# - deal: Deal two cards to a player for the initial deal.
# - hit: Add a card to the player's hand.
# - split: Split a player's hand into two if the first two cards are of the same rank, and add a card to each new hand.
# - fold: Fold the player's hand, removing them from the active hands.

# The class should use a Deck class to manage the deck(s) of cards.
# The class should use a dictionary to keep track of players' hands.

class Blackjack:

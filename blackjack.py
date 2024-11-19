from deck import Deck

class Blackjack:
    def __init__(self, num_decks=1):
        """
        Initialize the Blackjack table with a specified number of decks.
        :param num_decks: Number of decks to use at the table.
        """

    def reset(self):
        """Reset the table by shuffling all decks together and clearing active hands."""

    def deal(self, player):
        """
        Deal two cards to a player.
        :param player: The player's identifier (e.g., a name or number).
        """

    def hit(self, player):
        """
        Add a card to the player's hand.
        :param player: The player's identifier.
        """

    def split(self, player):
        """
        Split a player's hand into two if the first two cards are of the same rank.
        You can only split after the initial deal, not after you already hit
        Also adds a card to each new hand.
        :param player: The player's identifier.
        """

    def fold(self, player):
        """
        Fold the player's hand, removing them from the active hands.
        :param player: The player's identifier.
        """

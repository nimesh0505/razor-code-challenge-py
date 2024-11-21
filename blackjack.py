from deck import Deck

class Blackjack:
    def __init__(self, num_decks=1):
        """
        Initialize the Blackjack table with a specified number of decks.
        Also init the active_hands dictionary to keep track of players' hands.
        :param num_decks: Number of decks to use at the table.
        """

    def reset(self):
        """Reset the table by shuffling all decks together and clearing active hands."""

    def deal(self, player):
        """
        Deal two cards to a player. (This is the initial deal. i.e. replaces the hand)
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
        e.g. consider the active_hands dict:
        {
            "Alice": ["Ace of Spades", "Ace of Hearts"],
        }
        After splitting, it should look like:
        {
            "Alice": ["Ace of Spades"],
            "Alice_split": ["Ace of Hearts"],
        }
        then after hitting Alice and Alice_split:
        {
            "Alice": ["Ace of Spades", "3 of Diamonds"],
            "Alice_split": ["Ace of Hearts", "7 of Clubs"],
        }
        :param player: The player's identifier.
        """

    def fold(self, player):
        """
        Fold the player's hand, removing them from the active hands.
        :param player: The player's identifier.
        """

class Deck:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    def __init__(self):
        """Initialize the deck with a full set of 52 cards."""
        self.cards = []

    def shuffle(self):
        """Shuffle the deck."""

    def draw(self):
        """
        Draw a card from the deck.

        Raises:
            IndexError: If no cards are left in the deck.
        """

    def reset(self):
        """Reset the deck to the original state and shuffle it."""

    def remaining_cards(self):
        """Return the number of cards left in the deck."""

    def __str__(self):
        """Return a string representation of the remaining cards in the deck."""


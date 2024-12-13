import unittest

from deck import Deck


class TestDeck(unittest.TestCase):
    def setUp(self):
        """Set up a new deck instance for each test."""
        self.deck = Deck()

    def test_unique_cards(self):
        """Test that a shuffled and drawn deck has no duplicate cards."""
        self.deck.shuffle()
        drawn_cards = [tuple(self.deck.draw()[0].items()) for _ in range(52)]
        self.assertEqual(len(set(drawn_cards)), 52, "Deck has duplicate cards.")

    def test_randomness(self):
        """
        Test that shuffling multiple times produces different sequences.
        Reset the deck between shuffles to ensure fair tests.
        """
        sequences = []
        for _ in range(10):
            self.deck.reset()
            self.deck.shuffle()
            sequences.append([tuple(card.items()) for card in self.deck.draw(52)])
        unique_sequences = len(set(tuple(seq) for seq in sequences))
        self.assertGreater(
            unique_sequences, 1, "Shuffling produces identical sequences."
        )

    def test_draw_empty_deck(self):
        """Test that drawing from an empty deck raises an error."""
        for _ in range(52):
            self.deck.draw()
        with self.assertRaises(
            ValueError, msg="No error raised for drawing from empty deck."
        ):
            self.deck.draw()

    def test_multiple_deck(self):
        multi_deck = Deck(deck_count=2)
        self.assertEqual(
            multi_deck.remaining_cards(),
            104,
            "Incorrect number of crads for multiple decks.",
        )

    def test_remaining_cards(self):
        """Test that the remaining_cards method works correctly."""
        self.assertEqual(
            self.deck.remaining_cards(), 52, "Initial deck size is not 52."
        )
        self.deck.draw()
        self.assertEqual(
            self.deck.remaining_cards(), 51, "Deck size did not decrease after draw."
        )

    def test_str_representation(self):
        """Test the string representation of the deck."""
        self.assertEqual(
            str(self.deck),
            "Deck with 52 cards remaining.",
            "Incorrect initial string representation.",
        )
        self.deck.draw()
        self.assertEqual(
            str(self.deck),
            "Deck with 51 cards remaining.",
            "String representation not updated after draw.",
        )


if __name__ == "__main__":
    unittest.main()

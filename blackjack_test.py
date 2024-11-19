import unittest
from blackjack import Blackjack


class TestBlackjack(unittest.TestCase):
    def setUp(self):
        """Set up a new Blackjack table for testing."""
        self.table = Blackjack(num_decks=2)

    def test_deal(self):
        """Test that dealing assigns two cards to a player."""
        self.table.deal("Alice")
        self.assertIn("Alice", self.table.active_hands)
        self.assertEqual(len(self.table.active_hands["Alice"]), 2)

    def test_hit(self):
        """Test that hitting adds a card to the player's hand."""
        self.table.deal("Alice")
        self.table.hit("Alice")
        self.assertEqual(len(self.table.active_hands["Alice"]), 3)

    def test_split(self):
        """Test splitting a hand with identical ranks."""
        self.table.active_hands["Alice"] = ["Ace of Spades", "Ace of Hearts"]
        self.table.split("Alice")
        self.assertIn("Alice_split", self.table.active_hands)
        self.assertEqual(len(self.table.active_hands["Alice"]), 2)
        self.assertEqual(len(self.table.active_hands["Alice_split"]), 2)

    def test_split_invalid_hand(self):
        """Test splitting fails for a hand that cannot be split."""
        self.table.active_hands["Alice"] = ["Ace of Spades", "King of Hearts"]
        self.table.split("Alice")
        self.assertNotIn("Alice_split", self.table.active_hands)

    def test_fold(self):
        """Test folding removes the player's hand."""
        self.table.deal("Alice")
        self.table.fold("Alice")
        self.assertNotIn("Alice", self.table.active_hands)

    def test_reset(self):
        """Test that reset clears hands and shuffles cards."""
        self.table.deal("Alice")
        self.table.reset()
        self.assertEqual(len(self.table.active_hands), 0)
        self.assertEqual(len(self.table.cards), 52 * self.table.num_decks)


if __name__ == "__main__":
    unittest.main()

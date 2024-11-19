import unittest
from unittest.mock import patch
from game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        """Set up a Game instance with one deck for testing."""
        self.counter = Game(num_decks=1)

    def test_deal(self):
        """Test dealing cards assigns hands to player and house."""
        self.counter.deal("Alice")
        self.assertIn("Alice", self.counter.table.active_hands)
        self.assertEqual(len(self.counter.table.active_hands["Alice"]), 2)
        self.assertEqual(len(self.counter.house_hand), 2)

    def test_hit(self):
        """Test hitting adds a card to the player's hand."""
        self.counter.deal("Alice")
        initial_count = len(self.counter.table.active_hands["Alice"])
        self.counter.hit("Alice")
        self.assertEqual(len(self.counter.table.active_hands["Alice"]), initial_count + 1)

    @patch("builtins.print")
    def test_reveal_player_wins(self, mock_print):
        """Test reveal when the player has a higher hand value than the house."""
        self.counter.table.active_hands["Alice"] = ["10 of Hearts", "7 of Spades"]  # Player: 17
        self.counter.house_hand = ["3 of Clubs", "10 of Diamonds"]  # House: 13
        self.counter.reveal("Alice")

        # Capture printed output
        printed_lines = [call.args[0] for call in mock_print.call_args_list]
        self.assertIn("You win!", printed_lines)

    @patch("builtins.print")
    def test_reveal_house_wins(self, mock_print):
        """Test reveal when the house has a higher hand value than the player."""
        self.counter.table.active_hands["Alice"] = ["7 of Hearts", "8 of Diamonds"]  # Player: 15
        self.counter.house_hand = ["King of Hearts", "9 of Spades"]  # House: 19
        self.counter.reveal("Alice")

        # Capture printed output
        printed_lines = [call.args[0] for call in mock_print.call_args_list]
        self.assertIn("House wins.", printed_lines)

    @patch("builtins.print")
    def test_reveal_tie(self, mock_print):
        """Test reveal when the player and house tie."""
        self.counter.table.active_hands["Alice"] = ["10 of Hearts", "7 of Spades"]  # Player: 17
        self.counter.house_hand = ["9 of Diamonds", "8 of Hearts"]  # House: 17
        self.counter.reveal("Alice")

        # Capture printed output
        printed_lines = [call.args[0] for call in mock_print.call_args_list]
        self.assertIn("It's a tie.", printed_lines)

    @patch("builtins.print")
    def test_reveal_player_bust(self, mock_print):
        """Test reveal when the player busts."""
        self.counter.table.active_hands["Alice"] = ["10 of Hearts", "9 of Spades", "5 of Clubs"]  # Player: 24 (Bust)
        self.counter.house_hand = ["3 of Clubs", "10 of Diamonds"]  # House: 13
        self.counter.reveal("Alice")

        # Capture printed output
        printed_lines = [call.args[0] for call in mock_print.call_args_list]
        self.assertIn("You bust! House wins.", printed_lines)

    @patch("builtins.print")
    def test_reveal_house_bust(self, mock_print):
        """Test reveal when the house busts."""
        self.counter.table.active_hands["Alice"] = ["10 of Hearts", "7 of Spades"]  # Player: 17
        self.counter.house_hand = ["10 of Clubs", "6 of Hearts", "7 of Diamonds"]  # House: 23 (Bust)
        self.counter.reveal("Alice")

        # Capture printed output
        printed_lines = [call.args[0] for call in mock_print.call_args_list]
        self.assertIn("House busts! You win.", printed_lines)

    @patch("builtins.print")
    def test_reset(self, mock_print):
        """Test reset clears the game state."""
        self.counter.deal("Alice")
        self.counter.reset()

        self.assertEqual(len(self.counter.table.active_hands), 0)
        self.assertEqual(len(self.counter.house_hand), 0)
        self.assertEqual(self.counter.card_count, 0)

        # Capture printed output
        printed_lines = [call.args[0] for call in mock_print.call_args_list]
        self.assertIn("Game reset. Card count cleared.", printed_lines)

    def test_card_count_update(self):
        """Test the card count updates correctly."""
        # Directly manipulate cards for predictability.
        self.counter.table.active_hands["Alice"] = ["2 of Hearts", "10 of Spades"]
        self.counter.house_hand = ["Ace of Diamonds", "6 of Clubs"]
        for card in self.counter.table.active_hands["Alice"] + self.counter.house_hand:
            self.counter._update_count(card)

        # Count calculation:
        # 2 (+1), 10 (-1), Ace (-1), 6 (+1) = 0
        self.assertEqual(self.counter.card_count, 0)

    def test_get_advice(self):
        """Test the advice returned matches the card count."""
        self.counter.card_count = 10  # Simulate a high count.
        self.assertEqual(self.counter._get_advice(), "Bet High: The deck is favorable for you.")

        self.counter.card_count = -10  # Simulate a low count.
        self.assertEqual(self.counter._get_advice(), "Bet Low: The deck is unfavorable.")

        self.counter.card_count = 0  # Simulate a neutral count.
        self.assertEqual(self.counter._get_advice(), "Play Normally: The deck is neutral.")


if __name__ == "__main__":
    unittest.main()

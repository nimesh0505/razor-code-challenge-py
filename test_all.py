import unittest
from deck_test import TestDeck
from blackjack_test import TestBlackjack
from game_test import TestGame

if __name__ == "__main__":
    # Create a test suite that includes all test cases
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # Add test cases from individual test modules
    suite.addTests(loader.loadTestsFromTestCase(TestDeck))
    suite.addTests(loader.loadTestsFromTestCase(TestBlackjack))
    suite.addTests(loader.loadTestsFromTestCase(TestGame))

    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

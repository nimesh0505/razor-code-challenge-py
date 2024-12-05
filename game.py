from blackjack import Blackjack

low_cards = ["2", "3", "4", "5", "6"]
high_cards = ["10", "Jack", "Queen", "King", "Ace"]

advices = {
    "high": "Bet High: The deck is favorable for you.",
    "low": "Bet Low: The deck is unfavorable.",
    "neutral": "Play Normally: The deck is neutral.",
}

results = {
    "player_win": "You win!",
    "player_bust": "You bust! House wins.",
    "house_win": "House wins.",
    "house_bust": "House busts! You win.",
    "tie": "It's a tie.",
}

# The Game class should manage the overall game flow and user interactions.
# It should provide a command-line interface for the user to interact with the game.
# The Game class should use the Blackjack class to manage the game logic.
# The Game class should provide advice to the player based on the card count.

# The class should have the following methods:
# - __init__: Initialize the Game with a specified number of decks.
# - deal: Deal two cards to a player and the house, and update the card count.
# - hit: Perform a hit for the player and update the card count.
# - split: Perform a split for the player.
# - fold: Perform a fold for the player.
# - reveal: Reveal the house's hand and determine the winner.
# - reset: Reset the game state and card count.
# - run: Run the Game and accept user commands.

class Game:
    def run(self):
        """Run the Game and accept user commands."""
        print("Welcome to the Blackjack Game!")
        print("Commands: deal, hit, split, fold, reveal, reset, quit")

        while True:
            command = input("Enter command: ").strip().lower()
            if command == "quit":
                print("Exiting the game. Goodbye!")
                break
            elif command in ["deal", "hit", "split", "fold", "reveal"]:
                player = input("Enter player name: ").strip()
                if command == "deal":
                    self.deal(player)
                elif command == "hit":
                    self.hit(player)
                elif command == "split":
                    self.split(player)
                elif command == "fold":
                    self.fold(player)
                elif command == "reveal":
                    self.reveal(player)
            elif command == "reset":
                self.reset()
            else:
                print("Invalid command. Try again.")

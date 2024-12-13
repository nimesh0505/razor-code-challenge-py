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
    def __init__(self, deck):
        self.deck = deck
        self.players = {}
        self.dealer_hand = []

    def add_player(self, player_name):
        """Adds a player to the table"""
        if player_name in self.players:
            raise ValueError("Player already exits")
        self.players[player_name] = []

    def deal_initial_cards(self):
        """
        Deal two cards to each players and the dealer
        """
        for player in self.players:
            self.players[player] = self.deck.draw(2)
        self.dealer_hand = self.deck.draw(2)

    def hit(self, player_name):
        if player_name not in self.players:
            raise ValueError("Player not found")
        self.players[player_name].extends(self.deck.draw(1))

    def calculate_hand_value(self, hand):
        """
        Calculates the value of a hand, considering Ace as 1 or 11
        """
        value = 0
        aces = 0
        for card in hand:
            if isinstance(card["value"], int):
                value += card["value"]
            elif card["value"] in ["Jack", "Queen", "King"]:
                value += 10
            else:
                value += 11
                aces += 1
        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def fold(self, player_name):
        if player_name in self.players:
            del self.players[player_name]
        else:
            raise ValueError("Player not found.")

    def dealer_turn(self):
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.draw(1)[0])

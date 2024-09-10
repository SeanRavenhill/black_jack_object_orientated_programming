# Codecademy Python OOP Project
# Simple Blackjack Game: 52 Card Single Deck | No Bets | Single Player | Terminal-Based

# Importing required modules:
# random: Used to shuffle the deck of cards, ensuring random card distribution.
# subprocess: Utilized for executing shell commands, specifically for clearing the console screen.
# os: Employed to detect the operating system type, assisting in deciding which console clearing command to use.
import random
import subprocess
import os

# Constants representing the winning score in Blackjack and the dealer's stand threshold
BLACKJACK = 21
DEALERS_STAND = 17


# Clears the console screen cross-platform.
def clear_screen():
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run([command], shell=True)


# Prints a divider line for clear separation of game stages
def print_dash_divider():
    print("-------------------------------------------")


def print_star_divider():
    print("*******************************************")


# Represents a playing card with a rank and a suit
class Card:
    # Class-level constants define possible ranks and suits for a standard deck (excluding Jokers)
    RANKS = [
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]
    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self, rank, suit):
        # Initializing card with a specific rank and suit
        self.rank = rank
        self.suit = suit

    def value(self):
        # Returns the numerical value associated with the card's rank
        if self.rank in ["Jack", "Queen", "King"]:
            return 10
        elif self.rank == "Ace":
            return 1
        else:
            return self.RANKS.index(self.rank) + 2

    def __repr__(self) -> str:
        # Provides a string representation of the card
        return f"{self.rank} of {self.suit}"


# The Deck class represents a standard deck of cards with functionality to shuffle and deal
class Deck:
    def __init__(self):
        # Initializing the deck with 52 unique cards and shuffling them
        self.cards = [Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]
        self.shuffle()

    def shuffle(self):
        # Shuffling the cards in the deck
        random.shuffle(self.cards)

    def deal(self):
        # Returns and removes the top card from the deck
        return self.cards.pop()


# The Hand class represents a collection of cards dealt to a player or dealer
class Hand:
    def __init__(self):
        # Initializing an empty hand
        self.cards = []

    def add_card(self, card):
        # Adds the provided card to the hand
        self.cards.append(card)

    def value(self):
        # Calculates and returns the total value of the cards in the hand
        total = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == "Ace")
        # Adjust the value for aces when beneficial as the ace have dual values of either 1 or 11 given the hands total value
        while total <= 11 and aces:
            total += 10
            aces -= 1
        return total

    def show(self, hide_first_card=False):
        # Displays the contents of the hand, with an option to hide the first card (useful for dealer's hand)
        if hide_first_card:
            print("Hidden Card")
            print("\n".join(map(str, self.cards[1:])))
        else:
            print("\n".join(map(str, self.cards)))


# The Player class represents a game participant (either a human player or the dealer)
class Player:
    def __init__(self, name="Player"):
        # Initializing player with a name and an empty hand
        self.name = name
        self.hand = Hand()

    def hit(self, deck):
        # Allows the player to draw a card from the provided deck
        card = deck.deal()
        self.hand.add_card(card)

    def stand(self):
        # Indicates that the player opts not to draw more cards.
        print(f"{self.name} stands with a total of {self.hand.value()}")

    def show(self, hide_first_card=False):
        # Displays the player's hand and its total value, with an option to hide the first card
        print_dash_divider()
        print(f"{self.name} holds:")
        print_dash_divider()
        self.hand.show(hide_first_card)
        print_dash_divider()
        print(f"{self.name}'s current hand value is {self.hand.value()}")
        print_dash_divider()
        print()


# The Dealer class represents the game's dealer and inherits from the Player class
class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")


# The Game class orchestrates the flow of a Blackjack game. It initializes and manages the deck,
# the human player, and the dealer. The class defines the turn-based interactions, deals initial
# cards, and determines the winner based on Blackjack rules. It serves as the primary driver for
# game progression and enforces the gameplay logic
class Game:
    def __init__(self, players_name):
        # Initialize a new game with a deck, player, and dealer.
        self.deck = Deck()
        self.player = Player(players_name)
        self.dealer = Dealer()

    def game_setup(self):
        # Perform the initial setup for the game.
        clear_screen()
        print_star_divider()
        print("Initial Deal")
        print_star_divider()
        print()
        self.deal_initial_cards()
        return self.is_immediate_blackjack()

    def deal_initial_cards(self):
        # Deal two cards to each player to start the game.
        for _ in range(2):
            self.player.hit(self.deck)
            self.dealer.hit(self.deck)

    def is_immediate_blackjack(self):
        # Checks if the dealer or player has Blackjack at the start of the game.
        dealer_blackjack = self.dealer.hand.value() == BLACKJACK
        player_blackjack = self.player.hand.value() == BLACKJACK

        if dealer_blackjack or player_blackjack:
            self.dealer.show()
            self.player.show()
            if dealer_blackjack and player_blackjack:
                self.winner_message(
                    "It's a push! Both player and dealer have Blackjack!"
                )
            elif dealer_blackjack:
                self.winner_message("Dealer wins with a Blackjack!")
            elif player_blackjack:
                self.winner_message(f"{self.player.name} wins with a Blackjack!")
            return True
        return False

    def players_turn(self):
        """Manage the player's turn until they stand or bust."""
        print_star_divider()
        print(f"{self.player.name}'s turn:")
        print_star_divider()
        print()

        # Player's turn continues until they stand, bust, or achieve a total value of 21
        while self.player.hand.value() < BLACKJACK:
            players_turn = self.get_players_decision()
            if players_turn == "hit":
                self.player_hit()
            elif players_turn == "stand":
                print(f"{self.player.name} Stands on {self.player.hand.value()}")
                break

        # Check for possible outcomes of player's turn: Blackjack, Bust, or proceed to dealer's turn
        if self.player.hand.value() > BLACKJACK:
            print(f"{self.player.name} Busts on {self.player.hand.value()}")
            self.determine_winner()
        else:
            print()
            self.dealers_turn()

    def dealers_turn(self):
        """Manage the dealer's turn until they stand or bust."""
        print_star_divider()
        print("Dealer's turn:")
        print_star_divider()
        print()

        self.dealer.show()

        while self.dealer.hand.value() < DEALERS_STAND:
            self.dealer_hits()
            self.dealer.show()

        dealers_final_hand = self.dealer.hand.value()

        if dealers_final_hand > BLACKJACK:
            self.dealer_busts()
            self.determine_winner()
        elif dealers_final_hand >= DEALERS_STAND and dealers_final_hand <= BLACKJACK:
            self.determine_winner()

    def determine_winner(self):
        """Determine the winner of the game."""
        dealers_final_hand = self.dealer.hand.value()
        players_final_hand = self.player.hand.value()

        if players_final_hand > BLACKJACK:
            self.winner_message("Dealer Wins!")
        elif dealers_final_hand > BLACKJACK:
            self.winner_message(f"{self.player.name} Wins!")
        elif dealers_final_hand > players_final_hand:
            self.winner_message("Dealer Wins!")
        elif dealers_final_hand < players_final_hand:
            self.winner_message(f"{self.player.name} Wins!")
        else:
            self.winner_message("Game is a Draw!")

    # Game Class utility and supporting methods
    def get_players_decision(self):
        """Get the player's decision to hit or stand."""
        decision = input("Would you like to hit or stand? ").strip().lower()
        while decision not in ["hit", "stand"]:
            print()
            decision = input("Would you like to hit or stand? ").lower()
            print()
        return decision

    def player_hit(self):
        """Handle the player hitting and drawing a card."""
        self.player.hit(self.deck)
        print(f"{self.player.name} hits and draws the {self.player.hand.cards[-1]}")
        print()
        self.player.show()

    def dealer_hits(self):
        """Handle the dealer hitting and drawing a card."""
        self.dealer.hit(self.deck)
        print(f"Dealer hits and draws the {self.dealer.hand.cards[-1]}")
        print()

    def dealer_busts(self):
        """Handle the dealer busting."""
        print()
        print(f"Dealer Busts on {self.dealer.hand.value()}!")
        print()

    def winner_message(self, message):
        """Display a message announcing the winner."""
        print_dash_divider()
        print(message)
        print_dash_divider()


if __name__ == "__main__":

    while True:
        player_name = input('Please enter your name (or type "exit" to quit): ')
        if player_name.lower() == "exit":
            break

        print()
        new_game = Game(player_name)
        immediate_blackjack = new_game.game_setup()  # This will return True or False

        if (
            not immediate_blackjack
        ):  # If dealer or player does not have Blackjack, proceed with player's turn
            # Display the dealer's hand with the first card hidden
            new_game.dealer.show(True)

            # Display the player's full hand
            new_game.player.show()

            new_game.players_turn()

        input("\nPress Enter to play again...\n")

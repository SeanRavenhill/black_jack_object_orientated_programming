
# Simple Blackjack Game

This is a simple terminal-based Blackjack game built using Python and Object-Oriented Programming (OOP) principles. The game uses a 52-card deck (no jokers) and follows basic Blackjack rules, except for betting. It's a single-player game where the user plays against the dealer. The game clears the console for a clean display of game status, and players can choose to either "hit" or "stand."

## Project Background

This project was developed as part of the Codecademy Computer Science path. It was my first introduction to using Object-Oriented Programming (OOP) and Separation of Concerns (SOC) concepts in programming. The project helped me understand how to structure code logically and efficiently while focusing on building interactive, user-friendly terminal programs.

### Original Task Brief:

---
**Project Description:**  
Welcome to the portfolio project in CS 101: Introduction to Programming!

In this portfolio project, you will research, brainstorm, and build a basic terminal program of your choice for your friends and family to play with. After you finish building the program, you will create a blog post to share the program on a publication of your choice!

**Example Project Ideas:**
- Blackjack
- Tic-Tac-Toe
- Connect Four
- Battleship
- Minesweeper
- Who Wants to Be a Millionaire?
- Tarot Reading
- NYC MetroCard Price Calculator
- Mortgage Calculator
- Today’s Horoscope
- Your Very Own Text-Based Adventure

**Project Objectives:**
- Build a terminal program using Python
- Add at least one interactive feature using `input()`
- Use Git version control
- Use the command line and file navigation
- Write a technical blog post on the project

**Prerequisites:**
- Python
- Git/GitHub
- Command Line and File Navigation
---

### A Note on Version Control

Although the task required the use of Git version control, I did not strictly adhere to this aspect. I became deeply focused on the logic and structure of the game and admittedly overlooked the importance of proper version control practices. While I am aware of the need for version control, especially for managing features and branching in a collaborative environment, I chose to work on this project locally without using Git.

As this was an individual project with no need to share code or collaborate with others, I found Git usage to be less critical in this case. However, I recognize that this is something I need to pay more attention to in future projects, particularly in larger and collaborative environments where version control is essential for maintaining clean and trackable development processes.

## Features

- **52 Card Single Deck**: A standard deck with 4 suits (Clubs, Diamonds, Hearts, Spades) and ranks from 2 to Ace.
- **Random Card Distribution**: Uses Python’s `random` module to shuffle the deck and distribute cards.
- **Simple Rules**: No betting system, just hit, stand, and try to beat the dealer.
- **Cross-Platform Console Clearing**: Clears the console screen for a better game display, regardless of the operating system.
- **Dealer's Stand Rule**: The dealer will stand when their hand reaches 17 or more.

## How to Play

1. The game starts with the player and the dealer receiving two cards each.
2. The player can choose to "hit" (draw another card) or "stand" (keep their current hand).
3. The goal is to reach a hand value of 21 or as close as possible without going over.
4. Face cards (Jack, Queen, King) are worth 10 points, and Aces can be worth either 1 or 11.
5. The dealer will keep drawing cards until their hand is at least 17.

## Installation & Requirements

- **Python 3.x** must be installed on your machine.
- No additional external libraries are required—just the standard Python library.

### To Run the Game:

1. Clone or download this repository to your local machine.
2. Open a terminal window and navigate to the directory containing the game files.
3. Run the following command:
    ```bash
    python script.py
    ```
4. Enter your name when prompted and enjoy the game!

## Code Structure

- `Card`: Represents an individual playing card.
- `Deck`: Represents a deck of 52 shuffled cards.
- `Hand`: Represents a collection of cards dealt to either the player or dealer.
- `Player`: Represents the user and their actions (hit or stand).
- `Dealer`: Represents the dealer's automated actions.
- `Game`: Manages the flow of the game, including card dealing, player and dealer actions, and determining the winner.

## Example Gameplay

```
*******************************************
Initial Deal
*******************************************

-------------------------------------------
Player holds:
-------------------------------------------
Ace of Spades
Seven of Diamonds
-------------------------------------------
Player's current hand value is 18
-------------------------------------------

Would you like to hit or stand? stand

*******************************************
Dealer's turn:
*******************************************

-------------------------------------------
Dealer holds:
-------------------------------------------
Hidden Card
Four of Hearts
-------------------------------------------
Dealer's current hand value is 4
-------------------------------------------

Dealer hits and draws the King of Spades

Dealer stands with a total of 19

-------------------------------------------
Dealer Wins!
-------------------------------------------
```

## Acknowledgments

This project was developed as part of the Codecademy Python Object-Oriented Programming (OOP) project within the Computer Science path. It served as my introduction to OOP and Separation of Concerns (SOC) principles in programming, which helped deepen my understanding of how to organize code effectively.

---

Enjoy the game and feel free to modify or extend it!

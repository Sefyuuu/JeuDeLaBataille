# War Game Simulation

## Introduction

This project simulates different scenarios of the card game War (known as “Bataille” in French) and calculates probabilities of winning based on initial conditions. The game is played with a deck of 32 cards, and the objective is to win all the cards. 

## Rules of War

1. The game is played with a deck of 32 cards (from 7s to Aces in each suit).
2. The objective is to win all the cards.
3. Each player draws the top card of their deck; the player with the higher card wins the round and takes both cards, placing them at the bottom of their deck.
4. In the event of a tie (war), each player draws the top card of their deck and places it face down and then draws the top card of their deck and places it face up. The player with the higher face-up card wins all the cards on the table. The above is repeated as long as there is a tie.
5. If a player runs out of cards during a war, that player immediately loses the game.
6. If both players run out of cards simultaneously during a war, the game is declared a draw.
7. Cards are shuffled before being placed back under the player’s deck.
8. To avoid infinite scenarios, if no player has won after 5000 rounds, the game is declared a draw.

## Project Description

This project consists of a Flask web application that allows users to input specific starting conditions and receive the probability of winning. The game logic is implemented in a Python module using classes and methods to represent the game elements like the cards, the deck, the players, and the game itself.

### Features

- Simulate different starting scenarios for the War card game.
- Calculate and display probabilities of winning based on initial conditions.
- Input conditions such as the number of specific cards (e.g., more than 3 Aces, less than 3 Kings, and no Jack).
- Web interface for user interaction.

### Technologies Used

- Python
- Flask
- HTML/CSS for the web interface

### How It Works

1. Users input their specific starting conditions for the game through a web interface.
2. The backend logic simulates the game based on these conditions.
3. The application calculates the probabilities of winning and displays the results to the user.

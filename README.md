# BlackJack | Python Simulation
Project that utilizes OOP methods to simulate a classic game of BlackJack. 


## Project Overview

This Python project simulates the classic card game Blackjack. The program allows multiple players to participate in a round of Blackjack against a dealer. Each player starts with a certain number of tokens, places bets, and attempts to beat the dealer by getting a hand value as close to 21 as possible without exceeding it.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Gameplay](#gameplay)
6. [File Structure](#file-structure)
7. [Acknowledgements](#acknowledgements)

## Introduction

This project was developed as a demonstration of Python programming skills. The Blackjack game is implemented using object-oriented programming (OOP) principles to organize code and manage player data efficiently.

## Features

- **Multiple Players:** The program supports multiple players, each with their own set of tokens.
- **Betting System:** Players can place bets at the beginning of each round.
- **Game History:** Round results are stored in a file (`results.txt`), allowing players to review their game history.
- **Interactive Gameplay:** The game provides a user-friendly interface with prompts for actions such as hitting or standing.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/devp19/BlackJack.git

2. Navigate to the directory:

    ```bash
    cd BlackJack

3. Run the game:

    ```bash
    python blackjack.py
    ```

## Usage

- Make sure `results.txt` file is empty before starting. (Delete any previous game history!)
- Follow the on-screen prompts to set up the game and start playing.
- Press Enter/Return to progress through the game rounds.
- Enter the number of players, their names, and place bets when prompted.
- The game history is recorded in the `results.txt` file.

## Gameplay

1. **Player Setup:**
   - Enter the number of players and their names.
   - Each player starts with 100 tokens.

2. **Betting:**
   - Players place bets before each round.

3. **Game Rounds:**
   - Players take turns to hit or stand.
   - The dealer's cards are revealed at the end.

4. **Round Results:**
   - Players win tokens based on their hand value compared to the dealer.

5. **Game End:**
   - Review final results in the `results.txt` file.
   - Players' final token amounts and gains/losses are displayed.

## File Structure

- `blackjack.py`: The main Python script containing the Blackjack game logic.
- `deckofcards.txt`: A file containing the initial deck of cards.
- `results.txt`: A file storing the game history and round results.

## Acknowledgements

- **Developer:** Dev Patel
- **Course:** CPS 109 - Introduction to Computer Science    

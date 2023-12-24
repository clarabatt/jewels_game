# Jewels Game

![Jewels Game](/assets/jewels_game_example.png)

## Project Overview
Jewels Game is a 2D board game developed in Python with Pygame. In this game, two players take turns adding gems to a board. Each player starts with a gem in a specific corner of the board. A gem can be placed on any empty square or any square where the player already has at least one gem. The game utilizes an overflow mechanism, inspired by the classic game mechanics, and features a strategic depth through the implementation of AI bots.

## Key Features
1. **Dynamic Game Board:** A 2D grid where players strategically place their gems.
2. **Custom AI Bots:** Implemented bots that use a game tree for decision-making, providing a challenging experience.
3. **Overflow Mechanism:** Gems overflow to adjacent cells when the number of gems in a cell reaches a certain threshold.
4. **Winning Condition:** The game ends when all gems on the board are of the same color, and the player corresponding to that color wins.

## Installation

Before running the Jewels Game, ensure you have Python installed on your system. Follow these steps to set up the game environment:

1. **Clone the Repository**:
   Clone the Jewels Game repository to your local machine.

2. **Create a Virtual Environment**:
   Navigate to the project directory and create a virtual environment. This step ensures that the dependencies are installed in an isolated environment specific to this project.
   ```
   python -m venv venv
   ```
   This command creates a virtual environment named `venv` within your project directory.

3. **Activate the Virtual Environment**:
   Before installing dependencies and running the game, activate the virtual environment.
   - On Windows, use:
     ```
     venv\Scripts\activate
     ```
   - On Unix or MacOS, use:
     ```
     source venv/bin/activate
     ```
   You will know that the virtual environment is activated because the prompt will now show the name of the environment (e.g., `(venv)`).

4. **Install Dependencies**:
   With the virtual environment activated, install the required packages:
   ```
   pip install -r requirements.txt
   ```
   This will install Pygame and other required dependencies within the virtual environment.

5. **Deactivating the Virtual Environment** (optional):
   When you're done working with the game, you can deactivate the virtual environment by simply typing:
   ```
   deactivate
   ```
   This will return you to your system's default Python environment.

## How to Run

Navigate to the project directory and execute the following command:

```
python -m jewels_game.game.game.py
```


## Contributions
This project was developed as part of an academic assignment. Therefore, we are not accepting any contributions.


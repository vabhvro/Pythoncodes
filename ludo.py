import random
import os
import time

# Constants
BOARD_SIZE = 30
GOAL = BOARD_SIZE - 1

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, steps):
        self.position += steps
        if self.position > GOAL:
            self.position = GOAL  # Cannot go past the goal

def roll_die():
    return random.randint(1, 6)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(players):
    clear_screen()
    print("Ludo Board")
    for player in players:
        print(f"{player.name}: {player.position}")
    print("\n" + "-" * 20)

def main():
    print("Welcome to Ludo!")
    player1 = Player(input("Enter name for Player 1: "))
    player2 = Player(input("Enter name for Player 2: "))
    players = [player1, player2]
    current_player_index = 0

    while True:
        current_player = players[current_player_index]
        display_board(players)

        input(f"{current_player.name}, press Enter to roll the die...")
        steps = roll_die()
        print(f"{current_player.name} rolled a {steps}!")
        
        current_player.move(steps)

        if current_player.position == GOAL:
            display_board(players)
            print(f"{current_player.name} wins!")
            break

        current_player_index = (current_player_index + 1) % 2  # Switch turn

        time.sleep(1)

if __name__ == "__main__":
    main()

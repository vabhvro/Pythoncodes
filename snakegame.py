import random
import os
import time

# Constants
WIDTH = 10
HEIGHT = 10
SNAKE = 'S'
FOOD = 'F'
EMPTY = '.'

# Game board
board = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]
snake = [(HEIGHT // 2, WIDTH // 2)]  # Starting position of the snake
direction = (0, 1)  # Initial direction: right

def place_food():
    while True:
        food_pos = (random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1))
        if food_pos not in snake:
            return food_pos

def draw_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (y, x) in snake:
                print(SNAKE, end=' ')
            elif (y, x) == food:
                print(FOOD, end=' ')
            else:
                print(EMPTY, end=' ')
        print()

def update_snake():
    head_y, head_x = snake[0]
    new_head = (head_y + direction[0], head_x + direction[1])
    
    if new_head == food:
        snake.insert(0, new_head)
        return True  # Food eaten
    else:
        snake.insert(0, new_head)
        snake.pop()  # Remove the tail
        return False  # Food not eaten

def check_collision():
    head = snake[0]
    if (head[0] < 0 or head[0] >= HEIGHT or
        head[1] < 0 or head[1] >= WIDTH or
        head in snake[1:]):  # Collision with itself
        return True
    return False

# Main game loop
food = place_food()
while True:
    draw_board()
    if check_collision():
        print("Game Over!")
        break
    command = input("Enter direction (w/a/s/d): ").lower()
    
    if command == 'w':
        direction = (-1, 0)  # Up
    elif command == 's':
        direction = (1, 0)   # Down
    elif command == 'a':
        direction = (0, -1)  # Left
    elif command == 'd':
        direction = (0, 1)   # Right

    if update_snake():
        food = place_food()  # Place new food if eaten

    time.sleep(0.5)

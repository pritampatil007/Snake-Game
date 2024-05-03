import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Window size
WIDTH, HEIGHT = 600, 400

# Snake block size
BLOCK_SIZE = 10

# Speed of the snake
SPEED = 15

# Fonts
FONT = pygame.font.SysFont("comicsansms", 35)

# Initialize the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling the game's speed
clock = pygame.time.Clock()

# Function to display message on screen
def message(msg, color):
    mesg = FONT.render(msg, True, color)
    window.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Function to draw snake
def snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])

# Function to run the game
def gameLoop():
    # Snake initial position
    snake_list = []
    length_of_snake = 1

    # Initial position and direction of the snake
    lead_x = WIDTH / 2
    lead_y = HEIGHT / 2
    lead_x_change = 0
    lead_y_change = 0

    # Initial position of food
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    # Game over flag
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = BLOCK_SIZE
                    lead_x_change = 0

        # Update snake's position
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Draw background
        window.fill(BLUE)

        # Draw food
        pygame.draw.rect(window, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Update snake
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for snake's collision with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        # Check for snake's collision with the window boundaries
        if lead_x >= WIDTH or lead_x < 0 or lead_y >= HEIGHT or lead_y < 0:
            game_over = True

        # Check if snake ate the food
        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            length_of_snake += 1

        # Draw snake
        snake(snake_list)

        # Update display
        pygame.display.update()

        # Set the speed of the game
        clock.tick(SPEED)

    # Display game over message
    window.fill(BLUE)
    message("Game Over!", RED)
    pygame.display.update()
    time.sleep(2)

    # Restart the game
    gameLoop()

# Start the game
gameLoop()

# Quit Pygame
pygame.quit()
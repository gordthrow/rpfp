import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Set clock
clock = pygame.time.Clock()

# Set font
font = pygame.font.SysFont(None, 25)

# Define snake and food size
BLOCK_SIZE = 10

# Define function to display score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [0, 0])

# Define function to draw snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, WHITE, [x[0], x[1], snake_block, snake_block])

# Define the game loop
def game_loop():
    game_over = False
    game_close = False

    # Set initial snake position and length
    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2
    x1_change = 0
    y1_change = 0

    # Create initial snake body
    snake_List = []
    Length_of_snake = 1

    # Set initial food position
    foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    # Start the game loop
    while not game_over:

        # Check if game is closed
        while game_close == True:
            screen.fill(BLACK)
            message = font.render("You Lost! Press Q-Quit or C-Play Again", True, WHITE)
            screen.blit(message, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

            # Display score
            display_score(Length_of_snake - 1)

            # Update the display
            pygame.display.update()

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        # Check for boundaries
        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True

        # Update the snake position
        x1 += x1_change
        y1 += y1_change
        
        # Clear the screen
        screen.fill(BLACK)

        # Draw the food
        pygame.draw.rect(screen, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])

        # Update the snake head position
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # If snake has collided with food
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw the snake
        draw_snake(BLOCK_SIZE, snake_List)

        # Display score
        display_score(Length_of_snake - 1)

        # Update the display
        pygame.display.update()

        # If snake has collided with food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            Length_of_snake += 1

        # Set game speed
        clock.tick(20)

    # Quit Pygame
    pygame.quit()

    # Quit Python
    quit()

# Call the game loop
game_loop()
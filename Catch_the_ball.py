import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load images
try:
    player_image = pygame.image.load("C:/Users/Computer/Desktop/Catch the Ball/3.png")
    ball_image = pygame.image.load("C:/Users/Computer/Desktop/Catch the Ball/1.png")
    background_image = pygame.image.load("C:/Users/Computer/Desktop/Catch the Ball/2.png")

except pygame.error as e:
    print(f"Unable to load image: {e}")
    pygame.quit()
    exit()

# Resize images
player_image = pygame.transform.scale(player_image, (50, 50))
ball_image = pygame.transform.scale(ball_image, (30, 30))
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Player settings
player_width = 50
player_height = 50
player_x = screen_width // 2
player_y = screen_height - player_height
player_speed = 10

# Ball settings
ball_width = 30
ball_height = 30
ball_x = random.randint(0, screen_width - ball_width)
ball_y = -ball_height
ball_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 48) #Font for the title

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    ball_y += ball_speed
    if ball_y > screen_height:
        ball_y = -ball_height
        ball_x = random.randint(0, screen_width - ball_width)

    # Collision detection
    if (player_x < ball_x < player_x + player_width or player_x < ball_x + ball_width < player_x + player_width) and (player_y < ball_y < player_y + player_height):
        score += 1
        ball_y = -ball_height
        ball_x = random.randint(0, screen_width - ball_width)

    # Drawing
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(ball_image, (ball_x, ball_y))

    #Draw the title
    title_text = title_font.render("Mariya Game", True, (255, 255, 255))
    screen.blit(title_text, (screen_width // 2 -title_text.get_width() // 2, 10))
    
    #Draw the score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 50)) #Adjusted to not overlap with the title

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
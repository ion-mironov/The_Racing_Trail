import pygame


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)



""" Set main window dimensions """
WIDTH, HEIGHT = 1024, 576
pygame.display.set_caption("The Racing Trail")
screen = pygame.display.set_mode((WIDTH, HEIGHT))


""" Set main menu images """
background = pygame.image.load("assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

main_title_image = pygame.image.load("assets/main_title_image.png")
title_rect = main_title_image.get_rect(center=(WIDTH // 2, HEIGHT // 5))

new_game_image = pygame.image.load("assets/new_game_image.png")
new_game_rect = new_game_image.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))

load_game_image = pygame.image.load("assets/load_game_image.png")
load_game_rect = load_game_image.get_rect(center=(WIDTH // 2, HEIGHT // 1.3))

exit_game_image = pygame.image.load("assets/exit_game_image.png")
exit_game_rect = exit_game_image.get_rect(center=(WIDTH // 2, HEIGHT // 1.15))

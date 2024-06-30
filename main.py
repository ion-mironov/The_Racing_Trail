import pygame

from animations import *
from game_functions import *
from parameters import *
from random_events import *
import beginning


pygame.init()


# Main Menu images
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


# Game states
MAIN_MENU = "main_menu"
RACING = "racing"
UPGRADING = "upgrading"
EVENT = "event"
state = MAIN_MENU


# ============================================================================================= #
""" Main game loop """
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			exit()

		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				if is_hovered(new_game_rect):
					beginning.start_beginning(screen)

				elif is_hovered(load_game_rect):
					pass

				elif is_hovered(exit_game_rect):
					running = False


	if state == MAIN_MENU:
		screen.blit(background, (0, 0))							# Display background image
		screen.blit(main_title_image, title_rect)				# Display Title text image
		screen.blit(new_game_image, new_game_rect)				# Display New Game text image
		screen.blit(load_game_image, load_game_rect)			# Display Load Game text image
		screen.blit(exit_game_image, exit_game_rect)			# Display Exit Game text image


		# New Game button shimmer effect
		if is_hovered(new_game_rect):
			if not hovered_new:
				shimmer_progress_new = 0
				hovered_new = True
			if shimmer_progress_new < 1:
				shimmer_progress_new += 0.01
				draw_shimmer(screen, new_game_rect, shimmer_progress_new)
		else:
			hovered_new = False


		# Load Game button shimmer effect
		if is_hovered(load_game_rect):
			if not hovered_load:
				shimmer_progress_load = 0
				hovered_load = True
			if shimmer_progress_load < 1:
				shimmer_progress_load += 0.01
				draw_shimmer(screen, load_game_rect, shimmer_progress_load)
		else:
			hovered_load = False


		# Exit Game button shimmer effect
		if is_hovered(exit_game_rect):
			if not hovered_exit:
				shimmer_progress_exit = 0
				hovered_exit = True
			if shimmer_progress_exit < 1:
				shimmer_progress_exit += 0.01
				draw_shimmer(screen, exit_game_rect, shimmer_progress_exit)
		else:
			hovered_exit = False


	elif state == RACING:
		# Handle racing events
		pass

	elif state == UPGRADING:
		# Handle upgrading logic
		pass

	elif state == EVENT:
		# Handle random events
		pass
	
	pygame.display.flip()

pygame.quit()

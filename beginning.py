import pygame
from parameters import *
from game_functions import text_wrap

def start_beginning(screen):

	# Level name text settings
	font = pygame.font.Font(None, 40)
	beginning_text_surface = font.render("A New Beginning", True, (CYAN))
	beginning_text_rect = beginning_text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 20))


	# Dialogue text settings
	font = pygame.font.SysFont('Arial', 20)
	beginning_dialogue_1 = "You're a newly-graduated college student. After years of boring schoolwork, watching clichéd car racing movies, and playing similarly-themed racing games, you decided it was time to go out and see if you could turn those car racing fantasies into reality. As a graduation gift, your uncle gives you a gently-used 1997 Honda Civic."


	garage_with_civic = pygame.image.load("assets/garage_with_civic.png")
	garage_with_civic_rect = garage_with_civic.get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.6))


	""" Beginning game loop """
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		screen.fill((0, 0, 0))

		screen.blit(beginning_text_surface, beginning_text_rect)
		screen.blit(garage_with_civic, garage_with_civic_rect.topleft)

		text_wrap(screen, beginning_dialogue_1, (screen.get_width() // 10, screen.get_height() // 9), font, WHITE, screen.get_width() - screen.get_width() // 5)
		
		pygame.display.flip()

	pygame.quit()

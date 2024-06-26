import pygame

from game_functions import *
from parameters import *
import fixing



# 'Beginning' level images, dialogue text, and game loop
def start_beginning(screen):

	# === SHIMMER FUNCTION ========================================================================================================== #
	shimmer_progress_continue = 0		# Initialize shimmer progress
	hovered_continue = False			# Check if cursor is over 'continue' arrow (used to reset hover effect)


	# === DIALOGUE TEXT ============================================================================================================= #
	font = pygame.font.Font(None, 40)
	beginning_text_surface = font.render("A New Beginning", True, (CYAN))
	beginning_text_rect = beginning_text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 20))

	font = pygame.font.SysFont('Arial', 20)
	beginning_dialogue_1 = "You're a newly-graduated college student. After years of boring schoolwork, watching clichéd car racing movies, and playing similarly-themed racing games, you decided it was time to go out and see if you could turn those car racing fantasies into reality. As a graduation gift, your uncle gives you a gently-used 1997 Honda Civic."

	beginning_dialogue_2 = "You decide that a few changes need to be made, so you begin to get your hands dirty..."


	# === IMAGES ==================================================================================================================== #
	""" Yellow Civic in garage """
	garage_with_civic = pygame.image.load("assets/garage_with_civic.png")
	garage_with_civic_rect = garage_with_civic.get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.5))

	""" 'Continue' arrow button """
	continue_arrow = pygame.image.load("assets/continue_arrow.png")
	continue_arrow_rect = continue_arrow.get_rect(bottomright=(screen.get_width() // 1.005, screen.get_height() // 1.01))	# Display arrow at bottom right corner of screen



	# === 'BEGINNING' GAME LOOP ===================================================================================================== #
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			
			# Continue arrow button
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					if is_hovered(continue_arrow_rect):
						fixing.start_fixing(screen)

		screen.fill((0, 0, 0))


		# Display images at their predefined position
		screen.blit(garage_with_civic, garage_with_civic_rect.topleft)
		screen.blit(continue_arrow,continue_arrow_rect.topleft)
		screen.blit(beginning_text_surface, beginning_text_rect)


		# Use 'text_wrap' function to display text at a set position and have it auto-wrap to the next line
		text_wrap(screen, beginning_dialogue_1, (screen.get_width() // 10, screen.get_height() // 9), font, WHITE, screen.get_width() - screen.get_width() // 5)
		text_wrap(screen, beginning_dialogue_2, (screen.get_width() // 10, screen.get_height() // 3.5), font, WHITE, screen.get_width() - screen.get_width() // 5)


		""" 'Continue' arrow shimmer effect """
		if is_hovered(continue_arrow_rect):
			if not hovered_continue:
				shimmer_progress_continue = 0
				hovered_continue = True
			if shimmer_progress_continue < 1:
				shimmer_progress_continue += 0.005
				draw_shimmer(screen, continue_arrow_rect, shimmer_progress_continue)
		else:
			hovered_continue = False

		pygame.display.flip()

	pygame.quit()

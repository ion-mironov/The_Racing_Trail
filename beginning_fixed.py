import pygame

from game_functions import *
from parameters import *
import cruising


# Define cursors
arrow_cursor = pygame.SYSTEM_CURSOR_ARROW
hand_cursor = pygame.SYSTEM_CURSOR_HAND


# 'Beginning' level images, dialogue text, and game loop
def fixed_civic(screen):

	# === SHIMMER FUNCTION ========================================================================================================== #
	shimmer_progress_continue = 0		# Initialize shimmer progress
	hovered_continue = False			# Check if cursor is over 'continue' arrow (used to reset hover effect)


	# === DIALOGUE TEXT ============================================================================================================= #
	font = pygame.font.SysFont('Arial', 20)
	beginning_fixed_dialogue_1 = "You installed a new Cold Air Intake (CAI) kit and stainless steel cat-back exhaust, taking the car's stock engine with its 106 horsepower and 103 lb-ft of torque up to a more acceptable 166 HP and 159 lb-ft of torque. Along with that, you also gave it a new splash of paint, a lowered suspension, and some custom wheels. Now, the car finally feels likes it's yours."

	beginning_fixed_dialogue_2 = "Now, it is time to hit the open road and head west!"


	# === IMAGES ==================================================================================================================== #
	""" Yellow Civic in garage """
	garage_with_civic = pygame.image.load("assets/blue_civic_in_garage.png")
	garage_with_civic_rect = garage_with_civic.get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.45))

	""" 'Continue' arrow button """
	continue_arrow = pygame.image.load("assets/continue_arrow.png")
	continue_arrow_rect = continue_arrow.get_rect(bottomright=(screen.get_width() // 1.005, screen.get_height() // 1.01))



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
						cruising.start_cruising(screen)

		screen.fill((0, 0, 0))


		# Display images at their predefined position
		screen.blit(garage_with_civic, garage_with_civic_rect.topleft)
		screen.blit(continue_arrow,continue_arrow_rect.topleft)


		# Use 'text_wrap' function to display text at a set position and have it auto-wrap to the next line
		text_wrap(screen, beginning_fixed_dialogue_1, (screen.get_width() // 10, screen.get_height() // 9), font, WHITE, screen.get_width() - screen.get_width() // 5)
		text_wrap(screen, beginning_fixed_dialogue_2, (screen.get_width() // 10, screen.get_height() // 3), font, WHITE, screen.get_width() - screen.get_width() // 5)


		cursor_changed = False

		""" 'Continue' arrow shimmer effect """
		if is_hovered(continue_arrow_rect):
			if not hovered_continue:
				shimmer_progress_continue = 0
				hovered_continue = True

			if shimmer_progress_continue < 1:
				shimmer_progress_continue += 0.02
				draw_shimmer(screen, continue_arrow_rect, shimmer_progress_continue)

			pygame.mouse.set_cursor(hand_cursor)
			cursor_changed = True

		else:
			hovered_continue = False

		if not cursor_changed:
			pygame.mouse.set_cursor(arrow_cursor)

		pygame.display.flip()

	pygame.quit()

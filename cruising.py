import os
import pygame

from game_functions import *
from parameters import *


# Define cursors
arrow_cursor = pygame.SYSTEM_CURSOR_ARROW
hand_cursor = pygame.SYSTEM_CURSOR_HAND


# =========================================================================== #
# === GIF animation function ================================================ #
def load_frames(folder, prefix):
	frames = []
	for filename in sorted(os.listdir(folder)):
		if filename.startswith(prefix):
			img = pygame.image.load(os.path.join(folder, filename))
			frames.append(img)
	return frames


# =========================================================================== #
#  === 'Cruising' level animation, text, and game loop ====================== #
def start_cruising(screen):

	# =============================================================================================================================== #
	# === SHIMMER FUNCTION ========================================================================================================== #
	shimmer_progress_continue = 0
	hovered_continue = False
	show_new_image = False


	# =============================================================================================================================== #
	# === DIALOGUE TEXT ============================================================================================================= #
	font = pygame.font.SysFont('Arial', 24)
	cruising_text = "You grin from ear to ear as you cruise down the road, tunes thumping from the radio as your car glides along the pavement without a problem, all the modifications you did seeming to sing in perfect harmony."


	# =============================================================================================================================== #
	# === ANIMATION ================================================================================================================= #
	""" Define image frames for animation """
	frames = load_frames("assets/blue_civic_cruising/", "frame_")
	frame_count = len(frames)
	current_frame = 0

	""" Timing for frame updates """
	frame_delay = 100   # milliseconds before displaying next frame in sequence
	last_update = pygame.time.get_ticks()

	""" Get rect from first image frame to position animation """
	civic_cruising_rect = frames[0].get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.5))


	# =============================================================================================================================== #
	# === 'CONTINUE' ARROW ========================================================================================================== #
	continue_arrow = pygame.image.load("assets/continue_arrow.png")
	continue_arrow_rect = continue_arrow.get_rect(bottomright=(screen.get_width() // 1.005, screen.get_height() // 1.01))


	# Load the new image to display when the arrow is clicked
	new_image = pygame.image.load("assets/new_image.png")
	new_image_rect = new_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))



	# =============================================================================================================================== #
	# === 'CRUISING' GAME LOOP ====================================================================================================== #
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

			# 'Continue' arrow button
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					if is_hovered(continue_arrow_rect):
						show_new_image = True


		screen.fill((0, 0, 0))

		if not show_new_image:
			now = pygame.time.get_ticks()
			if now - last_update > frame_delay:
				current_frame = (current_frame + 1) % frame_count
				last_update = now


		# Display animation, dialogue text, and 'Continue' arrow
			screen.blit(frames[current_frame], civic_cruising_rect.topleft)
		else:
			screen.blit(new_image, new_image_rect)


		screen.blit(continue_arrow,continue_arrow_rect.topleft)
		text_wrap(screen, cruising_text, (screen.get_width() // 10, screen.get_height() // 9), font, WHITE, screen.get_width() - screen.get_width() // 5)


		""" 'Continue' arrow shimmer effect """
		if is_hovered(continue_arrow_rect):
			shimmer_progress_continue += 0.003
			draw_shimmer(screen, continue_arrow_rect, shimmer_progress_continue)
			pygame.mouse.set_cursor(hand_cursor)
		else:
			pygame.mouse.set_cursor(arrow_cursor)

		pygame.display.flip()

	pygame.quit()

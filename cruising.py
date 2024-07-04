import os
import pygame

from game_functions import *
from parameters import *


# Define cursors
arrow_cursor = pygame.SYSTEM_CURSOR_ARROW
hand_cursor = pygame.SYSTEM_CURSOR_HAND


# === GIF animation function ================================================ #
def load_frames(folder, prefix):
	frames = []
	for filename in sorted(os.listdir(folder)):
		if filename.startswith(prefix):
			img = pygame.image.load(os.path.join(folder, filename))
			frames.append(img)
	return frames


#  === 'Cruising' level animation, text, and game loop ====================== #
def start_cruising(screen):

	# === SHIMMER FUNCTION ========================================================================================================== #
	shimmer_progress_continue = 0
	hovered_continue = False


	# === DIALOGUE TEXT ============================================================================================================= #
	font = pygame.font.SysFont('Arial', 24)
	cruising_text = "Enter text here?"


	# === ANIMATION ================================================================================================================= #
	""" Define image frames for animation """
	frames = load_frames("assets/blue_civic_cruising/", "frame_")
	frame_count = len(frames)
	current_frame = 0

	""" Timing for frame updates """
	frame_delay = 100   # milliseconds
	last_update = pygame.time.get_ticks()

	""" Get rect from first GIF frame to position animation """
	civic_cruising_rect = frames[0].get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.5))


	# === 'CONTINUE' ARROW ========================================================================================================== #
	continue_arrow = pygame.image.load("assets/continue_arrow.png")
	continue_arrow_rect = continue_arrow.get_rect(bottomright=(screen.get_width() // 1.005, screen.get_height() // 1.01))


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
						pass

		screen.fill((0, 0, 0))


		# Update the frame animation index and stop once the final frame is displayed
		now = pygame.time.get_ticks()
		if now - last_update > frame_delay:
			current_frame = (current_frame + 1) % frame_count
			last_update = now


		# Display animation, dialogue text, and 'Continue' arrow
		screen.blit(frames[current_frame], civic_cruising_rect.topleft)
		text_wrap(screen, cruising_text, (screen.get_width() // 10, screen.get_height() // 9), font, WHITE, screen.get_width() - screen.get_width() // 5)
		screen.blit(continue_arrow,continue_arrow_rect.topleft)


		""" 'Continue' arrow shimmer effect """
		if is_hovered(continue_arrow_rect):
			if not hovered_continue:
				shimmer_progress_continue = 0
				hovered_continue = True
			if shimmer_progress_continue < 1:
				shimmer_progress_continue += 0.01
				draw_shimmer(screen, continue_arrow_rect, shimmer_progress_continue)
			pygame.mouse.set_system_cursor(hand_cursor)
			cursor_changed = True
		else:
			hovered_continue = False
			pygame.mouse.set_system_cursor(arrow_cursor)

		if not cursor_changed:
			pygame.mouse.set_system_cursor(arrow_cursor)

		pygame.display.flip()

	pygame.quit()

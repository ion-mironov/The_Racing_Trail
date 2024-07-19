import os
import pygame

from game_functions import *
from parameters import *
import broken_down



# Define cursors
arrow_cursor = pygame.SYSTEM_CURSOR_ARROW
hand_cursor = pygame.SYSTEM_CURSOR_HAND



# ═══════════════════════════════════════════════════════════════════════════ #
# ═══ GIF ANIMATION FUNCTION ════════════════════════════════════════════════ #
def load_frames(folder, prefix):
	frames = []
	for filename in sorted(os.listdir(folder)):
		if filename.startswith(prefix):
			img = pygame.image.load(os.path.join(folder, filename))
			frames.append(img)
	return frames


# ═══════════════════════════════════════════════════════════════════════════ #
# ═══ LEVEL IMAGES, DIALOGUE TEXT, AND GAME LOOP ════════════════════════════ #
def start_cruising(screen):

	# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ SHIMMER FUNCTION ═════════════════════════════════════════════════════════════════════════════════════════════ #
	shimmer_progress_continue = 0
	hovered_continue = False



	# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ DIALOGUE TEXT ════════════════════════════════════════════════════════════════════════════════════════════════ #
	font = pygame.font.SysFont('Arial', 24)
	cruising_text = "You grin from ear to ear as you cruise down the road, tunes thumping from the radio as your car glides along the pavement, the engine and exhaust note both complementing each other as all your modifications work in perfect harmony."



	# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ ANIMATION ════════════════════════════════════════════════════════════════════════════════════════════════════ #
	""" Define image frames for animation """
	frames = load_frames("assets/blue_civic_cruising/", "day_")
	frame_count = len(frames)
	current_frame = 0

	""" Timing for frame updates """
	frame_delay = 100   # milliseconds before displaying next frame in sequence
	last_update = pygame.time.get_ticks()

	""" Get rect from first image frame to position animation """
	civic_cruising_rect = frames[0].get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.5))



	# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ 'CONTINUE' ARROW ═════════════════════════════════════════════════════════════════════════════════════════════ #
	continue_arrow = pygame.image.load("assets/continue_arrow.png")
	continue_arrow_rect = continue_arrow.get_rect(bottomright=(screen.get_width() // 1.005, screen.get_height() // 1.01))



	# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ GAME LOOP ════════════════════════════════════════════════════════════════════════════════════════════════════ #
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					if is_hovered(continue_arrow_rect):
						broken_down.broken_down_civic(screen)


		# ─── ▼ Display all necessary images and text ▼ ───────────────────────────── #
		screen.fill((0, 0, 0))

		now = pygame.time.get_ticks()
		if now - last_update > frame_delay:
			current_frame = (current_frame + 1) % frame_count
			last_update = now

		screen.blit(frames[current_frame], civic_cruising_rect.topleft)
		screen.blit(continue_arrow, continue_arrow_rect.topleft)

		text_wrap(screen, cruising_text, (screen.get_width() // 10, screen.get_height() // 9), font, WHITE, screen.get_width() - screen.get_width() // 5)
		# ─── ▲ Display all necessary images and text ▲ ───────────────────────────── #


		# ─── ▼ 'Continue' arrow shimmer effect ▼ ─────────────────────────────────── #
		cursor_changed = False

		if is_hovered(continue_arrow_rect):
			if not hovered_continue:
				shimmer_progress_continue = 0
				hovered_continue = True

			if shimmer_progress_continue < 1:
				shimmer_progress_continue += 0.005
				draw_shimmer(screen, continue_arrow_rect, shimmer_progress_continue)

			pygame.mouse.set_cursor(hand_cursor)
			cursor_changed = True

		else:
			hovered_continue = False

		if not cursor_changed:
			pygame.mouse.set_cursor(arrow_cursor)
		# ─── ▲ 'Continue' arrow shimmer effect ▲ ─────────────────────────────────── #


		pygame.display.flip()

	pygame.quit()

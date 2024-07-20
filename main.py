import pygame

from game_functions import *
from parameters import *
import beginning


pygame.init()


# Define cursors
arrow_cursor = pygame.SYSTEM_CURSOR_ARROW
hand_cursor = pygame.SYSTEM_CURSOR_HAND



# ═══════════════════════════════════════════════════════════════════════════ #
# ═══ IMAGES ════════════════════════════════════════════════════════════════ #
background = pygame.image.load("assets/main_menu/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

main_title_image = pygame.image.load("assets/main_menu/main_title_image.png")
title_rect = main_title_image.get_rect(center=(WIDTH // 2, HEIGHT // 5))

new_game_image = pygame.image.load("assets/main_menu/new_game_image.png")
new_game_rect = new_game_image.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))

load_game_image = pygame.image.load("assets/main_menu/load_game_image.png")
load_game_rect = load_game_image.get_rect(center=(WIDTH // 2, HEIGHT // 1.3))

exit_game_image = pygame.image.load("assets/main_menu/exit_game_image.png")
exit_game_rect = exit_game_image.get_rect(center=(WIDTH // 2, HEIGHT // 1.15))



# ═══════════════════════════════════════════════════════════════════════════ #
# ═══ SHIMMER FUNCTION ══════════════════════════════════════════════════════ #

""" Initialize shimmer progress """
shimmer_progress_new = 0
shimmer_progress_load = 0
shimmer_progress_exit = 0

# Check if cursor is over images (used to reset hover shimmer effect)
hovered_new = False
hovered_load = False
hovered_exit = False



# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
# ═══ GAME LOOP ═════════════════════════════════════════════════════════════════════════════════════════════════════════ #
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			exit()

		# Continue arrow button
		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				if is_hovered(new_game_rect):
					beginning.start_beginning(screen)

				elif is_hovered(load_game_rect):
					pass

				elif is_hovered(exit_game_rect):
					running = False


	screen.blit(background, (0, 0))							# Display background image
	screen.blit(main_title_image, title_rect)				# Display Title text image
	screen.blit(new_game_image, new_game_rect)				# Display New Game text image
	screen.blit(load_game_image, load_game_rect)			# Display Load Game text image
	screen.blit(exit_game_image, exit_game_rect)			# Display Exit Game text image

	cursor_changed = False									# Set default state of system cursor



	# ═══ ↓↓↓ Main Menu buttons with shimmer effects ↓↓↓ ══════════════════════════════════════ #

	# ─── ▼ 'New Game' button shimmer effect ▼ ──────────────────────────────────── #
	if is_hovered(new_game_rect):
		if not hovered_new:
			shimmer_progress_new = 0
			hovered_new = True
		if shimmer_progress_new < 1:
			shimmer_progress_new += 0.01
			draw_shimmer(screen, new_game_rect, shimmer_progress_new)

		""" Change to 'hand' cursor when hovering over a selectable item """
		pygame.mouse.set_cursor(hand_cursor)
		cursor_changed = True

	else:
		hovered_new = False
	# ─── ▲ 'New Game' button shimmer effect ▲ ──────────────────────────────────── #



	# ─── ▼ 'Load Game' button shimmer effect ▼ ─────────────────────────────────── #
	if is_hovered(load_game_rect):
		if not hovered_load:
			shimmer_progress_load = 0
			hovered_load = True

		if shimmer_progress_load < 1:
			shimmer_progress_load += 0.01
			draw_shimmer(screen, load_game_rect, shimmer_progress_load)

		""" Change to 'hand' cursor when hovering over a selectable item """
		pygame.mouse.set_cursor(hand_cursor)
		cursor_changed = True

	else:
		hovered_load = False
	# ─── ▲ 'Load Game' button shimmer effect ▲ ─────────────────────────────────── #



	# ─── ▼ 'Exit Game' button shimmer effect ▼ ─────────────────────────────────── #
	if is_hovered(exit_game_rect):
		if not hovered_exit:
			shimmer_progress_exit = 0
			hovered_exit = True

		if shimmer_progress_exit < 1:
			shimmer_progress_exit += 0.01
			draw_shimmer(screen, exit_game_rect, shimmer_progress_exit)

		""" Change to 'hand' cursor when hovering over a selectable item """
		pygame.mouse.set_cursor(hand_cursor)
		cursor_changed = True

	else:
		hovered_exit = False
	
	if not cursor_changed:
		""" Change to 'arrow' cursor when not hovering over a selectable item """
		pygame.mouse.set_cursor(arrow_cursor)
	# ─── ▲ 'Exit Game' button shimmer effect ▲ ─────────────────────────────────── #

	# ═══ ↑↑↑ Main Menu buttons with shimmer effects ↑↑↑ ══════════════════════════════════════ #


	pygame.display.flip()

pygame.quit()

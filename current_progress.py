from sys import exit
import pygame

from game_functions import *
from parameters import *



# Define cursors
arrow_cursor = pygame.SYSTEM_CURSOR_ARROW


# ═══════════════════════════════════════════════════════════════════════════ #
# ═══ LEVEL IMAGES, DIALOGUE TEXT, AND GAME LOOP ════════════════════════════ #
def end_current_progress(screen):

	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ DIALOGUE TEXT ═════════════════════════════════════════════════════════════════════════════════════════════════ #
	font = pygame.font.Font("assets/arial.ttf", 22)
	end_current_progress_text = "That's it so far! Thank you for checking out what I've created up to this point!"



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ GAME LOOP ═════════════════════════════════════════════════════════════════════════════════════════════════════ #
	running = True
	while running:
		pygame.mouse.set_cursor(arrow_cursor)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()


		# ─── ▼ Display all necessary images and text ▼ ───────────────────────────── #
		screen.fill((0, 0, 0))

		text_wrap(screen, end_current_progress_text, (screen.get_width() // 10, screen.get_height() // 9), font, WHITE, screen.get_width() - screen.get_width() // 5)
		# ─── ▲ Display all necessary images and text ▲ ───────────────────────────── #


		pygame.display.flip()

	pygame.quit()

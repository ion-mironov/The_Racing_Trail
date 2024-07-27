from sys import exit
import pygame

from game_functions import *
from parameters import *
import first_time_sale



# Define cursors
arrow_cursor = pygame.SYSTEM_CURSOR_ARROW
hand_cursor = pygame.SYSTEM_CURSOR_HAND



# ═══════════════════════════════════════════════════════════════════════════ #
# ═══ LEVEL IMAGES, DIALOGUE TEXT, AND GAME LOOP ════════════════════════════ #
def truck_interior(screen):

	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ SHIMMER FUNCTION ══════════════════════════════════════════════════════════════════════════════════════════════ #
	shimmer_progress_continue = 0
	hovered_continue = False



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ DIALOGUE TEXT ═════════════════════════════════════════════════════════════════════════════════════════════════ #
	font = pygame.font.Font("assets/arial.ttf", 20)
	truck_interior_dialogue_1 = "Even though you've never met this man, despite a nagging feeling that you have seen him before, you decide it's perfectly safe and drive your car up the loading ramps and into the truck's interior. It's only then that you noticed that the mysterious man is now standing in front of your car. How'd he get inside so fast without you noticing?"

	truck_interior_dialogue_2 = "\"Let's do some business then, eh!\", says the seller. \"I reserved some items, just for you! My other customers don't know about these, heh heh heh.\" You can almost sense a grin hidden behind his mask as you look over the selection of parts he has to offer."



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ IMAGES ════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	""" Blue Civic inside truck container """
	truck_interior = pygame.image.load("assets/truck_interior_and_civic.png")
	truck_interior_rect = truck_interior.get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.45))

	""" 'Continue' arrow button """
	continue_arrow = pygame.image.load("assets/continue_arrow.png")
	continue_arrow_rect = continue_arrow.get_rect(bottomright=(screen.get_width() // 1.005, screen.get_height() // 1.01))



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ GAME LOOP ═════════════════════════════════════════════════════════════════════════════════════════════════════ #
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					if is_hovered(continue_arrow_rect):
						first_time_sale.parts_sale(screen)


		# ─── ▼ Display all necessary images and text ▼ ───────────────────────────── #
		screen.fill((0, 0, 0))

		text_wrap(screen, truck_interior_dialogue_1, (screen.get_width() // 10, screen.get_height() // 20), font, WHITE, screen.get_width() - screen.get_width() // 5)
		text_wrap(screen, truck_interior_dialogue_2, (screen.get_width() // 10, screen.get_height() // 3), font, WHITE, screen.get_width() - screen.get_width() // 5)

		screen.blit(truck_interior, truck_interior_rect.topleft)
		screen.blit(continue_arrow, continue_arrow_rect.topleft)
		# ─── ▲ Display all necessary images and text ▲ ───────────────────────────── #



		# ─── ▼ 'Continue' arrow shimmer effect ▼ ─────────────────────────────────── #
		cursor_changed = False

		if is_hovered(continue_arrow_rect):
			if not hovered_continue:
				shimmer_progress_continue = 0
				hovered_continue = True

			if shimmer_progress_continue < 1:
				shimmer_progress_continue += 0.015
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

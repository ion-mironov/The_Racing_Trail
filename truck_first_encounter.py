from sys import exit
import pygame

from ui_elements import *
from parameters import *
import truck_interior_and_civic



# Define cursors
arrow_cursor = pygame.SYSTEM_CURSOR_ARROW
hand_cursor = pygame.SYSTEM_CURSOR_HAND



# ═══════════════════════════════════════════════════════════════════════════ #
# ═══ LEVEL IMAGES, DIALOGUE TEXT, AND GAME LOOP ════════════════════════════ #
def merchant_truck(screen):

	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ SHIMMER FUNCTION ══════════════════════════════════════════════════════════════════════════════════════════════ #
	shimmer_progress_continue = 0
	hovered_continue = False



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ DIALOGUE TEXT ═════════════════════════════════════════════════════════════════════════════════════════════════ #
	font = pygame.font.Font("assets/arial.ttf", 20)
	truck_encounter_dialogue_1 = "After a few miles, you come across a truck with a strangely familiar logo on its side and an equally strangely familiar masked occupant in the driver's seat. As you get closer, the back door of the truck opens up and you see a slew of car parts and mechanic's tools. You then notice that the driver, wearing a long, thick leather coat and a purple bandana mask covering the lower half of his face, is now suddenly outside your window."

	truck_encounter_dialogue_2 = "\"Welcome!\", he says in a familiar accent. \"Come inside! Got a selection of good things on sale, driver!\""



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ IMAGES ════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	""" Truck and blue Civic at night """
	truck_civic_night = pygame.image.load("assets/truck_and_civic_night.png")
	truck_civic_night_rect = truck_civic_night.get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.45))

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
						truck_interior_and_civic.truck_interior(screen)


		# ─── ▼ Display all necessary images and text ▼ ───────────────────────────── #
		screen.fill((0, 0, 0))

		text_wrap(screen, truck_encounter_dialogue_1, (screen.get_width() // 10, screen.get_height() // 20), font, WHITE, screen.get_width() - screen.get_width() // 5)
		text_wrap(screen, truck_encounter_dialogue_2, (screen.get_width() // 10, screen.get_height() // 3), font, WHITE, screen.get_width() - screen.get_width() // 5)

		screen.blit(truck_civic_night, truck_civic_night_rect.topleft)
		screen.blit(continue_arrow, continue_arrow_rect.topleft)
		# ─── ▲ Display all necessary images and text ▲ ───────────────────────────── #



		# ─── ▼ 'Continue' arrow shimmer effect ▼ ─────────────────────────────────── #
		cursor_changed = False

		if is_hovered(continue_arrow_rect):
			if not hovered_continue:
				shimmer_progress_continue = 0
				hovered_continue = True

			if shimmer_progress_continue < 1:
				shimmer_progress_continue += 0.007
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

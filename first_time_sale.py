from sys import exit
import pygame

from game_functions import *
from parameters import *



# Define cursors
arrow_cursor = pygame.SYSTEM_CURSOR_ARROW
hand_cursor = pygame.SYSTEM_CURSOR_HAND



# Define parts data
parts = [
	{"name": "Brakes", "cost": 200, "image": pygame.image.load("assets/brakes.png")},
	{"name": "Engine", "cost": 1000, "image": pygame.image.load("assets/engine.png")},
	{"name": "Exhaust System", "cost": 500, "image": pygame.image.load("assets/muffler.png")},
	{"name": "Performance Tires", "cost": 450, "image": pygame.image.load("assets/wheels.png")},
]

# Player's money
player_money = 600



# ═══════════════════════════════════════════════════════════════════════════ #
# ═══ LEVEL IMAGES, DIALOGUE TEXT, AND GAME LOOP ════════════════════════════ #
def parts_sale(screen):
	global player_money  # Declare player_money as global

	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ SHIMMER FUNCTION ══════════════════════════════════════════════════════════════════════════════════════════════ #
	shimmer_progress_continue = 0
	hovered_continue = False


	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ IMAGES ════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# Set margin from the left side and the gap between images
	left_margin = 50
	top_margin = 50
	gap = 20


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
					for part in parts:
							part_rect = part["image"].get_rect(topleft=(left_margin, parts.index(part) * (part["image"].get_height() + gap) + top_margin))
							if is_hovered(part_rect):
								if player_money >= part["cost"]:
									player_money -= part["cost"]
									print(f"Bought {part['name']} for ${part['cost']}")
								else:
									print(f"Not enough money to buy {part['name']}")
					if is_hovered(continue_arrow_rect):
						pass


		# ─── ▼ Display all necessary images and text ▼ ───────────────────────────── #
		screen.fill((0, 0, 0))


		# Display parts and costs
		font = pygame.font.SysFont('Arial', 24)
		y_offset = top_margin
		for part in parts:
			# Blit part image
			part_rect = part["image"].get_rect(topleft=(left_margin, y_offset))
			screen.blit(part["image"], part_rect.topleft)

			# Blit part name and cost
			text_surface = font.render(f"{part['name']} - ${part['cost']}", True, (255, 255, 255))
			text_rect = text_surface.get_rect(topleft=(left_margin + part_rect.width + 10, y_offset + part_rect.height // 4))
			screen.blit(text_surface, text_rect)

			y_offset += part_rect.height + gap
		
		# Display player's money
		money_surface = font.render(f"Player's money: ${player_money}", True, (255, 255, 255))
		money_rect = money_surface.get_rect(topright=(screen.get_width() - left_margin, top_margin))
		screen.blit(money_surface, money_rect)


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

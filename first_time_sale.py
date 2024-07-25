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
	{"name": "Exhaust", "cost": 500, "image": pygame.image.load("assets/muffler.png")},
	{"name": "Tires", "cost": 450, "image": pygame.image.load("assets/wheels.png")},
]

# Player's money
player_money = 600



# ═══════════════════════════════════════════════════════════════════════════ #
# ═══ POP-UP WINDOW ═════════════════════════════════════════════════════════ #
def draw_popup(screen, message):
	popup_width, popup_height = 300, 150
	popup_surface = pygame.Surface((popup_width, popup_height))
	popup_surface.fill((255, 0, 0))  # Red background for the popup
	popup_rect = popup_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

	# Draw border
	border_thickness = 5
	border_color = (255, 255, 255)
	border_rect = pygame.Rect(
		popup_rect.left - border_thickness,
		popup_rect.top - border_thickness,
		popup_width + 2 * border_thickness,
		popup_height + 2 * border_thickness
	)
	pygame.draw.rect(screen, border_color, border_rect)
	screen.blit(popup_surface, popup_rect)

	# Draw message
	font = pygame.font.SysFont('Arial', 24)
	text_surface = font.render(message, True, (255, 255, 255))
	text_rect = text_surface.get_rect(center=(popup_rect.centerx, popup_rect.centery - 20))
	screen.blit(text_surface, text_rect)

	# Draw button
	button_rect = pygame.Rect(popup_rect.centerx - 50, popup_rect.centery + 20, 100, 40)
	pygame.draw.rect(screen, (255, 255, 255), button_rect)
	button_text = font.render("Close", True, (0, 0, 0))
	button_text_rect = button_text.get_rect(center=button_rect.center)
	screen.blit(button_text, button_text_rect)

	return button_rect



# ═══════════════════════════════════════════════════════════════════════════ #
# ═══ LEVEL IMAGES, DIALOGUE TEXT, AND GAME LOOP ════════════════════════════ #
def parts_sale(screen):
	global player_money			# Declare `player_money` as global

	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ SHIMMER FUNCTION ══════════════════════════════════════════════════════════════════════════════════════════════ #
	shimmer_progress_continue = 0
	hovered_continue = False


	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ IMAGES ════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	top_margin = 50				# Set gap from the top to first image
	left_margin = 50			# Set gap from left side of images
	gap = 20					# Set gap for in-between images


	""" 'Continue' arrow button """
	continue_arrow = pygame.image.load("assets/continue_arrow.png")
	continue_arrow_rect = continue_arrow.get_rect(bottomright=(screen.get_width() // 1.005, screen.get_height() // 1.01))

	popup_visible = False
	popup_message = ""
	button_rect = None



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
					if popup_visible:
						if button_rect and button_rect.collidepoint(event.pos):
							popup_visible = False
					else:
						for part in parts:
							part_rect = part["image"].get_rect(topleft=(left_margin, parts.index(part) * (part["image"].get_height() + gap) + top_margin))
							if part_rect.collidepoint(event.pos):
								if player_money >= part["cost"]:
									player_money -= part["cost"]
									print(f"Bought {part['name']} for ${part['cost']}")
								else:
									popup_message = "Not enough money to buy this, driver!"
									popup_visible = True
						if is_hovered(continue_arrow_rect):
							pass


		# ─── ▼ Display all necessary images and text ▼ ───────────────────────────── #
		screen.fill((0, 0, 0))


		# Display parts and costs
		font = pygame.font.SysFont('Arial', 24)
		y_offset = top_margin
		for part in parts:

			# Display part image
			part_rect = part["image"].get_rect(topleft=(left_margin, y_offset))
			screen.blit(part["image"], part_rect.topleft)

			# Display part name and cost
			text_surface = font.render(f"{part['name']} - ${part['cost']}", True, (255, 255, 255))
			text_rect = text_surface.get_rect(topleft=(left_margin + part_rect.width + 10, y_offset + part_rect.height // 4))
			screen.blit(text_surface, text_rect)

			y_offset += part_rect.height + gap
		
		# Display player's money on the screen
		money_surface = font.render(f"Player's money: ${player_money}", True, (255, 255, 255))
		money_rect = money_surface.get_rect(topright=(screen.get_width() - left_margin, top_margin))
		screen.blit(money_surface, money_rect)

		# Display pop-up if needed
		if popup_visible:
			button_rect = draw_popup(screen, popup_message)


		# ─── ▲ Display all necessary images and text ▲ ───────────────────────────── #



		# ─── ▼ 'Continue' arrow shimmer effect ▼ ─────────────────────────────────── #
		screen.blit(continue_arrow, continue_arrow_rect.topleft)
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

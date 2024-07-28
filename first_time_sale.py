from sys import exit
import pygame

from game_functions import *
from parameters import *
from player_data import player_instance



# Define cursors
arrow_cursor = pygame.SYSTEM_CURSOR_ARROW
hand_cursor = pygame.SYSTEM_CURSOR_HAND



# Define parts data
parts = [
	{"name": "Brakes", "cost": 200, "image": pygame.image.load("assets/brakes.png"), "hp_increase": 0, "torque_increase": 0},
	{"name": "Engine", "cost": 1000, "image": pygame.image.load("assets/engine.png"), "hp_increase": 60, "torque_increase": 56},
	{"name": "Exhaust", "cost": 500, "image": pygame.image.load("assets/muffler.png"), "hp_increase": 10, "torque_increase": 10},
	{"name": "Tires", "cost": 450, "image": pygame.image.load("assets/wheels.png"), "hp_increase": 0, "torque_increase": 0},
]



# ═══════════════════════════════════════════════════════════════════════════ #
# ═══ LEVEL IMAGES, DIALOGUE TEXT, AND GAME LOOP ════════════════════════════ #
def parts_sale(screen):

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
								if player_instance.subtract_money(part["cost"]):
									player_instance.update_car_performance(part["hp_increase"], part["torque_increase"])
									print(f"Bought {part["name"]} for ${part["cost"]}")
									print(f"New HP: {player_instance.car_hp}, New Torque: {player_instance.car_torque}")

								else:
									popup_message = "Not enough money, driver!"
									popup_visible = True

						if is_hovered(continue_arrow_rect):
							pass


		# ┌─── ▼ Display all necessary images and text ▼ ─────────────────────────────────────────────────────────────────────────────────────────┐
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


		# ┌─── Player's money and car values ─────────────────────────────────────────────────────────────────────────────────┐
		label_color = (255, 165, 0)		# Orange
		value_color = (255, 255, 255)	# White

		money_label_surface = font.render("Wallet:", True, label_color)
		money_label_rect = money_label_surface.get_rect(topright=(screen.get_width() - left_margin - 100, top_margin))
		money_value_surface = font.render(f"${player_instance.money}", True, value_color)
		money_value_rect = money_value_surface.get_rect(topleft=(money_label_rect.topright[0] + 5, top_margin))
		screen.blit(money_label_surface, money_label_rect)
		screen.blit(money_value_surface, money_value_rect)

		hp_label_surface = font.render("HP:", True, label_color)
		hp_value_surface = font.render(f"{player_instance.car_hp}", True, value_color)
		hp_label_rect = hp_label_surface.get_rect(topright=(screen.get_width() - left_margin - 100, top_margin + 30))
		hp_value_rect = hp_value_surface.get_rect(topleft=(hp_label_rect.topright[0] + 5, top_margin + 30))
		screen.blit(hp_label_surface, hp_label_rect)
		screen.blit(hp_value_surface, hp_value_rect)

		torque_label_surface = font.render("Torque:", True, label_color)
		torque_value_surface = font.render(f"{player_instance.car_torque}", True, value_color)
		torque_label_rect = torque_label_surface.get_rect(topright=(screen.get_width() - left_margin - 100, top_margin + 60))
		torque_value_rect = torque_value_surface.get_rect(topleft=(torque_label_rect.topright[0] + 5, top_margin + 60))
		screen.blit(torque_label_surface, torque_label_rect)
		screen.blit(torque_value_surface, torque_value_rect)
		# └─── Player's money and car values ─────────────────────────────────────────────────────────────────────────────────┘


		# Display pop-up if needed
		if popup_visible:
			button_rect = draw_popup(screen, popup_message)
		# └─── ▲ Display all necessary images and text ▲ ─────────────────────────────────────────────────────────────────────────────────────────┘



		# ┌─── ▼ 'Continue' arrow shimmer effect ▼ ───────────────────────────────────┐
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
		# └─── ▲ 'Continue' arrow shimmer effect ▲ ───────────────────────────────────┘


		pygame.display.flip()

	pygame.quit()

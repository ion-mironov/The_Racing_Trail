from sys import exit
import pygame

from ui_elements import *
from parameters import *
from player_data import player_instance
import first_engine_sale
import first_exhaust_sale



# Define cursors
arrow_cursor = pygame.SYSTEM_CURSOR_ARROW
hand_cursor = pygame.SYSTEM_CURSOR_HAND



# Dictionary defining part data with relevant player_data.py values
parts = [
	{"name": "Engine Tune 1", "cost": 1000, "image": pygame.image.load("assets/engine.png"), "hp_increase": 40, "torque_increase": 36, "next_level": first_engine_sale},
	{"name": "Sport Exhaust", "cost": 500, "image": pygame.image.load("assets/muffler.png"), "hp_increase": 12, "torque_increase": 10, "next_level": first_exhaust_sale}
]



# ═══════════════════════════════════════════════════════════════════════════ #
# ═══ LEVEL IMAGES, DIALOGUE TEXT, AND GAME LOOP ════════════════════════════ #
def parts_sale(screen):

	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ DIALOGUE TEXT ═════════════════════════════════════════════════════════════════════════════════════════════════ #
	font = pygame.font.Font("assets/arial.ttf", 20)
	first_sale_dialogue_1 = "You decide that the only parts you want to focus on are anything that can improve your engine's performance. With that in mind, you have your eyes set on an engine tune or sport exhaust system, but you only have enough cash to purchase one. Which will it be?"

	first_sale_dialogue_2 = "The engine tune will bump your HP to 206 and your torque to 195 lb-ft, but will leave you penniless. The exhaust system will increase your HP to 178 and your torque to 169 lb-ft, but you'll have money left over. Choose wisely, because you cannot go back once you make your selection!"


	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ IMAGES ════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	top_margin = 300			# Set gap from the top to first image
	left_margin = 50			# Set gap from left side of images
	gap = 20					# Set gap for in-between images

	popup_visible = False
	popup_message = ""
	button_rect = None
	next_level = None 			# Variable to store the next level


	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ GAME LOOP ═════════════════════════════════════════════════════════════════════════════════════════════════════ #
	running = True
	while running:
		cursor_changed = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					if popup_visible:
						if button_rect and button_rect.collidepoint(event.pos):
							popup_visible = False
							next_level.start_tuning(screen)

					else:
						for part in parts[:]:
							part_rect = part["image"].get_rect(topleft=(left_margin, parts.index(part) * (part["image"].get_height() + gap) + top_margin))
							if part_rect.collidepoint(event.pos):
								pygame.mouse.set_cursor(hand_cursor)
								if player_instance.subtract_money(part["cost"]):
									player_instance.update_car_performance(part["hp_increase"], part["torque_increase"])
									popup_message = "Heh heh heh, thank you!"
									popup_visible = True
									next_level = part["next_level"]		# Store the next level
									parts.remove(part)					# Remove part from list once bought
									break



	# ┌─── ▼ Display all necessary images and text ▼ ──────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
		screen.fill((0, 0, 0))

		text_wrap(screen, first_sale_dialogue_1, (screen.get_width() // 10, screen.get_height() // 15), font, WHITE, screen.get_width() - screen.get_width() // 5)
		text_wrap(screen, first_sale_dialogue_2, (screen.get_width() // 10, screen.get_height() // 4), font, WHITE, screen.get_width() - screen.get_width() // 5)


		# Display parts and costs
		font = pygame.font.Font("assets/arial.ttf", 20)
		y_offset = top_margin
		for part in parts:

			# Display part image
			part_rect = part["image"].get_rect(topleft=(left_margin, y_offset))
			screen.blit(part["image"], part_rect.topleft)

			# Display part name and cost
			text_surface = font.render(f"{part['name']} - ${part['cost']}", True, (255, 255, 255))
			text_rect = text_surface.get_rect(topleft=(left_margin + part_rect.width + 10, y_offset + part_rect.height // 4))
			screen.blit(text_surface, text_rect)

			# Check if mouse is hovering over the part
			if part_rect.collidepoint(pygame.mouse.get_pos()):
				pygame.mouse.set_cursor(hand_cursor)
				cursor_changed = True

			y_offset += part_rect.height + gap


	# ┌─── Player's money and car values ─────────────────────────────────────────────────────────────────────────────────────┐
		label_color = (255, 165, 0)		# Orange
		value_color = (255, 255, 255)	# White

		""" Money value """
		money_label_surface = font.render("Wallet:", True, label_color)
		money_label_rect = money_label_surface.get_rect(topright=(screen.get_width() - left_margin - 100, top_margin))
		money_value_surface = font.render(f"${player_instance.money}", True, value_color)
		money_value_rect = money_value_surface.get_rect(topleft=(money_label_rect.topright[0] + 5, top_margin))
		screen.blit(money_label_surface, money_label_rect)
		screen.blit(money_value_surface, money_value_rect)

		""" HP value """
		hp_label_surface = font.render("HP:", True, label_color)
		hp_value_surface = font.render(f"{player_instance.car_hp}", True, value_color)
		hp_label_rect = hp_label_surface.get_rect(topright=(screen.get_width() - left_margin - 100, top_margin + 30))
		hp_value_rect = hp_value_surface.get_rect(topleft=(hp_label_rect.topright[0] + 5, top_margin + 30))
		screen.blit(hp_label_surface, hp_label_rect)
		screen.blit(hp_value_surface, hp_value_rect)

		""" Torque value """
		torque_label_surface = font.render("Torque:", True, label_color)
		torque_value_surface = font.render(f"{player_instance.car_torque}", True, value_color)
		torque_label_rect = torque_label_surface.get_rect(topright=(screen.get_width() - left_margin - 100, top_margin + 60))
		torque_value_rect = torque_value_surface.get_rect(topleft=(torque_label_rect.topright[0] + 5, top_margin + 60))
		screen.blit(torque_label_surface, torque_label_rect)
		screen.blit(torque_value_surface, torque_value_rect)
	# └─── Player's money and car values ─────────────────────────────────────────────────────────────────────────────────────┘


		# Display pop-up if needed
		if popup_visible:
			button_rect = draw_popup(screen, popup_message)
		
		# Reset cursor if it hasn't been changed
		if not cursor_changed:
			pygame.mouse.set_cursor(arrow_cursor)
	# └─── ▲ Display all necessary images and text ▲ ──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘


		pygame.display.flip()

	pygame.quit()

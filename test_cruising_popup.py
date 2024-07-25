import os
import random
from sys import exit
import pygame

from game_functions import *
from parameters import *
import current_progress



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
def test_cruising(screen):

	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ ANIMATION ═════════════════════════════════════════════════════════════════════════════════════════════════════ #
	""" Define image frames for animation """
	frames = load_frames("assets/blue_civic_cruising/", "night_")
	frame_count = len(frames)
	current_frame = 0

	""" Timing for frame updates """
	frame_delay = 100							# milliseconds before displaying next frame in sequence
	last_update = pygame.time.get_ticks()

	""" Get rect from first image frame to position animation """
	civic_cruising_rect = frames[0].get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.5))



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ SHIMMER FUNCTION ══════════════════════════════════════════════════════════════════════════════════════════════ #
	shimmer_progress_continue = 0
	hovered_continue = False



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ POP-UP WINDOW ═════════════════════════════════════════════════════════════════════════════════════════════════ #
	popup_visible = False											# Pop-up window's default state.

	# Define random event interval
	event_probability = 0.5											# 50% chance of event being `True`
	last_event_check = pygame.time.get_ticks()

	# Create pop-up window and define its position on screen
	button_rect = pygame.Rect(screen.get_width() // 2 - 50, screen.get_height() // 2 + 20, 100, 30)

	# Define pop-up window border properties
	border_color = (255, 255, 255)									# White border
	border_thickness = 5

	# Display image within pop-up
	popup_image = pygame.image.load("assets/merchant_bust.png")		# Define image
	popup_image_rect = popup_image.get_rect(center=(150, 75))		# Center it within the pop-up window



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ 'CONTINUE' ARROW ══════════════════════════════════════════════════════════════════════════════════════════════ #
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
						pass

					if popup_visible and button_rect.collidepoint(event.pos):	# If pop-up is visible and button is clicked on
						popup_visible = False									# Close the pop-up
						last_event_check = pygame.time.get_ticks()				# Reset the event check timer


		# ─── ▼ Display all necessary images and text ▼ ───────────────────────────── #
		screen.fill((0, 0, 0))

		now = pygame.time.get_ticks()
		if not popup_visible and now - last_update > frame_delay:
			current_frame = (current_frame + 1) % frame_count
			last_update = now

		screen.blit(frames[current_frame], civic_cruising_rect.topleft)
		screen.blit(continue_arrow, continue_arrow_rect.topleft)
		# ─── ▲ Display all necessary images and text ▲ ───────────────────────────── #


		# ─── ▼ Pop-up window and its parameters ▼ ────────────────────────────────── #
		# Randomly show the pop-up
		if not popup_visible and now - last_event_check > 2000:			# Checks if 5 seconds have passed since the last event check and if no pop-up is currently visible
			last_event_check = now										# Updates to current time; resets timer for checking the next event from this point
			if random.random() < event_probability:						# Random float value between 0 and 1, compares to 0.5 defined earlier
				popup_visible = True									# Display a pop-up window if above condition is met

		# Display pop-up window
		if popup_visible:
			popup_text = "What're ya buyin'?"
			popup_width, popup_height = 300, 150
			popup_surface = pygame.Surface((popup_width, popup_height))
			popup_surface.fill((13, 17, 23))
			popup_surface.blit(popup_image, popup_image_rect)			# Display image onto the pop-up surface
			popup_rect = popup_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

			# Create border and display it behind pop-up window
			border_rect = pygame.Rect(
				popup_rect.left - border_thickness,
				popup_rect.top - border_thickness,
				popup_width + 2 * border_thickness,
				popup_height + 2 * border_thickness
			)
			pygame.draw.rect(screen, border_color, border_rect)

			screen.blit(popup_surface, popup_rect)

			font = pygame.font.Font("assets/arial.ttf", 24)
			text_surface = font.render(popup_text, True, WHITE)
			text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 20))
			screen.blit(text_surface, text_rect)

			# Create button and then display it
			pygame.draw.rect(screen, WHITE, button_rect)
			button_text = font.render("Close", True, BLACK)
			button_text_rect = button_text.get_rect(center=button_rect.center)
			screen.blit(button_text, button_text_rect)
		# ─── ▲ Pop-up window and its parameters ▲ ────────────────────────────────── #



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

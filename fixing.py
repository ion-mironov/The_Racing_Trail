import os
import pygame

from game_functions import *
from parameters import *
import cruising


# GIF animation function ============================================= #
def load_frames(folder, prefix):
	frames = []
	for filename in sorted(os.listdir(folder)):
		if filename.startswith(prefix):
			img = pygame.image.load(os.path.join(folder, filename))
			frames.append(img)
	return frames


#  Fixing Level animation, text, and game loop ======================= #
def start_fixing(screen):

	# Define image frames for animation
	frames = load_frames("assets/civic_fix/", "frame_")			# Load all frames for the animation from specified folder; filenames start with 'frame_'
	frame_count = len(frames)									# Calculate number of frames in list; returns length of list and stored into 'frame_count'
	current_frame = 0											# Start animation with the very first frame

	# Timing for frame updates
	frame_delay = 100   # milliseconds
	last_update = pygame.time.get_ticks()

	# Get rect from first GIF frame to position animation
	civic_fix_rect = frames[0].get_rect(center=(screen.get_width() // 2, screen.get_height() // 5))


	# Dialogue text settings
	font = pygame.font.SysFont('Arial', 24)
	you_tried_text_surface = font.render("Well, at least you tried...", True, WHITE)
	you_tried_text_rect = you_tried_text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2.7))

	you_fixed_it_text_surface = font.render("But, after a few hours of swearing and spending what little money you had, you finally got your car to your liking.", True, WHITE)
	you_fixed_it_text_rect = you_fixed_it_text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2.1))


	# Continue arrow settings
	continue_arrow = pygame.image.load("assets/continue_arrow.png")
	continue_arrow_rect = continue_arrow.get_rect(bottomright=(screen.get_width() // 1.005, screen.get_height() // 1.01))


	# Animation states
	animation_completed = False
	you_tried_displayed = False
	text_displayed_time = 0

	# Time Delays
	animation_end_time = 1000	# milliseconds
	second_text_delay = 1500	# milliseconds



	""" Main loop """
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			
			# Continue arrow button
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					if is_hovered(continue_arrow_rect):
						# cruising.cruising_animation(screen)
						pass


		# Update the frame animation index and stop once the final frame is displayed
		now = pygame.time.get_ticks()
		if now - last_update > frame_delay and not animation_completed:
			current_frame += 1
			last_update = now
		
			# Check if the animation has completed one cycle
			if current_frame == frame_count - 1:
				animation_completed = True
				text_displayed_time = pygame.time.get_ticks()  # Record the time when the animation completes


		screen.fill((0, 0, 0))


		# Display animation
		if current_frame < frame_count:
			screen.blit(frames[current_frame], civic_fix_rect.topleft)

		# Display dialogue text once the animation's final frame has displayed and first time-delay has passed
		if animation_completed:
			if now - text_displayed_time > animation_end_time:
				screen.blit(you_tried_text_surface, you_tried_text_rect)
				you_tried_displayed = True
		
		# Display the second dialogue text after the first has displayed and second time-delay has passed
		if you_tried_displayed and now - text_displayed_time > animation_end_time + second_text_delay:
			screen.blit(you_fixed_it_text_surface, you_fixed_it_text_rect)
			screen.blit(continue_arrow,continue_arrow_rect.topleft)

			""" Continue arrow shimmer effect """
			if is_hovered(continue_arrow_rect):
				if not hovered_new:
					shimmer_progress_new = 0
					hovered_new = True
				if shimmer_progress_new < 1:
					shimmer_progress_new += 0.006
					draw_shimmer(screen, continue_arrow_rect, shimmer_progress_new)
			else:
				hovered_new = False


		pygame.display.flip()

	pygame.quit()

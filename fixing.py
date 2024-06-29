import os
import pygame

from game_functions import *
from parameters import *



def load_frames(folder, prefix):
	frames = []
	for filename in sorted(os.listdir(folder)):
		if filename.startswith(prefix):
			img = pygame.image.load(os.path.join(folder, filename))
			frames.append(img)
	return frames



def start_fixing(screen):

	# Define image frames for animation
	frames = load_frames("assets/civic_fix/", "frame_")			# Load all frames for the animation from specified folder; filenames start with 'frame_'
	frame_count = len(frames)									# Calculate number of frames in list; returns length of list and stored into 'frame_count'
	current_frame = 0											# Start animation with the very first frame

	# Timing for frame updates
	frame_delay = 100	# milliseconds
	last_update = pygame.time.get_ticks()

	# Get rect from first GIF frame to position the animation
	civic_fix_rect = frames[0].get_rect(center=(screen.get_width() // 2, screen.get_height() // 5))

	# Font settings for text
	font = pygame.font.SysFont('Arial', 24)
	you_tried_text_surface = font.render("Well, at least you tried...", True, WHITE)
	you_tried_text_rect = you_tried_text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2.7))

	# Animation state
	animation_completed = False



	""" Game loop """
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()


		# Update the frame index in a continuous loop
		# now = pygame.time.get_ticks()
		# if now - last_update > frame_delay:
		# 	current_frame = (current_frame + 1) % frame_count
		# 	last_update = now

		# Update the frame index and stop once the final frame is displayed
		now = pygame.time.get_ticks()
		if now - last_update > frame_delay and not animation_completed:
			current_frame += 1
			last_update = now
		
			# Check if the animation has completed one cycle
			if current_frame == frame_count - 1:
				animation_completed = True


		screen.fill((0, 0, 0))


		if current_frame < frame_count:
			screen.blit(frames[current_frame], civic_fix_rect.topleft)

		if animation_completed:
			screen.blit(you_tried_text_surface, you_tried_text_rect)


		pygame.display.flip()

	pygame.quit()

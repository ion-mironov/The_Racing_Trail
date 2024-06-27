import os
import pygame

from parameters import *
from game_functions import *


def load_frames(folder, prefix):
	frames = []
	for filename in sorted(os.listdir(folder)):
		if filename.startswith(prefix):
			img = pygame.image.load(os.path.join(folder, filename))
			frames.append(img)
	return frames

def start_fixing(screen):

	frames = load_frames("assets/civic_fix/", "frame_")
	frame_count = len(frames)
	current_frame = 0

	# Timing for frame updates
	frame_delay = 100  # milliseconds
	last_update = pygame.time.get_ticks()

	# Get the rect from the first frame to position the animation
	civic_fix_rect = frames[0].get_rect(center=(screen.get_width() // 2, screen.get_height() // 5))


	""" Fixing game loop """
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		# Update the frame index
		now = pygame.time.get_ticks()
		if now - last_update > frame_delay:
			current_frame = (current_frame + 1) % frame_count
			last_update = now

		screen.fill((0, 0, 0))

		screen.blit(frames[current_frame], civic_fix_rect.topleft)

		pygame.display.flip()

	pygame.quit()

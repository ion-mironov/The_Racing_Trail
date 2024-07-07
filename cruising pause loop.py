import os
import pygame

from game_functions import *
from parameters import *



# === GIF animation function ================================================ #
def load_frames(folder, prefix):
	frames = []
	for filename in sorted(os.listdir(folder)):
		if filename.startswith(prefix):
			img = pygame.image.load(os.path.join(folder, filename))
			frames.append(img)
	return frames


#  === 'Cruising' level animation and game loop ====================== #
def start_cruising(screen):

	# === ANIMATION ================================================================================================================= #
	""" Define image frames for animation """
	frames = load_frames("assets/blue_civic_cruising/", "frame_")
	frame_count = len(frames)
	current_frame = 0

	""" Timing for frame updates """
	frame_delay = 	 100	# milliseconds to next frame display
	run_duration = 	 2000	# milliseconds to run the animation before pausing
	pause_duration = 500	# milliseconds to pause the animation
	last_update = pygame.time.get_ticks()
	is_paused = False		# Track whether the animation is paused

	""" Get rect from first image frame to position animation """
	civic_cruising_rect = frames[0].get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.5))

	# Timing control (Track the start time of the animation)
	animation_start_time = pygame.time.get_ticks()


	# === 'CRUISING' GAME LOOP ====================================================================================================== #
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		screen.fill((0, 0, 0))

		pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


		# Display image frames with a start/stop effect
		now = pygame.time.get_ticks()
		
		if is_paused:
			if now - last_update > pause_duration:
				is_paused = False
				animation_start_time = pygame.time.get_ticks()  # Reset animation start time
				last_update = now

		else:
			if now - last_update > frame_delay:
				current_frame = (current_frame + 1) % frame_count
				last_update = now

				if now - animation_start_time > run_duration:  # Pause after the run duration
					is_paused = True

		screen.blit(frames[current_frame], civic_cruising_rect.topleft)

		pygame.display.flip()

	pygame.quit()

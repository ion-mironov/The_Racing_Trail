import os
import pygame

from game_functions import *
from parameters import *



# GIF animation function ============================================= #
def load_frames(folder, prefix):
	frames = []
	for filename in sorted(os.listdir(folder)):
		if filename.startswith(prefix):
			img = pygame.image.load(os.path.join(folder, filename))
			frames.append(img)
	return frames


#  'Cruising' level animation, text, and game loop ======================= #
def start_cruising(screen):

	""" Shimmer function """
	# Initialize shimmer progress
	shimmer_progress_continue = 0

	# Check if cursor is over 'continue' arrow (used to reset hover effect)
	hovered_continue = False


	# Dialogue text settings
	font = pygame.font.SysFont('Arial', 24)
	cruising_text_surface = font.render("After a splash of paint, lowered suspension, and some different wheels, you hit the open road and begin your journey.", True, WHITE)
	cruising_text_rect = cruising_text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 7))


	# Define image frames for animation
	frames = load_frames("assets/civic_cruising/", "frame_")	# Load all frames for the animation from specified folder; filenames start with 'frame_'
	frame_count = len(frames)									# Calculate number of frames in list; returns length of list and stored into 'frame_count'
	current_frame = 0											# Start animation with the very first frame

	# Timing for frame updates
	frame_delay = 100   # milliseconds
	last_update = pygame.time.get_ticks()

	# Get rect from first GIF frame to position animation
	civic_cruising_rect = frames[0].get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))



	# 'Continue' arrow settings
	# continue_arrow = pygame.image.load("assets/continue_arrow.png")
	# continue_arrow_rect = continue_arrow.get_rect(bottomright=(screen.get_width() // 1.005, screen.get_height() // 1.01))


	""" Main loop """
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			
			# Continue arrow button
			# elif event.type == pygame.MOUSEBUTTONUP:
			# 	if event.button == 1:
			# 		if is_hovered(continue_arrow_rect):
			# 			pass

		screen.fill((0, 0, 0))


		# Update the frame animation index and stop once the final frame is displayed
		now = pygame.time.get_ticks()
		if now - last_update > frame_delay:
			current_frame = (current_frame + 1) % frame_count
			last_update = now

		# Display animation and dialogue text
		screen.blit(frames[current_frame], civic_cruising_rect.topleft)
		screen.blit(cruising_text_surface, cruising_text_rect)
		
		""" 'Continue' arrow shimmer effect """
		# if is_hovered(continue_arrow_rect):
		# 	if not hovered_continue:
		# 		shimmer_progress_continue = 0
		# 		hovered_continue = True
		# 	if shimmer_progress_continue < 1:
		# 		shimmer_progress_continue += 0.005
		# 		draw_shimmer(screen, continue_arrow_rect, shimmer_progress_continue)
		# else:
		# 	hovered_continue = False

		pygame.display.flip()

	pygame.quit()

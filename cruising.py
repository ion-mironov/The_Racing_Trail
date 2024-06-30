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
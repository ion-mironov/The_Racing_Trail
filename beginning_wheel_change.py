import os
import pygame

from game_functions import *
from parameters import *
import beginning_fixed



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
def start_fixing(screen):

	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ SHIMMER FUNCTION ══════════════════════════════════════════════════════════════════════════════════════════════ #
	shimmer_progress_continue = 0		# Initialize shimmer progress
	hovered_continue = False			# Check if cursor is over 'continue' arrow (used to reset hover effect)



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ ANIMATION ═════════════════════════════════════════════════════════════════════════════════════════════════════ #
	""" Define image frames for animation """
	frames = load_frames("assets/civic_fix/", "frame_")			# Load all frames for the animation from specified folder; filenames start with 'frame_'
	frame_count = len(frames)									# Calculate number of frames in list; returns length of list and stored into 'frame_count'
	current_frame = 0											# Start animation with the very first frame

	""" Timing for frame updates """
	frame_delay = 100   # milliseconds
	last_update = pygame.time.get_ticks()

	""" Get rect from first GIF frame to position animation """
	civic_fix_rect = frames[0].get_rect(center=(screen.get_width() // 2, screen.get_height() // 5))



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ DIALOGUE TEXT ═════════════════════════════════════════════════════════════════════════════════════════════════ #
	font = pygame.font.SysFont('Arial', 24)
	you_tried_text = font.render("Well, at least you tried...", True, WHITE)
	you_tried_text_rect = you_tried_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2.7))

	you_fixed_it_text = font.render("But, after a few hours of swearing and spending what little money you had, you finally got the car to your liking.", True, WHITE)
	you_fixed_it_text_rect = you_fixed_it_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2.1))



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ 'CONTINUE' ARROW ══════════════════════════════════════════════════════════════════════════════════════════════ #
	continue_arrow = pygame.image.load("assets/continue_arrow.png")
	continue_arrow_rect = continue_arrow.get_rect(bottomright=(screen.get_width() // 1.005, screen.get_height() // 1.01))



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ ANIMATION STATES ══════════════════════════════════════════════════════════════════════════════════════════════ #
	animation_completed = False
	you_tried_displayed = False
	text_displayed_time = 0



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ TIME DELAYS  ══════════════════════════════════════════════════════════════════════════════════════════════════ #
	animation_end_time = 1000	# milliseconds
	second_text_delay =  1500	# milliseconds



	# ═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════ #
	# ═══ GAME LOOP ═════════════════════════════════════════════════════════════════════════════════════════════════════ #
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
						beginning_fixed.fixed_civic(screen)


		# ─── ▼ Display all necessary images and text ▼ ───────────────────────────── #
		screen.fill((0, 0, 0))


		# Update civic_fix frame animation index and stop once the last frame is displayed
		now = pygame.time.get_ticks()
		if now - last_update > frame_delay and not animation_completed:
			current_frame += 1
			last_update = now
		
			# Check if the animation has completed one cycle
			if current_frame == frame_count - 1:
				animation_completed = True
				text_displayed_time = pygame.time.get_ticks()  # Record the time when the animation completes


		# Display animation
		if current_frame < frame_count:
			screen.blit(frames[current_frame], civic_fix_rect.topleft)


		# Display dialogue text once the animation's last frame has displayed AND first time-delay has passed
		if animation_completed:
			if now - text_displayed_time > animation_end_time:
				screen.blit(you_tried_text, you_tried_text_rect)
				you_tried_displayed = True


		# Display 'Continue' arrow AND the second dialogue text AFTER the first dialogue has displayed AND second time-delay has passed
		if you_tried_displayed and now - text_displayed_time > animation_end_time + second_text_delay:
			screen.blit(you_fixed_it_text, you_fixed_it_text_rect)
			screen.blit(continue_arrow, continue_arrow_rect.topleft)
		# ─── ▲ Display all necessary images and text ▲ ───────────────────────────── #


			# ─── ▼ 'Continue' arrow shimmer effect ▼ ─────────────────────────────────── #
			cursor_changed = False

			if is_hovered(continue_arrow_rect):
				if not hovered_continue:
					shimmer_progress_continue = 0
					hovered_continue = True

				if shimmer_progress_continue < 1:
					shimmer_progress_continue += 0.003
					draw_shimmer(screen, continue_arrow_rect, shimmer_progress_continue)

				pygame.mouse.set_cursor(hand_cursor)
				cursor_changed = True

			else:
				hovered_continue = False
			
			if not cursor_changed:
				pygame.mouse.set_cursor(arrow_cursor)
			# ─── ▲ 'Continue' arrow shimmer effect ▲ ─────────────────────────────────── #


		# ▼ This line is needed to ensure cursor is set to default system arrow ▼ #
		else:
			pygame.mouse.set_cursor(arrow_cursor)


		pygame.display.flip()

	pygame.quit()

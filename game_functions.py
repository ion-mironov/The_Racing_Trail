import pygame

""" Use this to allow the wrapping of text found in multiple dialogues """
def text_wrap(screen, text, position, font, color, max_width):
	words = text.split(" ")
	lines = []
	current_line = words[0]

	for word in words[1:]:
		if font.size(current_line + " " + word)[0] < max_width:
			current_line += " " + word
		else:
			lines.append(current_line)
			current_line = word

	lines.append(current_line)

	for i, line in enumerate(lines):
		text_surface = font.render(line, True, color)
		text_rect = text_surface.get_rect(topleft=(position[0], position[1] + i * font.get_linesize()))
		screen.blit(text_surface, text_rect)


# ========================================================================================================= #
# Check if mouse cursor hovers over image to initiate shimmer effect
def is_hovered(rect):
	mouse_pos = pygame.mouse.get_pos()
	return rect.collidepoint(mouse_pos)


""" Shimmer hover effect """
def draw_shimmer(surface, rect, progress):
	# Create a translucent white surface
	shimmer_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
	shimmer_surface.fill((255, 255, 255, 0))  # Fully transparent

	# Define shimmer width and calculate position
	shimmer_width = int(rect.width * 0.1)
	x_position = int(rect.width * progress) - shimmer_width

	# Draw the shimmer
	if x_position < rect.width:
		shimmer_rect = pygame.Rect(x_position, 0, shimmer_width, rect.height)
		shimmer_surface.fill((255, 255, 255, 128), shimmer_rect)

	# Draw the shimmer surface onto the main surface
	surface.blit(shimmer_surface, rect.topleft)

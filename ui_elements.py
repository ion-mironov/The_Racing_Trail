import pygame



# ═══════════════════════════════════════════════════════════════════════════ #
# ═════ TEXT WRAP FUNCTION  ═════════════════════════════════════════════════ #
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



# ═══════════════════════════════════════════════════════════════════════════ #
# ═══ POP-UP WINDOW ═════════════════════════════════════════════════════════ #
def draw_popup(screen, message):
	popup_width, popup_height = 300, 150
	popup_surface = pygame.Surface((popup_width, popup_height))
	popup_surface.fill((13, 17, 23))
	popup_rect = popup_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

	# Draw border
	border_thickness = 5
	border_color = (255, 255, 255)
	border_rect = pygame.Rect(
		popup_rect.left - border_thickness,
		popup_rect.top - border_thickness,
		popup_width + 2 * border_thickness,
		popup_height + 2 * border_thickness
	)
	pygame.draw.rect(screen, border_color, border_rect)
	screen.blit(popup_surface, popup_rect)

	# Draw message
	font = pygame.font.Font("assets/arial.ttf", 24)
	text_surface = font.render(message, True, (255, 255, 255))
	text_rect = text_surface.get_rect(center=(popup_rect.centerx, popup_rect.centery - 20))
	screen.blit(text_surface, text_rect)

	# Draw button
	button_rect = pygame.Rect(popup_rect.centerx - 50, popup_rect.centery + 20, 100, 40)
	pygame.draw.rect(screen, (255, 255, 255), button_rect)
	button_text = font.render("Continue", True, (0, 0, 0))
	button_text_rect = button_text.get_rect(center=button_rect.center)
	screen.blit(button_text, button_text_rect)

	return button_rect



# ═══════════════════════════════════════════════════════════════════════════ #
# ═══ SHIMMER & HOVER CHECK ═════════════════════════════════════════════════ #
""" Check if mouse cursor is hovering over image """
def is_hovered(rect):
	mouse_pos = pygame.mouse.get_pos()
	return rect.collidepoint(mouse_pos)


""" Shimmer effect """
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

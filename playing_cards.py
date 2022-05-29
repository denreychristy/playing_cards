# Playing Cards Libary

from os import mkdir
import pygame as pg

pg.init()

# ==================================================================================================== #

# Create images folder if necessary
try:
	mkdir("images")
except:
	pass

black = [0, 0, 0]
white = [255, 255, 255]
red = [127, 0, 0]
blue = [0, 0, 127]
green = [0, 127, 0]

font_path = "font.otf"
font = pg.font.Font(font_path, 70)

# ==================================================================================================== #

card_width = 250
card_height = round((350 / 250) * card_width)

for card_value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
	for suit in ["clubs", "spades", "hearts", "diamonds"]:
		card_rect = pg.Rect(0, 0, card_width, card_height)
		card_surface = pg.Surface(card_rect.size)
		card_surface.fill(white)

		if suit == "clubs":
			suit_color = black
		elif suit == "spades":
			suit_color = green
		elif suit == "hearts":
			suit_color = red
		elif suit == "diamonds":
			suit_color = blue

		# Card Value Small Text
		card_value_image = font.render(card_value, True, suit_color)
		card_value_rect = card_value_image.get_rect()

		card_surface.blit(card_value_image, [5, -5])
		card_value_rect.bottomright = [card_width - 5, card_height - 5]
		card_surface.blit(pg.transform.rotozoom(card_value_image, 180, 1), card_value_rect)

		# Card Value Large Text
		card_value_image = pg.font.Font(font_path, 150).render(card_value, True, suit_color)
		card_value_rect = card_value_image.get_rect(center = card_rect.center)
		card_surface.blit(card_value_image, card_value_rect)

		# Suit Symbol
		suit_image = pg.font.Font(font_path, 40).render(suit, True, suit_color)
		
		left_side = pg.transform.rotozoom(suit_image, 90, 1)
		left_rect = left_side.get_rect(bottomleft = [0, card_rect.h - 5])
		card_surface.blit(left_side, left_rect)

		right_side = pg.transform.rotozoom(suit_image, -90, 1)
		right_rect = right_side.get_rect(topright = [card_rect.w, 5])
		card_surface.blit(right_side, right_rect)

		card_surface.blit(left_side, left_rect)

		# Save card image to file
		pg.image.save(card_surface, f"images/{card_value}_of_{suit}.png")

# Joker
card_value = "Joker"

card_rect = pg.Rect(0, 0, card_width, card_height)
card_surface = pg.Surface(card_rect.size)
card_surface.fill(white)

suit_color = blue

card_value_image = font.render(card_value, True, suit_color)
card_value_rect = card_value_image.get_rect()

card_surface.blit(card_value_image, [5, 5])
card_value_rect.bottomright = [250 - 5, 350 - 5]
card_surface.blit(pg.transform.rotozoom(card_value_image, 180, 1), card_value_rect)

pg.image.save(card_surface, f"images/{card_value}.png")
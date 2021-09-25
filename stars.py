import pygame
from pygame.sprite import Sprite
from random import randint

class Stars(Sprite):
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.star_color
		#Creates a star
		self.rect = pygame.Rect(randint(1, 1200), randint(1,600),self.settings.star_width, self.settings.star_height)
		self.y = float(self.rect.y)

		

	def draw_star(self):
		pygame.draw.rect(self.screen, self.color, self.rect)	
		
	def update(self):
		self.y += 0.5

		self.rect.y = self.y	

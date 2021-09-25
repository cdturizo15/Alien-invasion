import pygame
from pygame.sprite import Sprite

class Lifes(Sprite):

	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()				
		#Lifes stuff
		self.image_life = pygame.image.load('data/images/life.bmp')
		self.rect_life = self.image_life.get_rect()
		self.rect_life.topleft = self.screen_rect.topleft
		


	def create_life(self, no_life):
		alien_width = self.rect_life.width
		self.rect_life.left = self.screen_rect.left + alien_width * no_life + 5

		#life.x = life_width  * (life_no * life_width) 
		#life.rect_life.x = life.x
		self.blit_lifes()
			

	def blit_lifes (self):
			self.screen.blit(self.image_life, self.rect_life)

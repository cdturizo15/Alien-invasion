from random import randint
import pygame
from pygame.sprite import Sprite

class Settings:
	"""THIS CLASS IS FOR SETTINGS OF THE SCREEN"""
	def __init__(self):
		#BACKGROUND SETTINGS
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (0, 0, 0)	
		"""STARS SETTINGS"""
		self.star_width =  1
		self.star_height = 1
		self.star_color = (255, 255 , 255)
		self.stars_number = 300
		#SHIP SETTINGS
		self.ship_speed = 1
		self.ship_lifes = 3
		#BULLETS SETTINGS
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255, 0, 0)
		self.bullet_speed = 1.0
		self.bullet_limit = 5
		#ALIEN SPEED
		self.alien_speed = 0.5
		self.change_direction = -1
		self.alien_direction = 1
		self.drop_speed = 10
		self.alien_score = 50
		


		
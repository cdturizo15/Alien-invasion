import pygame

class Ship:

	def __init__(self, ai_game):
		"""INITIALIZE THE SHIP AND POSITION"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get is rect
		self.image = pygame.image.load('data/images/ship.bmp')
		self.rect = self.image.get_rect()

		#Start the ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		#Store a decimal value of the ship
		self.x = float(self.rect.x)

		#MOVEMENT OF THE SHIP
		self.move_right = False
		self.move_left = False

	def update(self):
		#Update the ship movement
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.move_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed	

		self.rect.x = self.x	

	def center_ship(self):
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)


	def blitme(self):
		"""Draw the ship at his location"""
		self.screen.blit(self.image, self.rect)	
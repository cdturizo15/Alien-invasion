import pygame


class Game_stats:
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.settings = ai_game.settings		
		self.game_active = False
		self.play = False
		self.score = 0
		self.high_score = 0
		self.reset_stats()
		#Game over stuff
		self.screen_rect = ai_game.screen.get_rect()
		self.image = pygame.image.load('data/images/game_over.bmp')
		self.rect = self.image.get_rect()
		self.rect.center = self.screen_rect.center
		
		#Menu stuff
		self.image_menu = pygame.image.load('data/images/menu.bmp')
		self.rect_menu = self.image_menu.get_rect()
		self.rect_menu.center = self.screen_rect.center

	def reset_stats(self):
		self.ships_left = self.settings.ship_lifes	

	def show_game_over(self):
		self.screen.blit(self.image, self.rect)

	def show_menu(self):
		self.screen.blit(self.image_menu,self.rect_menu)


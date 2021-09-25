import pygame.font

class Scoreboard:
	"""docstring for Scoreboard"""
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.stats = ai_game.stats	
		self.screen_rect = ai_game.screen.get_rect()				
		#Scoreboard stuff
		self.text_score_color = (255, 255, 255)
		self.font_score = pygame.font.SysFont(None, 48)
		self.prep_score()
		self.prep_high_score()

	
	def prep_high_score(self):
		score_str = str(self.stats.high_score)
		self.high_score_image = self.font_score.render(score_str,
			True,self.text_score_color,self.settings.bg_color)

		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx 
		self.high_score_rect.top = self.score_rect.top	

	def check_high_score(self):
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()		


	def prep_score(self):
		score_str = str(self.stats.score)
		self.score_image = self.font_score.render(score_str,
			True,self.text_score_color,self.settings.bg_color)

		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		self.screen.blit(self.score_image,self.score_rect)	
		self.screen.blit(self.high_score_image,self.high_score_rect)		
import sys
import pygame

from time import sleep
from game_stats import Game_stats
from settings import Settings
from ship import Ship
from stars import Stars
from bullet import Bullets
from alien import Alien
from button import Button
from scoreboard import Scoreboard
from lifes import Lifes

class AlienInvasion:
	
 	
	def __init__(self):
		"""INITIALIZE THE GAME AND SOURCES"""
		pygame.init()
		self.settings = Settings()
		
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption('Alien Invasion')

		self.stats = Game_stats(self)
		self.ship = Ship(self)
		self.stars = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.lifes = Lifes(self)	
		self.play_button = Button(self, 'Play')
		self.play_again_button = Button(self,'Play again')
		self.score = Scoreboard(self)
		self._stars_background()
		self._create_fleet()



	def ship_hit(self):
		if self.stats.ships_left > 1:
			self.stats.ships_left -= 1

			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			self.ship.center_ship()

			sleep(0.5)
		else:
			self.stats.game_active = False	
			self.stats.play = True

	def check_play(self, mouse_pos):
		if self.play_button.rect.collidepoint(mouse_pos):
			self.stats.game_active = True

	def check_events(self):
		"""CHECKS KEYPRESSES AND OTHER EVENTS"""	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()		
			elif event.type == pygame.KEYDOWN:
				self.keydown_events(event)
			elif event.type == pygame.KEYUP:
				self.keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self.check_play(mouse_pos)		
				
	def _stars_background(self):
		for star in range(self.settings.stars_number):
			star = Stars(self)
			self.stars.add(star)
	
	def _create_fleet(self):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		ship_height = self.ship.rect.height
		free_space_x = self.settings.screen_width - (2 * alien_width)
		free_space_y = (self.settings.screen_height) - (3 * alien_height) - ship_height
		rows = free_space_y // (2 * alien_height)
		aliens_number_x = free_space_x // (2 * alien_width)			
		for row in range(rows):		
			for alien_no in range(aliens_number_x+1):
				self._create_alien(alien_no, row)
		
	def _create_alien(self, alien_no, row):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_no * alien_width
		alien.rect.y = alien.rect.height +  1.2 * alien.rect.height * row
		alien.rect.x = alien.x
		self.aliens.add(alien)		

	
	def _fire_bullet(self):
		#CREATES A BULLET
			if len(self.bullets) < self.settings.bullet_limit:
				new_bullet = Bullets(self)
				self.bullets.add(new_bullet)	


	def _fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien._check_edges():
				self.change_direction()
				break

	def change_direction(self):
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.drop_speed
		self.settings.alien_direction *= self.settings.change_direction 


	def check_alien_bottom(self):
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom <= screen_rect.bottom:
				self.ship_hit()
				break 

	def update_aliens(self):
		self._fleet_edges()
		self.aliens.update()
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self.ship_hit()

	def remove_objects(self):
		screen_rect = self.screen.get_rect()
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)	


		self._check_collisions()			
	

	def _check_collisions(self):
		collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
		if collisions:
			self.stats.score += self.settings.alien_score
			self.score.prep_score()
			self.score.check_high_score() 
			self.lifes.blit_lifes()
		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()
			self.settings.alien_speed *= 1.4		
	
	def keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			#MOVE THE SHIP TO THE RIGHT
			self.ship.move_right = True
		elif event.key == pygame.K_LEFT:
			#MOVE THE SHIP TO THE RIGHT
			self.ship.move_left = True	
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		 	


	def keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.move_right = False	
		elif event.key == pygame.K_LEFT:
			self.ship.move_left = False	


	def update_screen(self):
		#Redraw the screen during each pass
		self.screen.fill(self.settings.bg_color)
		if self.stats.game_active:
			self.ship.blitme()	
			self.score.show_score()
			for life in range(self.stats.ships_left):
				self.lifes.create_life(life)
		if not self.stats.game_active and not self.stats.play:
			self.stats.show_menu()
			self.play_button.draw_button()
				
		if not self.stats.game_active and self.stats.play:
			self.stats.show_game_over()
			self.stats.score = 0
			self.score.prep_score()			
			self.play_again_button.draw_button()
			self.settings.alien_speed = 0.5	

		#Create a background of stars
		for star in self.stars.sprites():
			star.draw_star()
		#Create the firing bullets	
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()	
		self.aliens.draw(self.screen)			
		#Make the most recently drawn screen visible	
		pygame.display.flip()
		
		
	def run_game(self):
		"""STARTS THE LOOP FOR THE GAME"""
		while True:
			self.check_events()
			#self.stars.update()
			if self.stats.game_active:
				self.ship.update()
				self.bullets.update()
				self.update_aliens()
				self.remove_objects()
			else:
				self.aliens.empty()
				self.bullets.empty()
				self.stars.update()
				for star in self.stars.copy():
					if (star.rect.bottom >= 600):
						self.stars.remove(star)	
						star = Stars(self)
						self.stars.add(star)				
		
			self.update_screen()
				

if __name__ ==	'__main__':
	ai = AlienInvasion()
	ai.run_game()	
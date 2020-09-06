class Settings():
	""" Class to save settings for alien invasion """
	def __init__(self):
		""" Initialise the game settings """
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_colour = (230,230,230)

		# Ship Settings.
		self.ship_speed_factor = 1.5
		self.ship_limit = 3

		# Bullet settings.
		self.bullet_speed_factor = 3
		self.bullet_width = 1
		self.bullet_height = 15
		self.bullet_colour = 60, 60, 60
		self.bullets_allowed = 3

		# Alient settings.
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 20

		# How quickly the game speeds up.
		self.speedup_scale = 1.1

		# How quickly the alien point values increase.
		self.score_scale = 1.5

		self.initialise_dynamic_settings()
		# Fleet direction of 1 represents right, -1 left.
		self.fleet_direction = 1

	def initialise_dynamic_settings(self):
		""" Initialise settings that change throughout the game. """
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		# Fleet direction of 1 represents right, -1 represents left.
		self.fleet_direction = 1

		# Scoring.
		self.alien_points = 10

	def increase_speed(self):
		""" Increase speed settings and alien point values. """
		self.ship_speed_factor *=self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)
class GameStats():
	""" Track statistics for alien invasion. """

	def __init__(self, ai_settings):
		""" Initialise statistics. """
		self.ai_settings = ai_settings
		self.reset_stats()

		# Start game as inactive.
		self.game_active = False

		# High score should never be reset.
		self.high_score = 0

	def reset_stats(self):
		""" Initialise statistics that could change during the game. """
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
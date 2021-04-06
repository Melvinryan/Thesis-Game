from levelbase import *


class Skillbase:
	def __init__(self, name, iden, level, xp, xpn):
		"""
		:param str name: The name of the skill
		:param int iden: The ID of the skill
		:param int level: Initial level to pass to Levelbase Class
		:param int xp: Current amount of XP/SP (passed to Levelbase)
		:param int xpn: XP/SP needed for levelup (passed to Levelbase)
		"""
		self.name = name
		self.id = iden
		self.level = Levelbase(level, xp, xpn)

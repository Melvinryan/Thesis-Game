from enum import Enum
import pygame

import assets
from core.items.item import Item


class Items(Enum):
	EMPTY = Item("Empty", "empty", 0, 1)

	# Tools
	AXE = Item("Axe", "", 1, 1)
	PICKAXE = Item("Pickaxe", "pickaxe", 2, 1)
	HAMMER = Item("Hammer", "hammer", 3, 1)

	# Weapons
	SWORD = Item("Sword", "sword", 25, 1)
	BOW = Item("Bow", "bow", 26, 1)
	GUN = Item("Gun", "gun", 27, 1)

	# Materials
	WOOD = Item("Wood", "wood", 50, 999)
	STONE = Item("Stone", "stone", 51, 999)
	IRON = Item("Iron", "iron", 52, 999)
	SULFUR = Item("Sulfur", "sulfur", 53, 999)
	COPPER = Item("Copper", "copper", 54, 999)
	TIN = Item("Tin", "tin", 55, 999)
	SILVER = Item("Silver", "silver", 56, 999)
	COAL = Item("Coal", "coal", 57, 999)
	GOLD = Item("Gold", "gold", 58, 999)

	# Ores
	LOG = Item("Log", "log", 100, 999)
	IRON_ORE = Item("Iron_Ore", "iron_ore", 101, 999)
	SULFUR_ORE = Item("Sulfur_Ore", "sulfur_ore", 102, 999)
	COPPER_ORE = Item("Copper_Ore", "copper_ore", 102, 999)
	TIN_ORE = Item("Tin_Ore", "tin_ore", 103, 999)
	SILVER_ORE = Item("Silver_Ore", "silver_ore", 104, 999)
	GOLD_ORE = Item("Gold_Ore", "gold_ore", 105, 999)

	@staticmethod
	def getItem(iden):
		"""
		:param int iden: the identifier of the entity type
		:return: Returns entity or None
		:rtype: Item
		"""
		for it in Items:
			if it.value.id == iden:
				return it.value
		return None

	@staticmethod
	def load(game):
		for it in Items:
			if it.value.texturePath is not None:
				it.value.image = pygame.transform.scale(
					assets.get_asset_from_name(game.graphics, it.value.texturePath).image, (64, 64))
				it.value.rect = it.value.image.get_rect()

	@staticmethod
	def getItemFromName(n):
		"""
		:param str n: The name string
		:return: Returns the Item object on success or None on failure
		:rtype: Item
		"""
		try:
			return Items[n.upper()].value
		except KeyError:
			return None

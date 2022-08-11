from base.creation_wand import CreationWand
from Blocks.Containers.Gold_ore_block import GoldOreBlock

class GoldOreCreationWand(CreationWand):
	"""docstring for StickCreateGold"""
	name = 'stick create gold ore'

	def __init__(self):
		super().__init__('stick create gold ore', 'creates a gold ore', 'GODLY', GoldOreBlock, StickCreateGoldOre)

StickCreateGoldOre()
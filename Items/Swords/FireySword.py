from base.sword import Sword

from Functions.effect_overlay import effect_overlay

import links


class FierySword(Sword):

	name = 'Fiery sword'
	desc = 'While holding each turn removed 2 HP'
	dmg = 5
	critical = 0
	rarity = 'common'
	effect = 'Fire'

	def __init__(self):
		self.use = True

	def using(self, obj):
		if not self.use:
			links.used_items.append(self)
			effect_overlay(obj, 2, 'WTS', 'set fire')
			if not(obj.selected is None):
				obj.selected.stop_using(obj)
			obj.inventory[1].remove(self)
			obj.selected = self
			obj.mid_dmg += self.dmg
			obj.crit += self.crit
	
	def stop_using(self, obj):
		self.use = False
		del links.intoxicated[obj]
		obj.mid_dmg -= self.dmg
		obj.crit -= self.crit
		links.used_items.remove(self)
		obj.add_to_inventory(self)
		obj.selected = None

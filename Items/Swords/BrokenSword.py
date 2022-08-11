from base.sword import Sword


class BrokenSword(Sword):
	name = 'Broken sword'
	desc = 'Size isn\'t important!'
	dmg = 2
	critical = 0
	rarity = 'common'
	effect = 'break'


BrokenSword()

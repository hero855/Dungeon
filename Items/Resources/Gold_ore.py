from base.resource import Resource
from Items.Resources.Gold_bar import GoldBar


class GoldOre(Resource):
	type_ = 'Resource'
	name = 'Gold ore'
	desc = 'You can melt a gold bar'
	rarity = 'common'

	# TODO: move this action to oven class
	def remelting(self, oven, obj, index):
		obj.backpack[index].remove(self)
		for slot in oven.slots:
			if len(slot) == 0:
				slot.append(GoldBar())
				break
			elif type(slot[0]) is GoldBar:
				slot.append(GoldBar())
				break

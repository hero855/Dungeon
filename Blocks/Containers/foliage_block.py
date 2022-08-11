from base.container import Container
from Items.Resources.Foliage import Foliage

class FoliageBlock(Container):
	def give(self, obj):
		obj.add_to_inventory([Foliage for _ in range(0, 2)])

from base.resource import Resource
from Items.Resources.Raw_stone import RawStone

from Blocks.Functional.workbench import Workbench


class Stone(Resource):
	name = 'Stone'


Stone.recipe = {RawStone: 6, 'result': Stone, 'num': 1, 'pace': Workbench}

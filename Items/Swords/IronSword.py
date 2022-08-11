from base.sword import Sword
from Items.Resources.Board import Board
from Items.Resources.Iron_bar import IronBar

from Blocks.Functional.workbench import Workbench


class IronSword(Sword):
	name = 'Iron Sword'
	desc = 'Simply sword, not expected, Yes?'
	dmg = 10
	critical = 0
	rarity = 'common'


IronSword.recipe = {Board: 2, IronBar: 4, 'result': IronSword, 'num': 1, 'place': Workbench}

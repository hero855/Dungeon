from base.resource import Resource
from Items.Resources.Broken_board import BrokenBoard

from Blocks.Functional.workbench import Workbench


class Board(Resource):
	name = 'Board'


Board.recipe = {BrokenBoard: 2, 'result': Board, 'num': 1, 'place': Workbench}

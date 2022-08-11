from base.container import Container
from random import randint

from Blocks.Functional.workbench import Workbench


class StoneBlock(Container):

    pic = '#'
    type_ = 'Block'

    def __init__(self):
        from items import RawStone
        self.recipe = {RawStone: 4, 'result': StoneBlock, 'num': 1, 'place': Workbench}

    def give(self, obj):
        # TODO: move to player
        obj.add_to_inventory([RawStone() for _ in range(randint(3, 5))])

        if randint(1, 100) in range(30):
            obj.add_to_inventory([Stone() for _ in range(randint(1, 3))])

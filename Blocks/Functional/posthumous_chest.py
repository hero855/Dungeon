import termcolor

from Functions.choice_of import choice_of
from base.functional import Functional


class PosthumousChest(Functional):
    """
    Chest with all the items of the Avatar, which is created at death
    """

    pic = termcolor.colored('%', 'blue')

    def __init__(self, player):
        self.name = 'Die chest'
        self.type_ = 'Triger'
        self.desc = 'Something'
        self.items = player.backpack.copy()

    def act(self, player):
        """Open it"""

        player.in_the_process = self

        item, idx, col, esc = choice_of(player.backpack, self.items, idx=obj.idx)

        if esc:
            player.in_the_process = None
            player.idx = 0

        if col == 'sec':
            self.object.add_to_inventory(item)
            self.inventory[idx] = None

        elif None in self.items:
            self.items[self.items.index(None)] = item
            obj.backpack[idx] = None

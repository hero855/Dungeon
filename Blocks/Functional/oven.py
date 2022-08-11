from pynput.keyboard import Key

from Functions.smart_input import smart_input
from Functions.choice_of import choice_of

from base.functional import Functional
from base.resource import Resource


class Oven(Functional):

    pic = '&'

    def __init__(self):
        self.name = 'Oven'
        self.type_ = 'Triger'
        self.desc = 'Something'
        self.slots = [[] for _ in range(5)]

    def act(self, player):

        player.in_the_process = self

        player.slots()

        item, idx, col, esc = choice_of(player.backpack, self.slots, idx=player.idx)

        if esc:
            player.in_the_process = None
            player.idx = 0

        if col == 0:
            if isinstance(item, list):
                if isinstance(item[0], Resource):
                    for bar in item:
                        bar.melting(self, player, idx-1)
        
        elif col == 1:
            if item:
                player.add_to_inventory(item)
                self.slots[idx].clear()

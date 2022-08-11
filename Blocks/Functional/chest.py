from random import randint, choice
from termcolor import colored
from time import sleep

from Functions.choice_of import choice_of
from base.functional import Functional
from Blocks.Functional.workbench import Workbench
from items import Board, IronBar


class Chest(Functional):
    name = 'Chest'
    type_ = 'Trigger'
    desc = 'Something'
    pic = colored('C', 'yellow')

    def __init__(self, rarity=None):
        self.recipe = {Board: 5, IronBar: 1, 'place': Workbench, 'resut': Chest}
        self.items = list()
        self.open = False
        self.rarity = rarity
        if self.rarity is None:
            # rarity_of(self)
            self.rarity = 'common'
        super().__init__()

    def generate_random_item(self, rarity, num_of_items):
        # TODO: return items instead adding in-method
        types_of_items = ['Sword', 'Drug', 'Resource']

        for count in range(num_of_items):
            type_ = choice(types_of_items)
            if type_ == 'Resource':
                num = randint(5, 20)
                res = choice(items[rarity][type_])
                item = [res() for _ in range(1, num)]
            else:
                item = choice(items[rarity][type_])()

            self.items.append(item)

    def generator(self):

        if self.rarity == 'common':
            self.generate_random_item(rarity='common', num_of_items=randint(2, 4))

        elif self.rarity == 'rare':
            self.generate_random_item(rarity='common', num_of_items=randint(2, 5))
            self.generate_random_item(rarity='rare', num_of_items=randint(1, 2))

        elif self.rarity == 'Epic':
            self.generate_random_item(rarity='common', num_of_items=randint(5, 10))
            self.generate_random_item(rarity='rare', num_of_items=randint(2, 5))
            self.generate_random_item(rarity='Epic', num_of_items=randint(1, 2))

        elif self.rarity == 'GODLY':
            self.generate_random_item(rarity='common', num_of_items=randint(8, 16))
            self.generate_random_item(rarity='rare', num_of_items=randint(4, 10))
            self.generate_random_item(rarity='Epic', num_of_items=randint(0, 2))
            self.generate_random_item(rarity='GODLY', num_of_items=1)

        for count in range(20 - len(self.items)): self.items.append(None)

    def act(self, player):
        """
        The first time creates in the chest of random things,
        depending on the rarity of the chest.
        Open it.
        """

        if not self.open:
            self.generator()
            self.open = True
            self.pic = colored('c', 'yellow')

        print(f'\n{self.rarity}\n')
        sleep(0.5)

        player.focused_utility_block = self

        item, player.idx, player.col, esc = choice_of(player.backpack, self.items, player.idx, player.col)

        if esc:
            player.focused_utility_block = None
            player.idx = 0
            player.col = 'fst'

        if player.col == 'sec':
            player.add_to_inventory(item)
            self.items[player.idx] = None

        elif None in self.items:
            self.items[self.items.index(None)] = item
            player.backpack[player.idx] = None

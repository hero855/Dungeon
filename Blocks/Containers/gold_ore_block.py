from random import randint, choice
from termcolor import colored
from time import sleep

from base.container import Container
from Items.Resources.Gold_ore import GoldOre


class GoldOreBlock(Container):
    
    # pic = colored('*', 'yellow')
    pic = '*'
    
    def give(self, obj):
        num = randint(1, 3)
        exp = randint(3, 7)
        # TODO: move this to player class
        obj.add_to_inventory([GoldOre() for _ in range(num)])
        obj.Exp += exp
        print(f'You got: {num} gold ore and {exp} exp')
        sleep(0.8)

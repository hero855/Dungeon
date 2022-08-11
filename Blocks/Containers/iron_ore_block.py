from random import randint
from time import sleep

from base.container import Container
import links

class IronOreBlock(Container):
    
    pic = '*'
    
    def give(self, obj):
        num = randint(1, 3)
        exp = randint(1, 4)
        obj.add_to_inventory([IronOre() for _ in range(num)])
        obj.Exp += exp
        print(f'You got: {num} iron ore and {exp} exp')
        sleep(0.8)
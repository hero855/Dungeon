import random

from Blocks.Containers.gold_ore_block import GoldOreBlock
from Blocks.Containers.iron_ore_block import IronOreBlock
from Blocks.Containers.ground_block import GroundBlock
from Blocks.Containers.stone_block import StoneBlock
from Blocks.Containers.wall import Wall
from Blocks.Containers.box import Box
from Blocks.Containers.pot import Pot
from Blocks.air import Air

from Blocks.Functional.simulator import Simulator
from Blocks.Functional.spike import Spike
from Blocks.Functional.chest import Chest


from Generations.rooms import Rooms, Room


def generator_for_blocks(location, area, height_of_ground):

    x = location.x
    y = location.y
    z = location.z

    #num  = random.randint(1, 10000)

    if z > height_of_ground:
        block = Air
    
    # elif z == height_of_ground:

    #     # if num in range(15 * 100):
    #     #   if random.randint(0, 1) == 0: block = Box
    #     #   else:                  block = Pot
    #     if num in range(30 * 100):
    #         block = StoneBlock
    #     else:
    #         block = Air

    elif z <= height_of_ground:

        block = StoneBlock

        # if   num in range( 3 * 100): block = GoldOreBlock
        # elif num in range(12 * 100): block = IronOreBlock
        # elif num in range(40 * 100): block = StoneBlock
        # else:                        block = GroundBlock
    
    area.map[z, y, x] = block()

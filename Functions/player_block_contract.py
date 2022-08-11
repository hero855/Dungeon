from Blocks.Functional.spike import Spike
from Blocks.Functional.door import Door
from Blocks.air import Air

from base.functional import Functional
from base.container import Container


def player_block_contract(player, direction, type_):
    z = player.z
    y = player.y
    x = player.x

    if direction == 'North':
        y -= 1
    elif direction == 'East':
        x += 1
    elif direction == 'South':
        y += 1
    elif direction == 'West':
        x -= 1
    elif direction == 'up':
        z += 1
    elif direction == 'down':
        z -= 1

    cell = player.map[z][y][x]

    if type_ == 'mov' and isinstance(cell, (Spike, Door, Air)):
        # TODO: replace with in-place algorithm
        cell.walk(player, z, y, x)

    elif type_ == 'raze' and isinstance(cell, (Container, Functional)):
        # TODO: replace with in-place algorithm
        cell.destroy(player, z, y, x)

    elif type_ == 'locate' and not type(cell) is Air:
        player.locate(z, y, x)

    elif type_ == 'hit':
        player.give_hit(cell, z, y, x)

    # elif type_ == 'act' and isinstance(cell, (Functional, NPC)):
    #     if type(cell) is Spike:
    #         cell.act(player, z, y, x)
    #     else:
    #         cell.act(player)

import time
import os

from Generations.area import Area
from Functions.smart_input import smart_input
from Functions.effect import effect
from Functions.player_block_contract import player_block_contract
from player import Player
from links import directions, actions, spec_input


area = Area('TestArea')
player = Player(area)
area.update(player.location)
area.map[0][0][0] = player
print(player.area.name)
time.sleep(1)

while True:
    os.system('cls')
    area.show(player)

    d = directions
    d.update(actions)
    d.update(spec_input)

    player_input = smart_input(d)

    #area.update(player.location)
    player.update()
    effect()

    if player.focused_utility_block:
        player.focused_utility_block.act(player)
        continue

    match player_input:
        case 'North' | 'East' | 'South' | 'West' | 'up' | 'down':
            player_block_contract(player, player_input, 'mov')
        case 'raze' | 'locate' | 'hit' | 'act':
            sec_choice = smart_input(directions)
            player_block_contract(player, sec_choice, player_input)
        case 'inv':
            player.open_inventory()
        case 'skills':
            player.skill_tree()
        case 'esc':
            exit()

    #area.update(player.location)
    player.update()
    player.fall()


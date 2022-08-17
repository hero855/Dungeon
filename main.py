import time
import os

os.system('python -m unittest')

from Generations.area import Area
from Functions.smart_input import smart_input
from Functions.effect import effect
from Functions.player_block_contract import player_block_contract
from player import Player
from links import directions, actions, spec_input


area = Area('TestArea', height_of_chunk=40)
area.initial_update()
player = Player(area, x=0, y=0, z=11)
area.update(player.location)
player.update()
print(player.area.name)
time.sleep(1)

while True:
    os.system('cls')
    player.update()
    area.update(player.location)

    player.stat()
    area.render(player.location, radius=10)

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


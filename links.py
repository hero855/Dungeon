from pynput.keyboard import Key


WAYS = [
    'North',
    'South',
    'East',
    'West'
]

RARITIES = [
    'common',
    'rare',
    'Epic',
    'GODLY'
]

TYPES_OF_ITEMS = [
    'Helmet',
    'Torso',
    'Leggings',
    'Shoes',
    'Sword',
    'Drug',
    'Wings',
    'Stick',
    'Ring',
    'Resource'
]

directions = {
    Key.up: 'North',
    Key.right: 'East',
    Key.down: 'South',
    Key.left: 'West',
    Key.space: 'up',
    Key.ctrl_l: 'down'
}

actions = {
    'e': 'act',
    'h': 'hit',
    'i': 'inv',
    'k': 'skills',
    'b': 'raze',
    'l': 'locate'
}

spec_input = {
    Key.esc: 'esc',
    Key.enter: None
}

enemies = list()
used_items = list()
intoxicated = dict()

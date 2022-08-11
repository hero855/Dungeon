import random

from links import ways
from Functions.player_block_contract import distributor

def random_moving(obj, *dirs):

    if 'all' in dirs:
        random_dir = random.choice(ways)
    else:
        random_dir = random.choice(dirs)
    distributor(obj, random_dir, 'mov')
from Enemys.Goblin import Goblin
from Enemys.Cravler import Cravler

'''TODO: FIXFIXFIX'''
def spawn_enemy(row, elm, map_, types=None):

    if types:

        if len(types) > 1:
            sorted(types, key=lambda x: x[::-1])
            num = randint(1, 100)
            for enemy, chance in types.items:
                if num in range(chance):
                    enemy(row, elm, map_)

        else:  # len = 1
            self = types()

    else:            
        chance = randint(1, 100)

        if chance in range(50):
            Goblin(row, elm, map_)
        else:
            Cravler(row, elm, map_)

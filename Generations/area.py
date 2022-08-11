from Generations.chank import Chank
from Generations.axis import Axis
from opensimplex import OpenSimplex

from Blocks.Functional.spike import Spike
from Blocks.air import Air
from Generations.vector import Vector3


class Area(object):

    def __init__(self, name, len_of_chank=15):
        self.name = name
        self.len_of_chank = len_of_chank

        # self.simplex = OpenSimplex
        self.map = Axis([Axis([Axis([None])])])
        self.chank_map = Axis([Axis([Chank(self, 0, 0)])])
        self.chank_map[0][0].generate_heights()
        self.chank_map[0][0].generate_blocks()

    def update(self, location_of_player: Vector3):
        location_of_player /= self.len_of_chank
        x = int(location_of_player.x)
        y = int(location_of_player.y)
        chank = self.chank_map[y][x]
        if not chank.is_sanded_message:
            chank.send(r=1)

    def show(self, location_of_player: Vector3, radius=5):
        """Show the map and the objects on it to the player"""

        x = location_of_player.x
        y = location_of_player.y
        z = location_of_player.z

        y_start = min([y - radius, len(self.map) - y])
        y_final = int(y + min([radius + 1, self.map.half - y - 1]))

        x_start = min([x - radius, len(self.map) - x])
        x_final = int(x + min([radius + 1, self.map.half - x - 1]))

        for row in self.map[z][y_start: y_final]:
            for elm in row[x_start: x_final]:
                if isinstance(elm, (Air, Spike)):
                    print(elm.pic(z, self.map[z].index(row), row.index(elm), self.map), end='')
                elif elm is None:
                    print(' ', end='')
                else:
                    print(elm.pic, end='')
            # next row
            print()

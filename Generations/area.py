from pprint import pprint

from Generations.chunk import Chunk
from Generations.axis import Axis
from Generations.chunk_map import ChunkMap
from Generations.plot_3d import Plot3D

from Blocks.Functional.spike import Spike
from Blocks.air import Air
from Generations.vector import Vector3


class Area:

    def __init__(self, name, height_of_chunk=20, width_of_chunk=15):
        self.name = name
        self.width_of_chunk = width_of_chunk
        self.height_of_chunk = height_of_chunk

        self.map = Plot3D()
        self.chunk_map = ChunkMap(self)

    def initial_update(self):
        self.chunk_map[0, 0] = Chunk(self, 0, 0, self.height_of_chunk, self.width_of_chunk)
        self.chunk_map[0, 0].generate_heights()
        self.chunk_map[0, 0].generate_blocks()

    def update(self, location_of_player: Vector3):
        location_of_player /= self.width_of_chunk
        x = int(location_of_player.x)
        y = int(location_of_player.y)
        chunk = self.chunk_map[y, x]
        if not chunk.is_sanded_message:
            chunk.send(r=1)

    def show(self, location_of_player: Vector3, radius=5):
        """Show the map and the objects on it to the player"""

        x = location_of_player.x
        y = location_of_player.y
        z = location_of_player.z

        y_start = y - radius
        y_final = y + radius + 1

        x_start = x - radius
        x_final = x + radius + 1

        slice_to_render = self.map[z, y_start: y_final, x_start: x_final][0]

        for elm_y, row in enumerate(slice_to_render):
            for elm_x, elm in enumerate(row):
                if isinstance(elm, (Air, Spike)):
                    print(elm.pic(z, elm_y, elm_x, self.map), end='')
                elif elm is None:
                    print(' ', end='')
                else:
                    print(elm.pic, end='')
            # next row
            print()

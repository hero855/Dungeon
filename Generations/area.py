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
        chunk_location = self.get_chunk_location(location_of_player)
        chunk = self.chunk_map[chunk_location]
        chunk.send(r=1)

    def render(self, location_of_player: Vector3, radius=5):
        """Shows the map and the objects on it to the player"""

        x_range, y_range, z_range = self.calc_ranges(location_of_player, radius)
        slice_to_render = self.map[z_range, y_range, x_range][0]

        for elm_y, row in enumerate(slice_to_render):
            for elm_x, elm in enumerate(row):
                if isinstance(elm, (Air, Spike)):
                    x = x_range.start + elm_x
                    y = y_range.start + elm_y
                    z = z_range.start
                    print(elm.pic(z, y, x, self.map), end=' ')
                elif elm is None:
                    print(' ', end=' ')
                else:
                    print(elm.pic, end=' ')
            # next row
            print()

    def get_chunk_location(self, location_of_player: Vector3):
        chunk_location = location_of_player / (self.width_of_chunk - self.width_of_chunk / 2)
        chunk_x = int(chunk_location.x)
        chunk_y = int(chunk_location.y)
        return chunk_x, chunk_y
    
    def calc_ranges(self, location_of_player: Vector3, radius):
        x, y, z = location_of_player

        x_start = x - radius
        x_final = x + radius + 1
        
        y_start = y - radius
        y_final = y + radius + 1

        x_slice = slice(x_start, x_final)
        y_slice = slice(y_start, y_final)
        z_slice = slice(z, z + 1)

        return x_slice, y_slice, z_slice

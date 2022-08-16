from Functions.generator_for_blocks import generator_for_blocks
from Generations.axis import Axis
from Generations.plot_2d import Plot2D
from Generations.vector import Vector2, Vector3


class Chunk(object):

    def __init__(self, area, x, y, height=20, width=11):
        self.area = area
        self.x = x
        self.y = y
        self.width = width  # lengthier of rows and elms
        self.height = height
        self.is_generated = False
        self.is_sanded_message = False
        self.heights_map = Plot2D()

    def update(self):
        if not self.is_generated:
            self.generate_heights()
            self.generate_blocks()
        if not self.is_sanded_message:
            self.send(2)

    def generate_heights(self):
        half = int(self.width / 2)
        for row in range(-half, half + 1):
            for elm in range(-half, half + 1):
                height = 10
                self.heights_map[row, elm] = height

    def generate_blocks(self):
        self.is_generated = True

        half = int(self.width / 2)
        lay_range = range(self.height)
        row_range = range(-half, half + 1)
        elm_range = range(-half, half + 1)

        for lay in lay_range:
            for row in row_range:
                for elm in elm_range:
                    height = self.heights_map[row, elm]
                    location = Vector3(self.y * self.width + elm, self.x * self.width + row, lay)
                    generator_for_blocks(location, self.area, height)

    def send(self, r: int):
        """
        # # # # # # #
        # # # # # # #
        # # # # # # #
        # # # c # # #
        # # # # # # # \
        # # # # # # # | > r
        # # # # # # # /
        """
        self.is_sanded_message = True

        y_start = self.y - r
        y_stop = self.y + r + 1
        x_start = self.x - r
        x_stop = self.x + r + 1
        map_slice = self.area.chunk_map[y_start: y_stop, x_start: x_stop]

        for row in map_slice:
            for chunk in row:
                if not chunk.is_generated:
                    chunk.generate_heights()
                    chunk.generate_blocks()

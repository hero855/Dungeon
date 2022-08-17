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

    def generate(self):
        if self.is_generated:
            return

        self.is_generated = True
        self.generate_heights()
        self.generate_blocks()

    def generate_heights(self):
        half = int(self.width / 2)
        for row in range(-half, half + 1):
            for elm in range(-half, half + 1):
                height = 10
                self.heights_map[row, elm] = height

    def generate_blocks(self):
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
        if self.is_sanded_message:
            return

        self.is_sanded_message = True

        y_slice = slice(self.y - r, self.y + r + 1)
        x_slice = slice(self.x - r, self.x + r + 1)
        map_slice = self.area.chunk_map[y_slice, x_slice]

        for row in map_slice:
            for chunk in row:
                chunk.generate()

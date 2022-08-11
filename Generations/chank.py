import math

from Functions.generator_for_blocks import generator_for_blocks
from Generations.axis import Axis
from Generations.vector import Vector2, Vector3


class Chank(object):

    def __init__(self, area, x, y, length=11):
        self.area = area
        self.length = length  # lengthier of rows and elms
        self.is_generated = False
        self.is_sanded_message = False
        self.heights_map = Axis([])

    def update(self):
        if not self.is_generated:
            self.generate_heights()
            self.generate_blocks()
        if not self.is_sanded_message:
            self.send(2)

    @property
    def map_coordinates(self):
        for row in self.area.chank_map.values:
            for chank in row.values:
                if chank is self:
                    half = math.floor(self.length / 2)
                    x = row.index(chank)
                    y = self.area.chank_map.index(row)
                    x = x * self.length - half
                    y = y * self.length - half
                    return Vector2(y, x)

    @property
    def ch_map_coordinates(self):
        for row in self.area.chank_map.values:
            for chank in row.values:
                if chank is self:
                    x = row.index(chank)
                    y = self.area.chank_map.index(row)
                    return Vector2(y, x)

    def generate_heights(self):
        for row in range(self.length):
            self.heights_map[row] = Axis([])
            for elm in range(self.length):
                height = 10
                print(f'{row = } {self.heights_map[row] = }')
                self.heights_map[row][elm] = height

    def generate_blocks(self):
        self.is_generated = True

        start_row, start_elm = self.map_coordinates

        for lay in range(len(self.area.map)):
            for row in range(self.length):
                for elm in range(self.length):
                    height = self.heights_map[row][elm]
                    location = Vector3(lay, start_row + row, start_elm + elm)
                    generator_for_blocks(location, self.area.map, height)

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

        x = self.map_coordinates.x
        y = self.map_coordinates.y

        for row in self.area.chank_map[y - r: y + r + 1]:
            for chank in row[x - r: x + r + 1]:
                if not chank.is_generated:
                    chank.generate_heights()
                    chank.generate_blocks()

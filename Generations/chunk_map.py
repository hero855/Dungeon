from Generations.chunk import Chunk
from Generations.plot_2d import Plot2D


class ChunkMap:
    def __init__(self, area):
        self.__plot = Plot2D()
        self.area = area

    def __getitem__(self, target):
        y, x = target

        rows_range = range(y.start, y.stop) if isinstance(y, slice) else range(y, y + 1)
        elms_range = range(x.start, x.stop) if isinstance(x, slice) else range(x, x + 1)

        for row_index in rows_range:
            for elm_index in elms_range:
                element = self.__plot[row_index, elm_index]
                if not isinstance(element, Chunk):
                    new_chunk = Chunk(
                        self.area,
                        elm_index,
                        row_index,
                        self.area.height_of_chunk,
                        self.area.width_of_chunk
                    )
                    self.__plot[row_index, elm_index] = new_chunk

        return self.__plot[target]

    def __setitem__(self, target, value):
        self.__plot[target] = value

from Generations.axis import Axis
from Generations.chunk_map import ChunkMap


class GameMap:
    def __init__(self, elms, rows, lays):
        self.map = Axis([Axis([Axis([None for _ in range(elms)]) for _ in range(rows)]) for _ in range(lays)])

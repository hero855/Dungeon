import math

from Generations.axis import Axis
from Generations.vector import Vector

#
# print(self.name)
# print()
# print('create a big dummy')
#
# self.map = Axis([Axis([Axis([None for _ in range(self.ELMS)]) for _ in range(self.ROWS)]) for _ in
#                  range(self.LAYS)])
#
# os.system('cls')
#
# x_len = int(self.ELMS / (self.LEN_OF_CHUNK * 2))
# y_len = int(self.ROWS / (self.LEN_OF_CHUNK * 2))
# z_len = int(self.LAYS / (self.LEN_OF_CHUNK * 2))
#
# list_of_axis = list()
# for row in range(-y_len, y_len):
#     list_of_chunks = list()
#     for elm in range(-x_len, x_len):
#         chunk = Chunk(row, elm, self, length=self.LEN_OF_CHUNK)
#         list_of_chunks.append(chunk)
#     axis = Axis(list_of_chunks)
#     list_of_axis.append(axis)
# self.chunk_map = Axis(list_of_axis)
#
# self.vector_map = Axis([Axis([[] for elm in range(math.ceil(self.ELMS / self.LEN_OF_CHUNK))]) for row in
#                         range(math.ceil(self.ROWS / self.LEN_OF_CHUNK))])
#
# map_ = Axis([Axis([None for elm in range(math.ceil(self.ELMS / self.LEN_OF_CHUNK + 2))]) for row in range(
#     math.ceil(self.ROWS / self.LEN_OF_CHUNK + 2))])
#
# vector_row = -math.ceil(len(self.vector_map) / 2)
# for row in range(-map_.RADIUS, map_.RADIUS):
#     vector_elm = -math.ceil(len(self.vector_map[0]) / 2)
#     for elm in range(-map_[0].RADIUS, map_[0].RADIUS):
#         map_[row][elm] = Vector(vector_elm, vector_row)
#         vector_elm += 1
#     vector_row += 1
#
# vector_row = -math.ceil(len(self.vector_map) / 2) + 1
# for row in range(-map_.RADIUS, map_.RADIUS - 1):
#     vector_elm = -math.ceil(len(self.vector_map[0]) / 2) + 1
#     for elm in range(-map_[0].RADIUS, map_[0].RADIUS - 1):
#         vector_list = self.vector_map[vector_row][vector_elm]
#         vector_list.append(map_[row][elm])
#         vector_list.append(map_[row][elm + 1])
#         vector_list.append(map_[row + 1][elm + 1])
#         vector_list.append(map_[row + 1][elm])
#         vector_elm += 1
#     vector_row += 1
#
# del map_
#
# self.chunk_map[0][0].generator()
#
#
# # chunk.msg()

class VectorMap:
    def __init__(self, elms, rows, len_of_chunk):
        self.vector_map = Axis([Axis([[] for _ in range(math.ceil(elms / len_of_chunk))]) for _ in
                                range(math.ceil(rows / len_of_chunk))])

        map_ = Axis([Axis([None for _ in range(math.ceil(elms / len_of_chunk + 2))]) for _ in range(
            math.ceil(rows / len_of_chunk + 2))])

        vector_row = -math.ceil(len(self.vector_map) / 2)
        for row in range(-map_.half, map_.half):
            vector_elm = -math.ceil(len(self.vector_map[0]) / 2)
            for elm in range(-map_[0].half, map_[0].half):
                map_[row][elm] = Vector(vector_elm, vector_row)
                vector_elm += 1
            vector_row += 1

        # vector_row = -math.ceil(len(self.vector_map) / 2) + 1
        # for row in range(-map_.half, map_.half - 1):
        #     vector_elm = -math.ceil(len(self.vector_map[0]) / 2) + 1
        #     for elm in range(-map_[0].half, map_[0].half - 1):
        #         vector_list = self.vector_map[vector_row][vector_elm]
        #         vector_list.append(map_[row][elm])
        #         vector_list.append(map_[row][elm + 1])
        #         vector_list.append(map_[row + 1][elm + 1])
        #         vector_list.append(map_[row + 1][elm])
        #         vector_elm += 1
        #     vector_row += 1

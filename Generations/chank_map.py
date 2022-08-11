from Generations.axis import Axis
from Generations.chank import Chank


class ChankMap:
    def __init__(self, area):
        x_len = int(area.elms / (area.len_of_chank * 2))
        y_len = int(area.rows / (area.len_of_chank * 2))
        z_len = int(area.lays / (area.len_of_chank * 2))

        list_of_axis = list()
        for row in range(-y_len, y_len):
            list_of_chanks = list()
            for elm in range(-x_len, x_len):
                chank = Chank(row, elm, area, length=area.len_of_chank)
                list_of_chanks.append(chank)
            axis = Axis(list_of_chanks)
            list_of_axis.append(axis)
        self.map = Axis(list_of_axis)
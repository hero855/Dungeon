from codecs import raw_unicode_escape_decode
from pprint import pprint
from Generations.axis import Axis


class Plot3D:
    def __init__(self):
        self.__axes = Axis([Axis([Axis([None])])])

    def __getitem__(self, target):
        if not isinstance(target, tuple):
            raise TypeError(
                f"Plot indices must be tuple, not {type(target).__name__}")

        if len(target) != 3:
            raise TypeError(
                f"Plot3D[z, y, x] takes 3 positional indices but {len(target)} were given")

        isSlice = any(isinstance(coord, slice) for coord in target)

        if isSlice:
            for coord in target:
                if isinstance(coord, slice) and not isinstance(coord.step, type(None)):
                    raise ValueError(f"Steps are not available in plot slices")

        z, y, x = target

        lays_range = range(z.start, z.stop) if isinstance(
            z, slice) else range(z, z + 1)
        rows_range = range(y.start, y.stop) if isinstance(
            y, slice) else range(y, y + 1)
        elms_range = range(x.start, x.stop) if isinstance(
            x, slice) else range(x, x + 1)

        # finds Nones where axes should be
        # and replaces when found
        for lay_index in lays_range:
            lay = self.__axes[lay_index]
            if not isinstance(lay, Axis):
                assert isinstance(lay, type(None))
                self.__axes[lay_index] = Axis([Axis([None])])
            for row_index in rows_range:
                row = self.__axes[lay_index][row_index]
                if not isinstance(row, Axis):
                    assert isinstance(row, type(None))
                    self.__axes[lay_index][row_index] = Axis([None])
                for elm_index in elms_range:
                    elm = self.__axes[lay_index][row_index][elm_index]
                    assert not isinstance(elm, Axis)

        if isSlice:
            res = []
            for lay_index in lays_range:
                lay = []
                for row_index in rows_range:
                    row = []
                    for elm_index in elms_range:
                        row.append(self.__axes[lay_index]
                                   [row_index][elm_index])
                    lay.append(row)
                res.append(lay)
            return res

        return self.__axes[z][y][x]

    def __setitem__(self, target, value):
        if not isinstance(target, tuple):
            raise TypeError(
                f"Plot indices must be tuple, not {type(target).__name__}")

        if len(target) != 3:
            raise TypeError(
                f"Plot3D[z, y, x] takes 3 positional indices but {len(target)} were given")

        isSlice = any(isinstance(coord, slice) for coord in target)

        if isSlice:
            for coord in target:
                if isinstance(coord, slice) and not isinstance(coord.step, type(None)):
                    raise ValueError(f"Steps are not available in plot slices")

            len_value_first_lay = len(value[0])
            len_value_first_row = len(value[0][0])
            for lay in value:
                if len(lay) != len_value_first_lay:
                    raise ValueError("Lays of value are not the same length")
                for row in lay:
                    if len(row) != len_value_first_row:
                        raise ValueError("Rows of value are not the same length")
            
            len_slice = target[0].stop - target[0].start
            len_slice_lay = target[1].stop - target[1].start
            len_slice_row = target[2].stop - target[2].start
            if len_slice != len(value):
                raise ValueError("Slice and value are not the same length")
            if len_slice_lay != len_value_first_lay:
                raise ValueError("Slice's and value's lays are not the same length")
            if len_slice_row != len_value_first_row:
                raise ValueError("Slice's and value's rows are not the same length")


        z, y, x = target

        lays_range = range(z.start, z.stop) if isinstance(
            z, slice) else range(z, z + 1)
        rows_range = range(y.start, y.stop) if isinstance(
            y, slice) else range(y, y + 1)
        elms_range = range(x.start, x.stop) if isinstance(
            x, slice) else range(x, x + 1)

        # finds Nones where axes should be
        # and replaces when found
        for lay_index in lays_range:
            lay = self.__axes[lay_index]
            if not isinstance(lay, Axis):
                assert isinstance(lay, type(None))
                self.__axes[lay_index] = Axis([Axis([None])])
            for row_index in rows_range:
                row = self.__axes[lay_index][row_index]
                if not isinstance(row, Axis):
                    assert isinstance(row, type(None))
                    self.__axes[lay_index][row_index] = Axis([None])
                for elm_index in elms_range:
                    elm = self.__axes[lay_index][row_index][elm_index]
                    assert not isinstance(elm, Axis)

        if isSlice:
            lay_counter = 0
            for lay_index in lays_range:
                row_counter = 0
                for row_index in rows_range:
                    elm_counter = 0
                    for elm_index in elms_range:
                        element = value[lay_counter][row_counter][elm_counter]
                        self.__axes[lay_index][row_index][elm_index] = element
                        elm_counter += 1
                    row_counter += 1
                lay_counter += 1
            return

        self.__axes[z][y][x] = value

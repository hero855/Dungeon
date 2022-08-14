from Generations.axis import Axis
from typing import List


class Plot2D:
    """ TODO: make 2d slices for plot
    """

    def __init__(self):
        self.__axes = Axis([Axis([None])])

    def __getitem__(self, target):
        if not isinstance(target, tuple):
            raise TypeError(
                f"Plot indices must be tuple, not {type(target).__name__}")

        if not len(target) == 2:
            raise TypeError(
                f"Plot2D[y, x] takes 2 positional indices but {len(target)} were given")

        isSlice = any(isinstance(coord, slice) for coord in target)

        y, x = target

        rows_range = range(y.start, y.stop) if isinstance(y, slice) else range(y, y + 1)
        elms_range = range(x.start, x.stop) if isinstance(x, slice) else range(x, x + 1)

        if isinstance(y, int) and not isinstance(self.__axes[y], Axis):
            assert isinstance(self.__axes[y], type(None))
            self.__axes[y] = Axis([None])

        if isSlice and not all(isinstance(row, Axis) for row in self.__axes[y]):
            for row_index in rows_range:
                row = self.__axes[row_index]
                if not isinstance(row, Axis):
                    assert isinstance(row, type(None))
                    self.__axes[row_index] = Axis([None])

        assert not isinstance(self.__axes[y][x], Axis)

        if any(isinstance(coord, slice) for coord in target):
            for coord in target:
                if isinstance(coord, slice) and not isinstance(coord.step,  type(None)):
                    raise ValueError("Steps are not available in plot slices")
            res = []
            for row_index in rows_range:
                row = []
                for elm_index in elms_range:
                    row.append(self.__axes[row_index][elm_index])
                res.append(row)
            return res

        return self.__axes[y][x]

    def __setitem__(self, target, value):
        if not isinstance(target, tuple):
            raise TypeError(
                f"Plot indices must be tuple, not {type(target).__name__}")

        if len(target) != 2:
            raise TypeError(
                f"Plot[y, x] takes 2 positional indices but {len(target)} where given")

        isSlice = any(isinstance(coord, slice) for coord in target)

        if isSlice:
            for coord in target:
                if isinstance(coord, slice) and not isinstance(coord.step, type(None)):
                    raise ValueError(f"Steps are not available in plot slices")

            len_value_first_row = len(value[0])
            for row in value:
                if len(row) != len_value_first_row:
                    raise ValueError("Rows of value are not the same length")

            len_slice = target[0].stop - target[0].start
            len_slice_row = target[1].stop - target[1].start
            if len_slice != len(value):
                raise ValueError("Slice and value are not the same length")
            if len_slice_row != len_value_first_row:
                raise ValueError(
                    "Slice's and value's rows are not the same length")

        y, x = target

        if isinstance(y, int):
            if not isinstance(self.__axes[y], Axis):
                assert isinstance(self.__axes[y], type(None))
                self.__axes[y] = Axis([None])

        if isinstance(y, slice):
            if not all(isinstance(row, Axis) for row in self.__axes[y]):
                for row_index in range(y.start, y.stop):
                    if not isinstance(self.__axes[row_index], Axis):
                        assert isinstance(self.__axes[row_index], type(None))
                        self.__axes[row_index] = Axis([None])

        assert not isinstance(self.__axes[y][x], Axis)

        if isSlice:
            values_first_row_len = len(value[0])
            for row in value:
                if len(row) != values_first_row_len:
                    raise ValueError("Rows of value are not the same length")

            if not isinstance(y.step, type(None)) or not isinstance(x.step, type(None)):
                raise ValueError("Steps are not available in plot slices")

            len_rows = y.stop - y.start
            len_elms = x.stop - x.start

            if len_rows != len(value):
                raise ValueError(
                    "Slice rows and value rows are not the same length")

            # other rows are the same length bc of check up here
            if len_elms != len(value[0]):
                raise ValueError(
                    "Slice elems and value elems are not the same length")

            rows_range = range(y.start, y.stop) if isinstance(
                y, slice) else range(y, y + 1)
            elms_range = range(x.start, x.stop) if isinstance(
                x, slice) else range(x, x + 1)
            rows_counter = 0
            for row in rows_range:
                elms_counter = 0
                for elm in elms_range:
                    self.__axes[row][elm] = value[rows_counter][elms_counter]
                    elms_counter += 1
                rows_counter += 1

            return

        self.__axes[y][x] = value

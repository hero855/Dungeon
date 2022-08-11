import typing

OutOfRangeValue = typing.NewType('OutOfRangeValue', None)


class Axis:
    """
    Displaces 0 index to center
    """

    def __init__(self, lst):
        self.values = lst
        self.__repr__ = lst.__repr__

    def __iter__(self):
        raise Exception("'Axis' object is not iterable, use slice")

    def __len__(self):
        length = 0
        for val in self.values:
            if val is not OutOfRangeValue:
                length += 1
        return length

    def __next__(self):
        """next(Axis)"""
        raise Exception("'Axis' object is not iterable, use slice")
        # val = self[self.values.index(next(self.values)) - self.half]
        # if val is OutOfRangeValue:
        #     raise StopIteration
        # else:
        #     return val

    def __getitem__(self, index):
        """Axis[index]"""
        offset = -self.half

        if isinstance(index, slice):
            val = self.values[index.start - self.half: index.stop - self.half: index.step]
            if OutOfRangeValue in val:
                raise IndexError(f'slice \'{repr(index)}\' is out of range')
            else:
                return val

        for i in range(len(self.values)):
            if offset == index:
                if self.values[i] is not OutOfRangeValue:
                    return self.values[i]
                else:
                    raise IndexError(f'index \'{index}\' is out of range')
            offset += 1

        raise IndexError(f'index \'{index}\' is out of range')

    def __setitem__(self, index, value):
        """Axis[index] = value"""
        offset = -self.half

        for i in range(len(self.values)):
            if offset == index:
                if self.values[i] is OutOfRangeValue:
                    raise IndexError(f'index \'{index}\' is out of range')
                else:
                    self.values[i] = value
                    return
            offset += 1

        raise IndexError(f'index \'{index}\' is out of range')

    @property
    def half(self):
        return int(len(self.values) / 2)

    def index(self, value):
        """Axis.index(value)"""

        assert len(self.values) % 2 == 1

        if value is OutOfRangeValue:
            raise ValueError(f'\'{value}\' is not in list')

        offset = -self.half

        for element in self.values:
            if element == value:
                return offset
            offset += 1

        raise ValueError(f'\'{value}\' is not in list')

    def append_right(self, value):
        """values <-- new_value"""

        assert len(self.values) % 2 == 1

        if value is OutOfRangeValue:
            raise ValueError('Cant append OutOfRangeValue to Axis')

        if self.values[-1] is OutOfRangeValue:
            self.values[-1] = value
        else:
            self.values.append(value)
        if len(self) % 2 == 0:
            self.values.insert(0, OutOfRangeValue)

    def append_left(self, value):
        """new_value --> values"""

        assert len(self.values) % 2 == 1

        if value is OutOfRangeValue:
            raise ValueError('Cant append OutOfRangeValue to Axis')

        if self.values[0] is OutOfRangeValue:
            self.values[0] = value
        else:
            self.values.insert(0, value)
        if len(self) % 2 == 0:
            self.values.append(OutOfRangeValue)

    def abs_set(self, index, value):
        """
        [-1, 0, 1].abs_set(2, val) -> [OutOfRangeValue, -1, 0, 1, val]
        [-1, 0, 1].abs_set(-2, val) -> [val, -1, 0, 1, OutOfRangeValue]
        [-1, 0, 1].abs_set(1, val) -> [-1, 0, val]
        [-1, 0, 1].abs_set(-1, val) -> [val, 0, 1]
        [-1, 0, 1].abs_set(-3, val) -> [val, OutOfRangeValue, -1, 0, 1, OutOfRangeValue, OutOfRangeValue]
        [-1, 0, 1].abs_set(0, val) -> [-1, val, 1]
        """

        if index in range(-self.half, self.half):
            self[index] = value
            return

        i = abs(index)
        half = len(self.values) / 2
        while i > half:
            self.values.append(OutOfRangeValue)
            self.values.insert(0, OutOfRangeValue)
            i -= 1

        self.values[index - self.half - 1] = value








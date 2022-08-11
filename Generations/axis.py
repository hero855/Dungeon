
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
            if val is not None:
                length += 1
        return length

    def __next__(self):
        """next(Axis)"""
        raise Exception("'Axis' object is not iterable, use slice")
        # val = self[self.values.index(next(self.values)) - self.half]
        # if val is None:
        #     raise StopIteration
        # else:
        #     return val

    def __getitem__(self, target):
        """Axis[index]"""

        if isinstance(target, slice):
            if target.start not in range(-self.half, self.half):
                self._calcUpTo(target.start)
            if target.stop not in range(-self.half, self.half):
                self._calcUpTo(target.stop)
            return self.values[
                target.start + self.half : 
                target.stop + self.half : 
                target.step
            ]

        if target not in range(-self.half, self.half):
            self._calcUpTo(target + 1)

        return self.values[target + self.half]

    def __setitem__(self, target, value):
        """Axis[index] = value"""

        if value is None:
            raise ValueError("Axis cant set None")
        
        if target not in range(-self.half, self.half):
            self._calcUpTo(target + 1)

        print(f'{self.values = }')
        print(f'{target = }')
        print(f'{self.half = }')
        print(f'{value = }')

        self.values[target + self.half] = value

    def _calcUpTo(self, target):
        target = abs(target)

        if target == 0:
            self.values[0] = None
            return

        i = self.half
        while i < target:
            curr_half = self.half
            if i > curr_half:
                self.values.insert(i + self.half, None)

            if -i < -curr_half:
                self.values.insert(0, None)
            i += 1

    @property
    def half(self):
        return int(len(self.values) / 2)

    def index(self, value):
        """Axis.index(value)"""

        assert len(self.values) % 2 == 1

        if value is None:
            raise ValueError(f'\'{value}\' is not in list')

        offset = -self.half

        for element in self.values:
            if element == value:
                return offset
            offset += 1

        raise ValueError(f'\'{value}\' is not in axis')

    def append_right(self, value):
        """values <-- new_value"""

        assert len(self.values) % 2 == 1

        if value is None:
            raise ValueError('Cant append None to Axis')

        if self.values[-1] is None:
            self.values[-1] = value
        else:
            self.values.append(value)
        if len(self) % 2 == 0:
            self.values.insert(0, None)

    def append_left(self, value):
        """new_value --> values"""

        assert len(self.values) % 2 == 1

        if value is None:
            raise ValueError('Cant append None to Axis')

        if self.values[0] is None:
            self.values[0] = value
        else:
            self.values.insert(0, value)
        if len(self) % 2 == 0:
            self.values.append(None)


if __name__ == '__main__':
    test_axis = Axis([-3, -2, -1, 0, 1, 2, 3])
    #for i in range(5):
    #    print(f'{test_axis[i] = }')
    #print(test_axis[1 : 7 : 1])
    
    test_axis[7] = 7

    print(test_axis.values)



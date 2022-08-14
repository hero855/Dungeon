class Axis:
    """Simple one dimension list with [0] index always at center
    and autofilling up to new index with Nones
    """

    def __init__(self, lst):
        self.__values = lst
        self.initSetup()
    
    def initSetup(self):
        if len(self.__values) == 0:
            self.__values.insert(0, 0)

    def __iter__(self):
        """iter(Axis)"""
        raise TypeError("'Axis' object is not iterable, use slice")

    def __next__(self):
        """next(Axis)"""
        raise TypeError("'Axis' object is not iterable, use slice")
    
    @property
    def __repr__(self):
        return self.__values.__repr__

    def __getitem__(self, target):
        """Axis[index]"""

        if not isinstance(target, (int, slice)):
            raise TypeError(f"'{type(self).__name__}' indices must be integers or slices, not {type(target).__name__}")

        if isinstance(target, slice):
            if target.start not in range(-self.half - 1, self.half + 1):
                self._calcUpTo(target.start)
            if target.stop not in range(-self.half - 1, self.half + 1):
                self._calcUpTo(target.stop)
            return self.__values[
                target.start + self.half : 
                target.stop + self.half : 
                target.step
            ]
        
        if target not in range(-self.half, self.half):
            d = -1 if target < 0 else 1
            self._calcUpTo(target + d)

        return self.__values[target + self.half]

    def __setitem__(self, target, value):
        """Axis[index] = value"""

        if not isinstance(target, (int, slice)):
            raise TypeError(f"'{type(self).__name__}' indices must be integers or slices, not {type(target).__name__}")

        if value is None:
            raise ValueError("Axis cant set None")
        
        if isinstance(target, int):
            if target not in range(-self.half, self.half):
                self._calcUpTo(target + -1 if target < 0 else 1)

            self.__values[target + self.half] = value
        
        if isinstance(target, slice):
            slice_length = target.stop - target.start
            if slice_length != len(value):
                raise ValueError(f"Length of slice ({slice_length}) and length of value ({len(value)}) not match")
            if target.start not in range(-self.half - 1,  self.half + 1):
                self._calcUpTo(target.start)
            if target.stop not in range(-self.half - 1, self.half + 1):
                self._calcUpTo(target.stop)
            for idx in range(target.start, target.stop):
                self.__values[idx + self.half] = value[idx + self.half]
                

    def _calcUpTo(self, target):
        target = abs(target)

        if target == 0:
            self.__values[0] = None
            return

        i = self.half
        while i < target:
            curr_half = self.half
            if i > curr_half:
                self.__values.insert(i + self.half, None)

            if -i < -curr_half:
                self.__values.insert(0, None)
            i += 1

    @property
    def half(self):
        return int(len(self.__values) / 2)

    def index(self, value):
        """Axis.index(value)"""

        assert len(self.__values) % 2 == 1

        if value is None:
            raise ValueError(f'\'{value}\' is not in list')

        offset = -self.half

        for element in self.__values:
            if id(element) is id(value):
                return offset
            offset += 1

        raise ValueError(f'\'{value}\' is not in axis')

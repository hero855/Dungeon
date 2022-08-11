import unittest

from Generations.chank import Chank
from Generations.area import Area


class ChankTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.area = Area('Test')
        self.chank = self.area.chank_map

    # TODO: tests
    def test_generation(self):
        pass


if __name__ == '__main__':
    unittest.main()

import unittest

from Generations.area import Area
from Generations.vector import Vector3
from base.container import Container


class AreaTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.area = Area('Test')

    def test_generation(self):
        self.area.initial_update()
        # self.assertIsInstance(self.area.map[0, 0, 0], Container)
    
    def test_rendering(self):
        # self.area.show(Vector3(0, 0, 0))
        pass


if __name__ == '__main__':
    unittest.main()

import unittest
import sys

sys.path.append('C:/code/Dungeon')

from Generations.vector import Vector2, Vector3


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.v2_1 = Vector2(1, 2)
        self.v2_2 = Vector2(3, 4)
        self.v3_1 = Vector3(1, 2, 3)
        self.v3_2 = Vector3(4, 5, 6)

    def test_operations(self):

        #v2_3 = self.v2_1 + self.v2_2
        #v2_4 = self.v2_1 * self.v2_2

        v3_3 = self.v3_1 + self.v3_2
        v3_4 = self.v3_1 * 3
        v3_5 = self.v3_1 ^ self.v3_2
        v3_6 = self.v3_1.cross(self.v3_2)

        self.assertEqual(v3_3, Vector3(5, 7, 9))
        self.assertEqual(v3_4, Vector3(3, 6, 9))
        self.assertEqual(v3_5, Vector3(-3, 6, -3))
        self.assertEqual(v3_6, Vector3(-3, 6, -3))

    def test_unpack(self):
        with self.assertRaises(AttributeError):
            x, y = self.v2_1


if __name__ == '__main__':
    unittest.main()

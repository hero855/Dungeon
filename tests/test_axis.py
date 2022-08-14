import unittest

from Generations.axis import Axis


class AxisTestCase(unittest.TestCase):
    def setUp(self):
        self.a1 = Axis([n for n in range(5)])  # [0, 1, 2, 3, 4]
        self.a2 = Axis([n for n in range(-2, 3)])  # [-2, -1, 0, 1, 2]

    def test_get_item(self):
        self.assertEqual(self.a1[2], 4)
        self.assertEqual(self.a1[0], 2)
        self.assertEqual(self.a1[-2], 0)

        self.assertEqual(self.a2[2], 2)
        self.assertEqual(self.a2[0], 0)
        self.assertEqual(self.a2[-2], -2)

    def test_set_item(self):
        self.a2[0] = 1
        self.assertEqual(self.a2[0], 1)
        self.a2[0] = 0
        self.a2[-3] = -3
        self.a2[3] = 3
        self.assertEqual(self.a2[-3], -3)
        self.assertEqual(self.a2[3], 3)
        self.a2[-5] = -5
        self.assertEqual(self.a2[-5], -5)
        with self.assertRaises(ValueError):
            self.a1.__setitem__(0, None)

    def test_iteration(self):
        with self.assertRaises(TypeError):
            iter(self.a1)
        with self.assertRaises(TypeError):
            next(self.a1)
    
    def test_get_slicing(self):
        self.a2[-3] = -3
        self.a2[3] = 3
        self.assertEqual(self.a2[-3: 4], list(range(-3, 4)))
    
    def test_set_slicing(self):
        self.a2[-3: 4] = list(range(-3, 4))
        self.assertEqual(self.a2[-3: 4], list(range(-3, 4)))


if __name__ == '__main__':
    unittest.main()

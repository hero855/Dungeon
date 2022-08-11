import unittest

from Generations.axis import Axis


class AxisTestCase(unittest.TestCase):
    def setUp(self):
        self.a1 = Axis([n for n in range(5)])  # [0, 1, 2, 3, 4]
        self.a2 = Axis([n for n in range(-2, 3)])  # [-2, -1, 0, 1, 2]

    def test_getitem(self):
        self.assertEqual(self.a1[2], 4)
        self.assertEqual(self.a1[0], 2)
        self.assertEqual(self.a1[-2], 0)
        with self.assertRaises(IndexError):
            self.a1.__getitem__(-3)  # instead a[n] bc required callable
            self.a1.__getitem__(3)

        self.assertEqual(self.a2[2], 2)
        self.assertEqual(self.a2[0], 0)
        self.assertEqual(self.a2[-2], -2)
        with self.assertRaises(IndexError):
            self.a2.__getitem__(3)
            self.a2.__getitem__(-3)

    def test_setitem(self):
        self.a2[0] = 1
        self.assertEqual(self.a2[0], 1)
        self.a2[0] = 0
        self.a2[-3] = -3
        self.a2[3] = 3
        self.assertEqual(self.a2.values, list(range(-3, 4)))
        self.a2[-5] = -5
        self.assertEqual(self.a2[-5], -5)
        with self.assertRaises(IndexError):
            self.a2.__getitem__(-4)
            self.a2.__getitem__(4)
            self.a2.__getitem__(5)

    def test_iteration(self):
        i = -2
        counter = 0
        for _ in range(len(self.a1)):
            self.assertEqual(self.a1[i], counter)
            i += 1
            counter += 1

        counter = 0
        for number in self.a1.values:
            self.assertEqual(number, counter)
            counter += 1

    def test_appending(self):
        self.a1.append_right(5)
        self.assertEqual(self.a1[3], 5)
        self.a1.append_left(-1)
        self.assertEqual(self.a1[-3], -1)
        self.assertEqual(self.a1.values, list(range(-1, 6)))
        with self.assertRaises(ValueError):
            self.a1.append_left(None)
            self.a1.append_right(None)


if __name__ == '__main__':
    unittest.main()

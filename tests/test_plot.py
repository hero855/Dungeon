from pprint import pprint
import unittest

from Generations.plot_2d import Plot2D
from Generations.plot_3d import Plot3D
from Generations.vector import Vector3


class PlotTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.plot2d = Plot2D()
        self.plot3d = Plot3D()

    # TODO: check error if value lengths are not the same (__getitem__ and __setitem__)
    # TODO: check error if slice and value lengths are not the same (__getitem__ and __setitem__)

    def test_setitem(self):
        self.plot2d[0, 0] = 42
        self.assertEqual(self.plot2d[0, 0], 42)
        self.plot2d[0, 1] = 3284729

    def test_set_slice(self):
        self.plot2d[-1: 2, -1: 2] = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        self.plot3d[-1: 2, -1: 2, -1: 2] = [
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ], [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ], [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
        ]

    def test_get_slice(self):
        self.plot2d[-1: 2, -1: 2] = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(
            self.plot2d[-1: 2, -1: 2],
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
        )

        self.plot3d[-1: 2, -1: 2, -1: 2] = [
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ], [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ], [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
        ]

        self.assertEqual(
            self.plot3d[-1: 2, -1: 2, -1: 2],
            [
                [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ], [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ], [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ]
            ]
        )


if __name__ == '__main__':
    unittest.main()

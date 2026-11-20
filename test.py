import unittest
from rectangle import area, perimetr


class RectangleTestCase(unittest.TestCase):

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_square(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_rectangle(self):
        self.assertEqual(area(3, 5), 15)

    def test_area_float(self):
        self.assertEqual(area(2.5, 2), 5)

    def test_perimetr_zero(self):
        self.assertEqual(perimetr(0, 0), 0)

    def test_perimetr_square(self):
        self.assertEqual(perimetr(10, 10), 40)

    def test_perimetr_rectangle(self):
        self.assertEqual(perimetr(3, 5), 16)


if __name__ == "__main__":
    unittest.main()
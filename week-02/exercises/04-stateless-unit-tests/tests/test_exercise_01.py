import unittest

from package.exercise_01 import add, subtract, multiply, divide


class TestExercise01(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2, add(1, 1))
        self.assertEqual(0, add(112, -112))
        self.assertEqual(-256, add(-206, -50))
        self.assertEqual(256, add(150, 106))
        self.assertEqual(17, add(10, 7))
        self.assertEqual(-5, add(300, -305))

    def test_subtract(self):
        self.assertEqual(0, subtract(10, 10))
        self.assertEqual(5, subtract(10, 5))
        self.assertEqual(-15, subtract(10, 25))
        self.assertEqual(100000, subtract(100001, 1))
        self.assertEqual(-200, subtract(50, 250))
        self.assertEqual(13, subtract(40, 27))

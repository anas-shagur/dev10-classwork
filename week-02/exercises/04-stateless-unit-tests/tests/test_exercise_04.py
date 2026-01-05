import unittest


from package.exercise_04 import Exercise04


class TestExercise04(unittest.TestCase):
    def test_calculate_total_cost(self):
        inst = Exercise04()
        # floats are notoriously hard to test because they use floating-point rounding.
        # The third argument in `assertAlmostEqual` is a delta.
        # It represents the margin of error for equality.
        # As long as the expected and actual differ by less than the delta, the test passes.
        self.assertAlmostEqual(1.25, inst.calculate_total_cost(0.25, 5), delta=0.001)
        self.assertAlmostEqual(99.06, inst.calculate_total_cost(1.27, 100), delta=0.001)

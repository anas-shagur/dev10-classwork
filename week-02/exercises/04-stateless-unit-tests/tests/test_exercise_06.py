import unittest

from package.exercise_06 import Exercise06


class TestExercise06(unittest.TestCase):
    instance = Exercise06()

    # Suggested test additions:
    # shouldBeNullForNullArg
    # shouldCapitalizeMultipleElements (several scenarios)
    # shouldIgnoreNullElements
    # shouldIgnoreEmptyElements

    def test_shouldCapitalizeOneElement(self):
        values = ["lower"]
        expected = ["Lower"]
        actual = self.instance.capitalize_all(values)
        self.assertEqual(expected, actual)

    def test_shouldBeEmptyForEmptyArg(self):
        self.assertEqual([], self.instance.capitalize_all([]))

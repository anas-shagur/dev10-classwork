import unittest

from package.exercise_02 import surround_with_tag


class TestExercise02(unittest.TestCase):
    def test_surround_with_tag(self):
        self.assertEqual("<b>a</b>", surround_with_tag("a", "b"))
        self.assertEqual("splendid", surround_with_tag("splendid", None))

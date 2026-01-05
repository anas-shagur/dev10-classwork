import unittest

from package.ocean import Submarine


class TestSubmarine(unittest.TestCase):
    def setUp(self):
        self.submarine = Submarine(100.0)

    def test_shouldHaveCorrectDepthAfter3Dives(self):
        self.submarine.dive()
        self.submarine.dive()
        self.submarine.dive()
        self.assertAlmostEqual(9.0, self.submarine.depth_in_meters, delta=0.001)

    def test_shouldHaveCorrectPressureAfter3Dives(self):
        self.submarine.dive()
        self.submarine.dive()
        self.submarine.dive()
        # 1.0 at sea level, 0.9 for 9 meters
        self.assertAlmostEqual(1.9, self.submarine.pressure_in_atmospheres, delta=0.001)

    # 1. Create one or more tests to confirm `dive` is working properly.
    # 2. Create a test to assert the submarine can't go deeper than the max depth.
    # (Be sure to use more than one max depth.)
    # 3. Create one or more tests to confirm `surface` is working properly.
    # 4. Create a test to assert the submarine can't go above sea level.
    # (Depth can never be negative.)
    # 5. Create one or more tests to confirm `pressure_in_atmospheres` is working properly.

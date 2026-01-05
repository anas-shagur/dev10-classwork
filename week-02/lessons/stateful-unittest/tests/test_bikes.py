import unittest

from package.bikes import Cyclist, Bicycle


class TestCyclist(unittest.TestCase):
    def test_shouldMakeSmallInvalidPowerTheMin(self):
        actual = Cyclist("Test Cyclist", 0.111)
        self.assertAlmostEqual(1.0, actual.power, delta=0.01)

        actual = Cyclist("Test Cyclist", -10000.0)
        self.assertAlmostEqual(1.0, actual.power, delta=0.01)

    def test_shouldMakeLargeInvalidPowerTheMax(self):
        actual = Cyclist("Test Cyclist", 55.5)
        self.assertAlmostEqual(10.0, actual.power, delta=0.01)

        actual = Cyclist("Test Cyclist", 999999999)
        self.assertAlmostEqual(10.0, actual.power, delta=0.01)

    def test_shouldAllowValidPower(self):
        actual = Cyclist("Test Cyclist", 5.55)
        self.assertAlmostEqual(5.55, actual.power, delta=0.01)

        actual = Cyclist("Test Cyclist", 9.87)
        self.assertAlmostEqual(9.87, actual.power, delta=0.01)

        actual = Cyclist("Test Cyclist", 2.12)
        self.assertAlmostEqual(2.12, actual.power, delta=0.01)

    def test_shouldGetName(self):
        actual = Cyclist("Test Cyclist", 5.55)
        self.assertEqual("Test Cyclist", actual.name)

        actual = Cyclist(None, 5.55)
        # nulls are allowed.
        self.assertIsNone(actual.name)

        actual = Cyclist("", 5.55)
        # No restrictions on empty strings
        self.assertEqual("", actual.name)


class TestBicycle(unittest.TestCase):
    def setUp(self):
        highPowerCyclist = Cyclist("High Power Cyclist", 9.87)
        self.highPowerBike = Bicycle(highPowerCyclist)

        mediumPowerCyclist = Cyclist("Medium Power Cyclist", 4.9)
        self.mediumPowerBike = Bicycle(mediumPowerCyclist)

        lowPowerCyclist = Cyclist("Low Power Cyclist", 1.54)
        self.lowPowerBike = Bicycle(lowPowerCyclist)

    def test_shouldAccelerate(self):
        self.highPowerBike.accelerate()
        self.assertAlmostEqual(8.55, self.highPowerBike.velocity, delta=0.01)

        self.mediumPowerBike.accelerate()
        self.assertAlmostEqual(6.56, self.mediumPowerBike.velocity, delta=0.01)

        self.lowPowerBike.accelerate()
        self.assertAlmostEqual(5.22, self.lowPowerBike.velocity, delta=0.01)

    def test_shouldBrake(self):
        # accelerate twice (arrange)
        for _ in range(2):
            self.highPowerBike.accelerate()
            self.mediumPowerBike.accelerate()
            self.lowPowerBike.accelerate()

        # brake (act)
        self.highPowerBike.brake()
        self.mediumPowerBike.brake()
        self.lowPowerBike.brake()

        # (assert)
        self.assertAlmostEqual(7.096, self.highPowerBike.velocity, delta=0.01)
        self.assertAlmostEqual(3.12, self.mediumPowerBike.velocity, delta=0.01)
        self.assertAlmostEqual(0.432, self.lowPowerBike.velocity, delta=0.01)

    def test_shouldNotExceedMaxVelocity(self):
        # accelerate 1000 times
        for _ in range(1000):
            self.highPowerBike.accelerate()
            self.mediumPowerBike.accelerate()
            self.lowPowerBike.accelerate()

        self.assertEqual(Bicycle.MAX_VELOCITY, self.highPowerBike.velocity)
        self.assertEqual(Bicycle.MAX_VELOCITY, self.mediumPowerBike.velocity)
        self.assertEqual(Bicycle.MAX_VELOCITY, self.lowPowerBike.velocity)

    def test_shouldNotReachNegativeVelocity(self):
        # brake 1000 times
        for _ in range(1000):
            self.highPowerBike.brake()
            self.mediumPowerBike.brake()
            self.lowPowerBike.brake()

        self.assertEqual(0.0, self.highPowerBike.velocity)
        self.assertEqual(0.0, self.mediumPowerBike.velocity)
        self.assertEqual(0.0, self.lowPowerBike.velocity)

    def test_shouldCreateAnonymousCyclist(self):
        # independent arrangement and act
        bike = Bicycle(None)

        # assert
        self.assertIsNotNone(bike.cyclist)
        self.assertEqual("Anonymous", bike.cyclist.name)
        self.assertEqual(Cyclist.MIN_POWER, bike.cyclist.power)

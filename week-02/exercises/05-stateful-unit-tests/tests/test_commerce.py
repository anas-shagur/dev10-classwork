import unittest

from package.commerce import Order, LineItem


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order = Order(25)

    def test_shouldHaveOrderId(self):
        self.assertEqual(25, self.order.order_id)

    def test_shouldAddValidItems(self):
        grassSeed = LineItem("Grass Seed", 19.99, 2)
        result = self.order.add(grassSeed)
        self.assertTrue(result)
        self.assertEqual(1, len(self.order.items))
        self.assertEqual(grassSeed, self.order.items[0])

        gardenRake = LineItem("Garden Rake", 44.99, 1)
        result = self.order.add(gardenRake)
        self.assertTrue(result)
        self.assertEqual(2, len(self.order.items))
        self.assertEqual(gardenRake, self.order.items[1])

        hose = LineItem("Garden Hose - 50ft", 38.49, 1)
        result = self.order.add(hose)
        self.assertTrue(result)
        self.assertEqual(3, len(self.order.items))
        self.assertEqual(hose, self.order.items[2])

    # 1. Add test_shouldNotAddInvalidItems:
    #    confirm that it's not possible to add items with <= 0 quantity or < 0 price.
    # 2. Test the order.total in various scenarios and confirm it's correct.
    # 3. If you tackle `order.remove`, test the method thoroughly.

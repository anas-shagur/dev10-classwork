import unittest


from package.chess import Queen


class TestQueen(unittest.TestCase):
    def setUp(self):
        self.queen = Queen()

    def test_shouldMoveToFourCorners(self):
        self.assertTrue(self.queen.move(7, 0))  # top left;
        self.assertEqual(7, self.queen.row)
        self.assertEqual(0, self.queen.column)

        self.assertTrue(self.queen.move(7, 7))  # top right;
        self.assertEqual(7, self.queen.row)
        self.assertEqual(7, self.queen.column)

        self.assertTrue(self.queen.move(0, 7))  # bottom right;
        self.assertEqual(0, self.queen.row)
        self.assertEqual(7, self.queen.column)

        self.assertTrue(self.queen.move(0, 0))  # bottom left;
        self.assertEqual(0, self.queen.row)
        self.assertEqual(0, self.queen.column)

        # 1. Add tests to validate Queen movement.
        # Required tests:
        # - anything off the board is invalid, should return False and leave attributes alone.
        # - moving to the current location should return False and leave attributes alone.
        # - should still be able to move after an invalid move.
        # - can move diagonally in various ways
        # Always confirm that attributes have been properly updated.

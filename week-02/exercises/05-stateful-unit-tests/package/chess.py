class Queen:
    """
    The most powerful chess piece.
    Moves horizontally, vertically, or diagonally as many spaces as she wants.
    She tracks her current position with two integer fields: row and column.
    Rows and columns are zero-based.
    The queen starts at row 0 and column 0, though there is no board.
    Row 7 - - - - - - - -
    Row 6 - - - - - - - -
    Row 5 - - - - - - - -
    Row 4 - - - - - - - -
    Row 3 - - - - - - - -
    Row 2 - - - - - - - -
    Row 1 - - - - - - - -
    Row 0 Q - - - - - - -
    Cols: 0 1 2 3 4 5 6 7

    See: https://en.wikipedia.org/wiki/Queen_(chess)
    """

    def __init__(self):
        self._row = 0
        self._column = 0

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column

    def move(self, row, column):
        """
        Requests a move to a new row and column.
        Args:
            row (int): the requested row
            column (int): the requested column
        Returns:
            bool: True if the move is valid, False if it's not
        """

        # 1. Implement the move method.
        # If the move is valid, return True and update `row` and `column` attributes.
        # If the move is invalid, return False and do not update attributes.
        # Rules for valid moves:
        # - row and column can never be less than 0 or greater than 7 (8 rows and columns on a chess board).
        # - can't equal the existing row and column (same location)
        # - If the row parameter and attribute are the same but the column is not, the queen is moving horizontally. That's valid.
        # - If the column parameter and attribute are the same but the row is not, the queen is moving vertically. That's valid.
        # - Otherwise, the absolute difference between row parameter and attribute
        #   and the absolute difference between the column parameter and attribute must be the same.
        #   That represents a diagonal move. That's valid.

        return False

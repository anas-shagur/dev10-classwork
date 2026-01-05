# 1. Read the is_within_five_of_a_hundred docstring.
# 2. Implement is_within_five_of_a_hundred.
# 3. Create tests for is_within_five_of_a_hundred and confirm that it is correct.


class Exercise05:
    def is_within_five_of_a_hundred(self, value):
        """
        Determines if a value is within 5 of any number evenly divisible by 100.
        Examples
        -105 to -95: True
        -94 to -6: False
        -5 to 5: True
        6 to 94: False
        95 to 105: True
        106 to 194: False
        195 to 205: True
        206 to 294: False
        ...continues in both the positive and negative directions...

        Args:
            value (int): the number to test
        Returns:
            bool: True if value is within 5 of a number evenly divisible by 100, False if not.
        """
        return False

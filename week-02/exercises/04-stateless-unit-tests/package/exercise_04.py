#  TESTING AN INSTANCE
#  (testing a method)
#  1. Read the calculate_total_cost docstring.
#  2. Review test_exercise_04.TestExercise04.
#  3. Implement calculate_total_cost.
#  4. Tests are incomplete. Complete them to verify all scenarios.


class Exercise04:
    def calculate_total_cost(self, price, quantity):
        """
        Calculates the cost to the customer give an item price and the quantity purchased.
        Negative price or quantity results in 0.0 cost.
        Volume discounts apply.
        1 - 15 items: no discount
        16 - 25 items: 5% discount
        26 - 50 items: 10% discount
        51 - 75 items: 15% discount
        Greater than 75 items: 22% discount

        Args:
            price (float): the price of a single item
            quantity (int): the number of items to purchase
        Returns:
            float: the total cost with volume discounts applied
        """
        return 0.0

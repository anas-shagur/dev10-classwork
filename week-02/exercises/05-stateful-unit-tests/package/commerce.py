from dataclasses import dataclass, field


@dataclass
class LineItem:
    """
    A product or service that's part of an Order.
    Could represent anything with a price and quantity.
    Examples:
    LineItem("Grass Seed", 25.49, 1)
    LineItem("Double Scoop Cone - Rocky Road", 5.45, 2)
    LineItem("Technician Service (hours)", 56.75, 8.50)
    LineItem("Movie Rental - The Muppet Movie", 1.99, 1)
    """

    item_name: str
    price: float
    quantity: float

    @property
    def total(self):
        return self.price * self.quantity


@dataclass
class Order:
    """
    An informal sale contract for purchasable products and services.
    Products and services are modeled as LineItems.
    They're added to the order one at a time with the `add` method.
    """

    order_id: int
    line_items: list[LineItem] = field(default_factory=list)

    @property
    def items(self):
        return self.line_items

    @property
    def total(self):
        # 1. Complete the total property.
        # It should calculate the order's grand total by summing totals from each LineItem.
        return 0.0

    def add(self, item: LineItem):
        if item is None or item.quantity <= 0 or item.price < 0.0:
            return False

        self.line_items.append(item)
        return True

    # 2. Stretch goal: add a remove method that removes a LineItem by either index or reference.

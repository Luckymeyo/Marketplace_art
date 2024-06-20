
class Price:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

class Dimensions:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
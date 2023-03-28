class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if self.quantity + milliliters <= self.size:
            result = self.quantity = self.quantity + milliliters
            return result

    def status(self):
        result = self.size - self.quantity
        return result


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())

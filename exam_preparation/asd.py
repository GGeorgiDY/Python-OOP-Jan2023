class ShoppingCart:
    def __init__(self, shop_name: str, budget: float):
        self.shop_name = shop_name
        self.budget = budget
        self.products = {}

    def __add__(self, other):  # other is another ShoppingCart instance
        new_shop_name = f"{self.shop_name}{other.shop_name}"
        new_budget = self.budget + other.budget
        new_shopping_cart = ShoppingCart(new_shop_name, new_budget)
        new_shopping_cart.products.update(**self.products)
        new_shopping_cart.products.update(**other.products)
        return new_shopping_cart


cart1 = ShoppingCart('metro', 1000)
cart2 = ShoppingCart('Lidl', 1000)
cart1.products = {'bananas': 100}
cart2.products = {'apples': 100}
print(cart1.__add__(cart2))
# print(new_shopping_cart.new_shop_name)

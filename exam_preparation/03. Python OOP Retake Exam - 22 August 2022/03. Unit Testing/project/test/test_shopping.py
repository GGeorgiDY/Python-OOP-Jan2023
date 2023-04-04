from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class ShoppingCartTests(TestCase):

    def setUp(self):
        self.cart1 = ShoppingCart('Metro', 1000)
        # self.cart2 = ShoppingCart('Lidl', 1000)

    def test_initialization(self):
        self.assertEqual('Metro', self.cart1.shop_name)
        self.assertEqual(1000, self.cart1.budget)
        self.assertEqual({}, self.cart1.products)

    def test_shop_name_validation_starting_with_capital_letter(self):
        with self.assertRaises(ValueError) as ve:
            self.cart1 = ShoppingCart('metro', 1000)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_shop_name_validation_contain_only_letters(self):
        with self.assertRaises(ValueError) as ve:
            self.cart1 = ShoppingCart('Metro1', 1000)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_product_cost_too_much(self):
        with self.assertRaises(ValueError) as ve:
            self.cart1.add_to_cart('apples', 100)
        self.assertEqual("Product apples cost too much!", str(ve.exception))

    def test_product_successfully_added_to_cart(self):
        self.cart1.add_to_cart('apples', 90)
        self.assertEqual({'apples': 90}, self.cart1.products)

    def test_product_successfully_added_to_cart_return(self):
        result = self.cart1.add_to_cart('apples', 90)
        self.assertEqual("apples product was successfully added to the cart!", result)

    def test_unable_removing_product(self):
        with self.assertRaises(ValueError) as ve:
            self.cart1.remove_from_cart('apples')
        self.assertEqual("No product with name apples in the cart!", str(ve.exception))

    def test_successfully_removing_product(self):
        self.cart1.products = {'apples': 100}
        self.cart1.remove_from_cart('apples')
        self.assertEqual({}, self.cart1.products)

    def test_successfully_removing_product_return(self):
        self.cart1.products = {'apples': 100}
        result = self.cart1.remove_from_cart('apples')
        self.assertEqual("Product apples was successfully removed from the cart!", result)

    def test_new_shop_name(self):
        cart2 = ShoppingCart('Lidl', 1000)
        result = self.cart1.__add__(cart2)
        self.assertEqual('MetroLidl', result.shop_name)

    def test_new_budget(self):
        cart2 = ShoppingCart('Lidl', 1000)
        result = self.cart1.__add__(cart2)
        self.assertEqual(2000, result.budget)

    def test_new_products2(self):
        cart1 = ShoppingCart('Metro', 1000)
        cart2 = ShoppingCart('Lidl', 1000)
        cart1.products = {'apples': 50}
        cart2.products = {'bananas': 50}
        self.assertEqual({'apples': 50, 'bananas': 50}, cart1.__add__(cart2).products)

    def test_new_products_return(self):
        cart1 = ShoppingCart('Metro', 1000)
        cart2 = ShoppingCart('Lidl', 1000)
        cart1.products = {'apples': 50}
        cart2.products = {'bananas': 50}
        self.assertEqual('ShoppingCart', cart1.__add__(cart2).__class__.__name__)

    def test_buy_products_ve(self):
        self.cart1.products = {'bananas': 1001}
        with self.assertRaises(ValueError) as ve:
            self.cart1.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 1.00lv!", str(ve.exception))

    def test_buy_products_successfully(self):
        self.cart1.products = {'bananas': 700}
        result = self.cart1.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 700.00lv.', result)


if __name__ == "__main__":
    main()
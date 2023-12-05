import unittest
from shopping_cart import ShoppingCart
from product import Product

class TestShoppingCart(unittest.TestCase):
    def test_add_item(self):
        cart = ShoppingCart()
        product = Product(name='Sample Product', price=20.0)
        cart.add_item(product, quantity=2)
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]['quantity'], 2)

    def test_calculate_total(self):
        cart = ShoppingCart()
        product1 = Product(name='Product 1', price=10.0)
        product2 = Product(name='Product 2', price=15.0)
        cart.add_item(product1, quantity=3)
        cart.add_item(product2, quantity=2)
        total = cart.calculate_total()
        self.assertEqual(total, 60.0)

if __name__ == '__main__':
    unittest.main()

import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        print("* setUp() - Tworzenie nowego koszyka")
        self.cart = ShoppingCart()

    def test_add_product(self):
        print("* test_add_product() - Dodawanie produktu")
        self.assertTrue(self.cart.add_product("Apple", 5, 2))
        self.assertIn("Apple", self.cart.get_products())

    def test_remove_product(self):
        print("* test_remove_product() - Usuwanie produktu")
        self.cart.add_product("Banana", 3, 1)
        self.assertTrue(self.cart.remove_product("Banana"))
        self.assertNotIn("Banana", self.cart.get_products())

    def test_update_quantity(self):
        print("* test_update_quantity() - Aktualizacja ilości")
        self.cart.add_product("Orange", 4, 2)
        self.assertTrue(self.cart.update_quantity("Orange", 5))
        self.assertEqual(self.cart.count_products(), 5)

    def test_get_total_price(self):
        print("* test_get_total_price() - Obliczanie sumy cen")
        self.cart.add_product("Grapes", 10, 3)
        self.assertEqual(self.cart.get_total_price(), 30)

    def test_apply_discount_code(self):
        print("* test_apply_discount_code() - Zastosowanie rabatu")
        self.cart.add_product("Watermelon", 20, 2)
        self.assertTrue(self.cart.apply_discount_code("SAVE10"))
        self.assertEqual(self.cart.get_total_price(), 36)

    def test_checkout(self):
        print("* test_checkout() - Finalizacja zamówienia")
        self.cart.add_product("Mango", 15, 1)
        self.assertTrue(self.cart.checkout())
        self.assertEqual(self.cart.count_products(), 0)

if __name__ == "__main__":
    unittest.main()
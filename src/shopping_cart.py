class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.discount = 0

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        if product_name and price > 0 and quantity > 0:
            if product_name in self.products:
                self.products[product_name]['quantity'] += quantity
            else:
                self.products[product_name] = {'price': price, 'quantity': quantity}
            return True
        return False

    def remove_product(self, product_name: str) -> bool:
        if product_name in self.products:
            del self.products[product_name]
            return True
        return False

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        if product_name in self.products and new_quantity > 0:
            self.products[product_name]['quantity'] = new_quantity
            return True
        return False

    def get_products(self):
        return list(self.products.keys())

    def count_products(self) -> int:
        return sum(item['quantity'] for item in self.products.values())

    def get_total_price(self) -> int:
        total = sum(item['price'] * item['quantity'] for item in self.products.values())
        return total - (total * self.discount // 100)

    def apply_discount_code(self, discount_code: str) -> bool:
        valid_codes = {"SAVE10": 10, "SAVE20": 20}
        if discount_code in valid_codes:
            self.discount = valid_codes[discount_code]
            return True
        return False

    def checkout(self) -> bool:
        if self.products:
            self.products.clear()
            self.discount = 0
            return True
        return False
class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer


class OrderValidator:
    def _validate_order(self):
        print("Walidacja zamowienia.", order.id)


class OrderRepository:
    def _save_order_to_database(self):
        print("Zapisywanie zamowienia do bazy danych.", order.id)


class EmailService:
    def _send_confirmation_email(self):
        print(f"Wysylanie e-maila potwierdzajacego {order.customer}.")


class OrderProcessor (OrderValidator,OrderRepository, EmailService):
    def __init__(self, order):
        self.order = order

    def process_order(self):
        self._validate_order()
        self._save_order_to_database()
        self._send_confirmation_email()


# Użycie
order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
processor = OrderProcessor(order)
processor.process_order()
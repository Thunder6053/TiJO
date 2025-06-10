from unittest.mock import Mock
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from my_counter import Counter,Operation


class CounterTestCase(unittest.TestCase):

    def test_count_characters_mock_return_value(self):
        """Sprawdza, czy metoda count zwraca poprawną wartość dla danego argumentu."""
        mock_operation = Mock(spec=Operation)
        mock_operation.count.return_value = 5  # Ustawiamy zwracana wartosc

        counter = Counter(mock_operation)
        result = counter.count_characters("Hello")  # Wywolujemy metode

        self.assertEqual(result, 5)  # Powinno zwrocic wartosc z mocka
        mock_operation.count.assert_called_once_with("Hello")  # Sprawdzamy, czy funkcja zostala wywolana raz z "Hello"

    def test_count_characters_mock_call_count_one(self):
        """Sprawdza, czy metoda count() zostala wywołana dokładnie 1 raz."""
        mock_operation = Mock(spec=Operation)
        counter = Counter(mock_operation)

        counter.count_characters("Hello")

        self.assertEqual(mock_operation.count.call_count, 1)  # Powinno byc wywołane 1 raz
        mock_operation.count.assert_called_with("Hello")  # Sprawdzamy, czy uzyto poprawnego argumentu

    def test_count_characters_mock_call_count_multiple(self):
        """Sprawdza, czy metoda count() została wywołana wielokrotnie."""
        mock_operation = Mock(spec=Operation)
        counter = Counter(mock_operation)

        counter.count_characters("Hello")
        counter.count_characters("World")
        counter.count_characters("Test")

        self.assertEqual(mock_operation.count.call_count, 3)  # Sprawdzamy, czy metoda byla wywolana 3 razy
        mock_operation.count.assert_any_call("Hello")  # Sprawdzamy, czy wywolano z "Hello"
        mock_operation.count.assert_any_call("World")  # Sprawdzamy, czy wywolano z "World"
        mock_operation.count.assert_any_call("Test")  # Sprawdzamy, czy wywolano z "Test"

if __name__ == '__main__':
    unittest.main()

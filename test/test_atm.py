import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from atm import ATM, InvalidPinException, InsufficientFundsException


class TestATM(unittest.TestCase):
    def setUp(self):
        self.atm = ATM(pin=1234, initial_balance=100.0)

    def test_check_balance_valid_pin(self):
        balance = self.atm.check_balance(1234)
        print("Saldo konta: ", balance)
        self.assertEqual(balance, 100.0)

    def test_check_balance_invalid_pin(self):
        with self.assertRaises(InvalidPinException):
            print("Błędny PIN przy sprawdzaniu salda")
            self.atm.check_balance(9999)

    def test_deposit_valid_pin(self):
        new_balance = self.atm.deposit(1234, 50.0)
        print("Nowe saldo po wpłacie: ", new_balance)
        self.assertEqual(new_balance, 150.0)

    def test_deposit_invalid_pin(self):
        with self.assertRaises(InvalidPinException):
            print("Błędny PIN przy wpłacie")
            self.atm.deposit(9999, 50.0)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            print("Próba wpłaty ujemnej kwoty")
            self.atm.deposit(1234, -10.0)

    def test_withdraw_valid_amount(self):
        new_balance = self.atm.withdraw(1234, 50.0)
        print("Nowe saldo po wypłacie: ", new_balance)
        self.assertEqual(new_balance, 50.0)

    def test_withdraw_invalid_pin(self):
        with self.assertRaises(InvalidPinException):
            print("Błędny PIN przy wypłacie")
            self.atm.withdraw(9999, 50.0)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsException):
            print("Próba wypłaty większej kwoty niż saldo")
            self.atm.withdraw(1234, 200.0)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            print("Próba wypłaty ujemnej kwoty")
            self.atm.withdraw(1234, -10.0)


if __name__ == '__main__':
    unittest.main()
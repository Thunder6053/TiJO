class InvalidPinException(Exception):
    """Gdy podany PIN jest nieprawidłowy"""
    pass
class InsufficientFundsException(Exception):
    """Gdy saldo jest niewystarczające"""
    pass
class ATM:
    """
    Klasa reprezentująca bankomat (ATM) z podstawowymi operacjami bankowymi.
    """

    def __init__(self, pin: int, initial_balance: float = 0.0):
        self.pin = pin
        self.balance = initial_balance

    def check_balance(self, pin: int) -> float:
        """
        Sprawdza saldo konta użytkownika.

        :param pin: PIN użytkownika.
        :return: Saldo konta użytkownika.
        :raises InvalidPinException: Jeśli podany PIN jest nieprawidłowy.
        """

        if pin != self.pin:
            raise InvalidPinException("Nieprawidłowy PIN")
        return self.balance

    def deposit(self, pin: int, amount: float) -> float:
        """
        Wpłaca środki na konto użytkownika.

        :param pin: PIN użytkownika.
        :param amount: Kwota do wpłacenia.
        :return: Aktualne saldo po wpłacie.
        :raises InvalidPinException: Jeśli podany PIN jest nieprawidłowy.
        """

        if pin != self.pin:
            raise InvalidPinException("Nieprawidłowy PIN")
        if amount <= 0:
            raise ValueError("Kwota wpłaty musi być większa od 0")
        self.balance += amount
        return self.balance

    def withdraw(self, pin: int, amount: float) -> float:
        """
        Wypłaca środki z konta użytkownika.

        :param pin: PIN użytkownika.
        :param amount: Kwota do wypłacenia.
        :return: Aktualne saldo po wypłacie.
        :raises InsufficientFundsException: Jeśli saldo jest niewystarczające.
        :raises InvalidPinException: Jeśli podany PIN jest nieprawidłowy.
        """
        if pin != self.pin:
            raise InvalidPinException("Nieprawidowy PIN")
        if amount <= 0:
            raise ValueError("Kwota wypłaty musi być większa od 0")
        if amount > self.balance:
            raise InsufficientFundsException("Niewystarczające środki na koncie")
        self.balance -= amount
        return self.balance


class User:
    def __init__(self, name, age):
        self._name = name
        self.set_age(age)  # używamy settera już w konstruktorze

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if not isinstance(new_age, int):
            raise ValueError("Wiek musi być liczbą całkowitą.")
        if new_age < 0 or new_age > 130:
            raise ValueError("Wiek musi być w przedziale 0-130.")
        self._age = new_age

# Test
try:
    user = User("Jan", 30)
    print(f"Początkowy wiek: {user.get_age()}")

    user.set_age(-5)
except ValueError as e:
    print(f"Błąd przy ustawianiu wieku: {e}")

try:
    user.set_age(200)
except ValueError as e:
    print(f"Błąd przy ustawianiu wieku: {e}")

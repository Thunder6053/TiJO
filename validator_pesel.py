from register_form_fields import RegisterFormFields
from validator import Validator

class PeselValidator(Validator):
    def __init__(self, pesel):
        self.pesel = pesel

    def is_valid(self):
        if not self.pesel or not self.pesel.isdigit() or len(self.pesel) != 11:
            return False

        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        control_sum = sum(int(self.pesel[i]) * weights[i] for i in range(10))
        control_digit = (10 - control_sum % 10) % 10
        return control_digit == int(self.pesel[-1])

    def field_name(self):
        return RegisterFormFields.PESEL
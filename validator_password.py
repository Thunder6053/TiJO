import re
from register_form_fields import RegisterFormFields
from validator import Validator

class PasswordValidator(Validator):
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        if not self.password or len(self.password) < 4:
            return False
        pattern = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-]).{4,}$")
        return bool(pattern.match(self.password))

    def field_name(self):
        return RegisterFormFields.PASSWORD
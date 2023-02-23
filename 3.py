import re

def validate_password(password):
    if len(password) < 8 or len(password) > 15:
        return False

    if not re.search(r'[A-Z]', password) \
            or not re.search(r'[a-z]', password) \
            or not re.search(r'[!@#$%^&*(),.?":{}|<>]', password) \
            or not re.search(r'[0-9]', password):
        return False

    if re.search(r'(?i)qwerty|asd', password):
        return False

    return True

password = "Abcd1234!"
is_valid = validate_password(password)
print(is_valid)

password = "qwerty123!"
is_valid = validate_password(password)
print(is_valid)
import re

def camel_to_snake(camel_str):
    # replace capital letters with '_'+lowercase version
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_str

# example usage
print(camel_to_snake("myCamelCaseString"))  # output: my_camel_case_string
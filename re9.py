import re

def insert_spaces(text):
    # split the text at each capital letter that is not at the beginning of the word
    # and insert a space before it
    return re.sub(r'(?<!\b)(?=[A-Z])', ' ', text)

# example usage
text = 'ThisIsAnExampleOfTextWithCamelCase'
result = insert_spaces(text)
print(result)
import re

def split_at_uppercase(s):
    # Split string at uppercase letters
    parts = re.findall('[A-Z][^A-Z]*', s)

    # Join parts with a space and return
    return ' '.join(parts)


# Example usage
s = 'ThisIsAStringWithUpperCaseLetters'
result = split_at_uppercase(s)
print(result)
import re

# define the pattern to match
pattern = r'a.*b$'

# test strings
test_string_1 = 'acb'
test_string_2 = 'abbbbab'
test_string_3 = 'a1b'
test_string_4 = 'ab'
test_string_5 = 'abcdebf'

# find all matches
matches = re.findall(pattern, test_string_1)
print(matches)

matches = re.findall(pattern, test_string_2)
print(matches)

matches = re.findall(pattern, test_string_3)
print(matches)

matches = re.findall(pattern, test_string_4)
print(matches)

matches = re.findall(pattern, test_string_5)
print(matches)
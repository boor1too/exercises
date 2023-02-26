import re

# define the pattern to match
pattern = r'a(b*)'

# test string
test_string = 'abbb ab abbbbb abbbbbb'

# find all matches
matches = re.findall(pattern, test_string)

# print the matches
print(matches)
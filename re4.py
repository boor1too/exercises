import re

# define the pattern to match
pattern = r'[A-Z][a-z]+'

# test string
test_string = 'This is a Test for Regex Matching'

# find all matches
matches = re.findall(pattern, test_string)

# print the matches
print(matches)
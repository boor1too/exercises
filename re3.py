import re

# define the pattern to match
pattern = r'[a-z]+_[a-z]+'

# test string
test_string = 'this_is_a_test for_regex_matching'

# find all matches
matches = re.findall(pattern, test_string)

# print the matches
print(matches)
import re

string = "This is a sample, string. With spaces, commas, and dots."
pattern = r"[ ,\.]"
replacement = ":"

new_string = re.sub(pattern, replacement, string)

print(new_string)
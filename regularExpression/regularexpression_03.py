import re

pattern = r'gr.y'  # Matches "gray", "green", etc.

text1 = "gray"
text2 = "green"
text3 = "grxy"

print(re.match(pattern, text1))  # Match
print(re.match(pattern, text2))  # Match
print(re.match(pattern, text3))  # No match

pattern = r'ab.*cd'  # Matches "abcd", "abxcd", "ab123cd", etc.

text1 = "abcd"
text2 = "abxyzcd"
text3 = "ab123cd"

print(re.match(pattern, text1))  # Match
print(re.match(pattern, text2))  # Match
print(re.match(pattern, text3))  # Match

pattern = r'\w+'  # Matches one or more word characters (alphanumeric + underscore).

text = "hello_world_123"

print(re.match(pattern, text).group())  # Output: hello_world_123


pattern = r'\d+'  # Matches one or more digits.

text = "12345"

print(re.match(pattern, text).group())  # Output: 12345

pattern = r'\D+'  # Matches one or more non-digit characters.

text = "abc123"

print(re.match(pattern, text).group())  # Output: abc
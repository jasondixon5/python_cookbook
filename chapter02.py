"""
Chapter 2: Strings and Text
"""
import os
import re

"""
2.1 Splitting strings on any of multiple delimiters
"""

# Need to split a string into fields, but the delimiters
# and spacing around them aren't consistent

# Use re.split() instead of split()

line = "asdf fjdk; afed, fjek,asdf,       foo"
split_line = re.split(r"[;,\s]\s*", line)
print("2.1")
print(line)
print(split_line)

# If use parentheses instead of brackets inside re.split(),
# creates a capture group that will also capture the 
# delimiters
# Note the use of pipes also
fields = re.split(r"(;|,|\s)\s*", line)
print(fields)

"""
2.2 Matching text at the start or end of a string
"""
# Check start of end of string for specific text patterns
# using str.startswith() or str.endswith()

filename = "spam.txt"
print(filename)
print(filename.endswith("txt"))
print(filename.startswith("file:"))
url = "http://www.python.org"
print(url.startswith("http"))

# Can also pass a tuple of possibilities to check
# against multiple choices
exts_to_check = (".txt", ".doc", ".docx", ".csv")
print(filename.endswith(exts_to_check))
dir_files = os.listdir("../..")
dir_text_files = [
    filename for filename in dir_files if filename.endswith(
        exts_to_check)]
for filename in dir_text_files:
    print(filename)


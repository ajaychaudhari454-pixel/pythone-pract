"""
Program Name: Remove Extra Spaces from String
Description :
This program demonstrates line-by-line execution of string methods.
It finds the position of a double space in a string and replaces it
with a single space.
"""

# Step 1:
# A string object is created in memory.
# The string contains an extra double space between 'good' and 'boy'.
name = "ajay is good  boy"

# Step 2:
# Python starts executing the find() method on the string.
# It scans the string from left to right.
# When it finds the first occurrence of double space ("  "),
# it returns the starting index of that position.
# The returned value is passed to the print() function.
print(name.find("  "))

# Step 3:
# Python executes the replace() method on the string.
# It searches for all occurrences of double space ("  ").
# Each double space is replaced with a single space (" ").
# A new string is created (original string remains unchanged).
# The new string is then printed on the screen.
print(name.replace("  ", " "))

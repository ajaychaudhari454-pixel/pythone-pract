"""
Program Name: String Methods Demonstration
Description:
This program demonstrates step-by-step execution of various
Python string operations on a single string.
"""

# Step 1:
# A string object is created and stored in memory.
name = "ajay keep it up"


# Step 2:
# Python slices the string from index 0 up to (but not including) index 4.
# The sliced string is then printed.
print(name[0:4])


# Step 3:
# Python calculates the total number of characters in the string.
# The length value is printed.
print(len(name))


# Step 4:
# Python converts negative indexes to positive internally.
# It extracts characters starting from -4 up to -1 (excluding -1).
print(name[-4:-1])


# Step 5:
# Python starts slicing from index 1 to index 6,
# skipping characters with a step value of 3.
print(name[1:6:3])


# Step 6:
# Python checks whether the string ends with "up".
# It returns a boolean value and prints it.
print(name.endswith("up"))


# Step 7:
# Python checks whether the string starts with "ajay".
# The boolean result is printed.
print(name.startswith("ajay"))


# Step 8:
# Python scans the entire string and counts occurrences of "a".
print(name.count("a"))


# Step 9:
# Python creates a new string with the first character capitalized.
print(name.capitalize())


# Step 10:
# Python searches for "ajay" and replaces it with "vijay".
# A new string is created and printed.
print(name.replace("ajay", "vijay"))


# Step 11:
# Python repeats the string 3 times and prints the result.
print(name * 3)


# Step 12:
# Python converts all characters in the string to uppercase.
print(name.upper())


# Step 13:
# Python converts all characters in the string to lowercase.
print(name.lower())


# Step 14:
# Python converts the first character of each word to uppercase.
print(name.title())


# Step 15:
# Python searches for the substring "keep".
# It returns the starting index of the first match.
print(name.find("keep"))


# Step 16:
# Python searches for the first occurrence of character "k".
# If found, its index is returned and printed.
print(name.index("k"))


# Step 17:
# Python splits the string into a list using space as the separator.
print(name.split(" "))


# Step 18:
# Python removes leading and trailing whitespace (if any).
print(name.strip())


# Step 19:
# Python checks whether the string contains only letters and numbers.
print(name.isalnum())


# Step 20:
# Python checks whether the string contains only alphabetic characters.
print(name.isalpha())


# Step 21:
# Python checks whether all characters in the string are lowercase.
print(name.islower())


# Step 22:
# Python checks whether the string contains only whitespace characters.
print(name.isspace())


# Step 23:
# Python checks whether all characters in the string are uppercase.
print(name.isupper())


# Step 24:
# Python swaps uppercase characters to lowercase and vice versa.
print(name.swapcase())


# Step 25:
# Python centers the string within a width of 50 characters.
print(name.center(50))


# Step 26:
# Python pads the string with leading zeros until the length becomes 50.
print(name.zfill(50))


# Step 27:
# Python splits the string into three parts using "keep" as the separator.
print(name.partition("keep"))


# Step 28:
# Python splits the string from the right using "up" as the separator.
print(name.rpartition("up"))


# Step 29:
# Python left-justifies the string within a width of 50 characters.
print(name.ljust(50))


# Step 30:
# Python right-justifies the string within a width of 50 characters.
print(name.rjust(50))


# Step 31:
# Python splits the string from the right using space as the separator.
print(name.rsplit(" "))

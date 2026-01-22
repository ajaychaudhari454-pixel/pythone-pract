"""
Demonstration of Python list mutability.

This script shows:
- How to create a list
- How to access elements using indexing
- How to modify list elements (lists are mutable)
"""

# Create a list containing different data types
friends = ["ajay", "nirmal", "suresh", "ram", False, "shyam", 3225]

# Print the type of the variable
print(type(friends))

# Access and print the first element of the list
print(friends[0])

# Modify the first element of the list (lists are mutable)
friends[0] = "vikram"

# Print the updated first element
print(friends[0])

# Create a tuple containing different data types
a = ("ajay", 23, 5.6, True, "kumar", "vijay", "sanket")

# Print the entire tuple
print(a)

# Count how many times the value 45 appears in the tuple
# Since 45 is not present, the result will be 0
no = a.count(45)
print(no)

# Find the index position of the element "vijay" in the tuple
no = a.index("vijay")
print(no)

# Check whether "vijay" exists in the tuple
print("vijay" in a)

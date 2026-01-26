# Create a list of integers
a = [12, 32, 45, 67, 32, 89, 32]

# Check if the sum of list elements is greater than 50
# If true, it prints True; otherwise, it prints "fail"
print(sum(a) > 50 if sum(a) > 50 else "fail")

# Count how many times the value 32 appears in the list
count_32 = a.count(32)
print(count_32)

# Sort the list in ascending order
a.sort()

# Print the sorted list
print(a)

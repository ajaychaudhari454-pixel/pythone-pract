# Dictionary to store subject names as keys and marks as values
mark = {
    "science": 90,
    "math": 80,
    "english": 70,
    "marathi": 60,
    "hindi": 90,
    "sanskrit": 90,
    "history": 54
}

# Initialize total marks variable
total = 0

# Calculate total marks by iterating through the dictionary
for subject in mark:
    total = total + mark[subject]

# Calculate percentage (assuming total marks out of 700)
percent = (total / 700) * 100

# Determine grade based on percentage
if percent > 90:
    grade = "A"
elif percent > 80:
    grade = "B"
elif percent > 70:
    grade = "C"
else:
    grade = "D"

# Print final results
print("Total =", total)
print("Percentage =", percent)
print("Grade =", grade)

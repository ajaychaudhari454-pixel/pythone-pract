# Create an empty list to store marks of subjects
marks = []

# Take input for subject 1 and convert it to integer
f1 = int(input("Enter the marks of subject 1: "))
marks.append(f1)  # Add subject 1 marks to the list

# Take input for subject 2 and convert it to integer
f2 = int(input("Enter the marks of subject 2: "))
marks.append(f2)  # Add subject 2 marks to the list

# Take input for subject 3 and convert it to integer
f3 = int(input("Enter the marks of subject 3: "))
marks.append(f3)  # Add subject 3 marks to the list

# Sort the marks list in ascending order
marks.sort()

# Calculate and print the total marks entered by the user
print("You entered:", sum(marks))

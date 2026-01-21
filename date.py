# Program to calculate the average of two numbers

# Taking the user's name as input
name = input("Enter your name: ")

# Importing datetime class to get current date
from datetime import datetime

# Getting today's date from the system
today = datetime.now().strftime("%d-%m-%Y")

# Printing a good morning message with name and date
print(f"Good morning {name}, today's date is {today}")



#name="""dear <[name]>,
#You are invited to the 
#annual gathering on <[date]>."""

#print(name.replace("<[name]>", "nirmal").replace("<[date]>","6th june 2024"))
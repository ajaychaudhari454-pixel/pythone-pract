# List banayi jisme string, number aur boolean values hain
name = ["ajay", "nirmal", "suresh", "ram", 1222, False, "shyam", 3225]  # mutable list

# name list ka type check karne ke liye
# print(type(name))

# List ke end me ek naya element add karta hai
name.append("vikram")

# Numbers wali list
list = [1, 22, 11, 45, 66, 44, 55, 23, 43]

# List ko ascending order me sort karta hai
# list.sort()

# List ke elements ka order reverse karta hai
# list.reverse()

# Index 2 par value 100 insert karta hai
# list.insert(2, 100)

# List me se first occurrence of 44 remove karta hai
# list.remove(44)

# List ka last element remove karta hai
# list.pop()

# Index 2 ka element remove karta hai
# list.pop(2)

# Index 2 ka element remove karke usko print karta hai
# print(list.pop(2))

# List ke sare elements remove kar deta hai
# list.clear()

# name list ke sare elements ko list me add karta hai
# list.extend(name)

# Kisi element ki kitni baar occurrence hai wo batata hai
# list.count(4)

# Kisi element ka first index return karta hai
# list.index(22)

# Final list print karta hai
print(list)

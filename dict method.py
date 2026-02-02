# Dictionary banayi
mark = {
    "mark": 123,
    "ajay": 143,
    "subham": 324
}

# saare key-value pairs print karta hai
# print(mark.items())

# sirf keys print karta hai
# print(mark.keys())

# 'ajay' key ki value safely deta hai
# print(mark.get("ajay"))

# sirf values print karta hai
# print(mark.values())

# 'ajay' ki value update karta hai
# mark.update({"ajay": 4556})

# poori dictionary print karta hai
# print(mark)

# 'ajay' ki value print karta hai
# print(mark.get("ajay"))

# 'ajay' key ko delete karta hai aur uski value return karta hai
# print(mark.pop("ajay"))

# check karta hai ki 'ajay' ya 'subham' key dictionary me hai ya nahi
if "ajay" in mark or "subham" in mark:
    print("available")
else:
    print("not available")

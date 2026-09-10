role = str(input("Enter your role: "))
age = int(input("Enter your age: "))
print("Discount Eligibility: ", role=="admin" and age < 21)
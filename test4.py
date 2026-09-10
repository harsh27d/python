a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
print("before swapping: a =", a, "b =", b)
a=a + b
b=a - b
a=a - b
print("after swapping: a =", a, "b =", b)
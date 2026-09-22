n = int(input("Enter number of rows: "))

num = 1

for i in range(n, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
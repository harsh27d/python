#Search an Element: Write a program to accept N integers into an array and search for a given number. Display an appropriate message indicating whether the number is present in the array or not and also display its position. 
n = int(input("Enter number of elements: "))
arr = list(map(int, input(f"Enter {n} numbers separated by space: ").split()))
search_num = int(input("Enter the number to search: "))

found = False
for i in range(n):
    if arr[i] == search_num:
        print(f"Number {search_num} is present at position {i}")
        found = True
        break

if not found:
    print(f"Number {search_num} is not present in the array")
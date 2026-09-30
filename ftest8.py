#Reverse the Array: Write a program to accept N integers into an array and display the elements in reverse order without changing the original array. 
n = int(input("Enter number of elements: "))
arr = list(map(int, input(f"Enter {n} numbers separated by space: ").split()))
print("Original array:", arr)
print("Reversed array:", arr[::-1])
#Write a program to accept N integers into an array and calculate and display the sum of all the elements
n= int(input("Enter the numbers: "))
array=[]
for i in range(n):
 num = int(input(f"Enter the {i+1} number:"))
 array.append(num)
array_sum= sum(array)
print("The sum of the array is ",array_sum)
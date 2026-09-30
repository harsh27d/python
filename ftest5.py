#Write a program to accept N integers into an array and find and display the largest element , second largest element , smallest element , second smallest element present in the array 

n = int(input("Enter number of elements: "))

array = list(map(int, input(f"Enter {n} numbers separated by space: ").split()))

largest = -float("inf")
second_largest = -float("inf")

smallest = float("inf")
second_smallest = float("inf")

for num in array:
    
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

# Display the results
print("Smallest element:       ", smallest)
print("Second smallest element:", second_smallest)
print("Second largest element: ", second_largest)
print("Largest element:        ", largest)
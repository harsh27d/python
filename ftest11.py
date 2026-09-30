#Finfd the largest and the second largest and smallest and second smallest number from an array list pgm in class 
arr=[10,3,34,45,32,65,23,53,66,2]
max= min=arr[0]
smin=smax=arr[0]
for num in arr:
    if num > max:
            smax=max
            max=num
    elif(num>smax and num!=max):
         smax=num
         if num<min:
            smin=min
            min=num
    elif (num<sum and num!=min):
           smin=min
print("maximum: ", max)
print("Second Max : ", smax)
print("Smallest: ", min)
print("Second smallest: " , smin)

    
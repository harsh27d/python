min = int(input("Enter a minutes: "))
print("{min} minutes is equal to {result} hours and {minutes} minutes".format(min=min, result=min // 60, minutes=min % 60))
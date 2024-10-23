user=input("enter number seperated by spaces:")
numbers=user.split()
for i in range(len(numbers)):
    if int(numbers[i])>100:
        numbers[i]='over'
print("list is",numbers)
        

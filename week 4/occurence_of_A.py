list=[]
sum=0
size=int(input("enter the size of the list"))
for i in range(size):
    a=(input("enter the name:"))
    list.append(a)
for j in list:
     count1=j.count("a")
     count2=j.count("A")
     count=count1+count2
     sum=sum+count
print(sum)

list1=[]
list2=[]
n=int(input("Enter the number of terms: "))
for i in range (1,n+1):
    a=int(input("Enter the %d value: "%i))
    list1.append(a)
print ("The Entered list is: ",list1)

i=1

while(i<=len(list1)):
    c=max(list1)
    list2.insert(0,c)
    list1.remove(c)
print("The sorted list is: ",list2)

        


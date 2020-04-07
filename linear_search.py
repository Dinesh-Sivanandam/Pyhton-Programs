#Linear Search

def linearsearch(arr,x):
    for i in range(len(arr)):
        if (arr[i]==x):
            return i
    return -1

list1=[]
l=int(input("Enter the number of array: "))
for j in range(l):
    item=int(input())
    list1.append(item)
a=int(input("Enter the number to search: "))
b=linearsearch(list1,a)
if(b != -1):
    print("Element present at ",(b+1))
else:
    print("Element not present")
    
    

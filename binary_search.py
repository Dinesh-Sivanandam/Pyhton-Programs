#Binary Search

def binarysearch(arr,l,r,x):
    while l <= r: 
  
        mid = l + (r - l)//2; 
        if arr[mid] == x: 
            return mid
        elif arr[mid] < x: 
            l = mid + 1
        else: 
            r = mid - 1
    return -1

list1=[]
l=int(input("Enter the number of array: "))
for j in range(l):
    item=int(input())
    list1.append(item)
a=int(input("Enter the number to search: ")) 

result = binarysearch(list1, 0, len(list1)-1, a) 
  
if result != -1: 
    print ("Element is present at index %d" % result) 
else: 
    print ("Element is not present in array")

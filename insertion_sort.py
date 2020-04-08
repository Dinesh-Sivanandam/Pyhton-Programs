def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
		
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element

list1=[]
n=int(input("Enter the number of terms: "))
print("Enter the elements:")
for i in range(n):
    item=int(input())
    list1.append(item)
insertion_sort(list1)
print(list1)

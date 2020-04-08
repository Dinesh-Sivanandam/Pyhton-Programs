def bubblesort(list):
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp


list=[]
n=int(input("Enter the number of terms: "))
print("Enter the elements:")
for i in range(n):
    item=int(input())
    list.append(item)
bubblesort(list)
print(list)

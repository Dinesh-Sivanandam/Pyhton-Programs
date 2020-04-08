def selection_sort(input_list):

    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


list1=[]
n=int(input("Enter the number of terms: "))
print("Enter the elements:")
for i in range(n):
    item=int(input())
    list1.append(item)
selection_sort(list1)
print(list1)

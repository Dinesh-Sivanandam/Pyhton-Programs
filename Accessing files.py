import os #for getting the file name
import shutil # for performing the move operations between directiories
list=[]
idx=[]
entries=os.listdir('Downloads\\AgeDB\\') #getting the elements in the directory
for j in range(0,len(entries)):
    element=entries[j]
    index=element.index('_') #getting the first index value from name starts
    for k in range(index+1,len(element)):
        if element[k]=='_':
            break   #getting the last index value till name ends
    name=element[index+1:k]
    list.append(name) #append the names to the list
res=[]
for x in list:
    if x not in res:
        res.append(x) #removing the duplicates from the list

for y in range(0, len(res)):
    name=res[y]
    path="C:\\Users\\DINESH\\AppData\\Local\\Programs\\Python\\Python38-32\\Downloads\\"
    folder=os.path.join(path,name)
    os.mkdir(folder)  # creating the folders according to the names in the removed duplicate list

for d in range(0, len(res)): #getting the values of sorted list
    for z in range(0,len(list)): #getting the values of the list
        if(list[z]==res[d]): #checking the value of list is as same as res
            shutil.move('C:\\Users\\DINESH\\AppData\\Local\\Programs\\Python\\Python38-32\\Downloads\\AgeDB\\'+entries[z],'C:\\Users\\DINESH\\AppData\\Local\\Programs\\Python\\Python38-32\\Downloads\\'+res[d])
#moving the files by getting the list index and mobing the file by the index to the specified file

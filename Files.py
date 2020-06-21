import os
f=open("Dat.txt",'w')
f.write("This is the sample text.")
f.close()
f=open("Dat.txt",'r')
print(f.read()) #prints the above typed text
f.close()

#appending the text
f=open('Dat.txt','a')
f.write(" This is the appended text.")
f.close()
#printing the appended file
f=open("Dat.txt",'r')
print(f.read())

#Deleting the file
os.remove("Dat.txt")
f=open("Dat.txt",'r')#Shows error that the file is missing

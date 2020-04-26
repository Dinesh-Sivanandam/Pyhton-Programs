#You have a record of n students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and marks for  students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

if __name__ == '__main__':
    N = int(input())
    results = {}
    for i in range(N):
        a = input().split(' ')
        results[a[0]] = [float(x) for x in a[1:]]
    student = input()
    print ("%.2f" %(sum(results[student])/len(results[student])))

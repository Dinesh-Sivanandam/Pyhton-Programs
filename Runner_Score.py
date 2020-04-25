if __name__ == '__main__':
    lis=[]
    i = int(input())
    for n in range(i):
        a=int(input())
        lis.append(a)
    m=max(lis)
    while max(lis)==m:
        lis.remove(m)
    m=max(lis)
    print(m)


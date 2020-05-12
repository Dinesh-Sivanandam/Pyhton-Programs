from itertools import permutations
I = raw_input().split()
k = map(''.join,list(permutations(I[0],int(I[1]))))
k.sort()
for i in k:
    print ''.join(i)

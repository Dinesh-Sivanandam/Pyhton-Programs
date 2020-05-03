N, M = map(int,input().split())
for i in range(0,N/2): 
    print ('.|.'*i).rjust((M-2)/2,'-')+'.|.'+('.|.'*i).ljust((M-2)/2,'-')
print 'WELCOME'.center(M,'-')
for i in reversed(range(0,N/2)): 
    print ('.|.'*i).rjust((M-2)/2,'-')+'.|.'+('.|.'*i).ljust((M-2)/2,'-')

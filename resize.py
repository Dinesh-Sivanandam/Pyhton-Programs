import numpy as np

#using the order c
a = np.array([[0, 1,2], [3,4,5],[6,7,8]], order='C')
a.resize((3,1))
print(a)
print()

#using the order f
a = np.array([[0, 1,2], [3,4,5],[6,7,8]], order='F')
a.resize((3,1))
print(a)

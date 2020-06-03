import numpy as np
import random
a=np.random.randint(9,size=(3,3))
print(a)

#printing a blank line
print()

#including flags in array
a.setflags(write=0,align=0)

#printing the attributes
print(a.flags)

#again blank line
print()

#printing transpose of array
print(a.transpose())
print()

#flatten in numpy
print(a.flatten('F'))
print()

#take the values by the index
indices = [0, 1, 4]
print(np.take(a, indices))

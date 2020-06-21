import matplotlib.pyplot as plt
a=(1,2,3,4)
x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(a,[4,5,6,7],label='Line 1')
plt.plot(x,y,label='Line 2')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title("Difference Line")
plt.show()

#Plotting two lines
x=[1,2,3]
y=[5,7,4]
x1=[1,2,3]
y1=[10,14,12]
plt.plot(x,y,label='Line 1')
plt.plot(x1,y1,label='Line 2')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('LINE GRAPH')
plt.legend()
plt.show()

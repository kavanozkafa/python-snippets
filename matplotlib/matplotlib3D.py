import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from matplotlib import style

#lets create shortcut
figure = plt.figure()
ax1 = figure.add_subplot(111,projection='3d')


x = [1,2,3,4,5,10,6,7,8,9]
y = [4,5,6,7,8,9,11,21,5,12]
z = [1,2,3,2,4,3,5,6,7,8]

style.use('ggplot')
ax1.scatter(x,y,z,marker='*',c='red')

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

#plt.show()



x1=np.ones(10)
y1=np.ones(10)
z1=[1,2,3,4,5,6,7,8,9,10]

ax1.bar3d(x,y,z,x1,y1,z1)
plt.show()


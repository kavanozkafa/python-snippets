import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style


style.use('ggplot')

x,y = np.loadtxt('mycsv.csv',unpack=True,delimiter = ',')
plt.plot(x,y,color='#D151CC',marker='o')
plt.show()


"""
put these numbers in a text file and save as mycsv.csv 

1,2
3,4
5,10
6,7
8,9
4,5
6,7
8,9
11,21
5,12

"""
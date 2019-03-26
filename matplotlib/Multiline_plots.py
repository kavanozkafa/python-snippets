import matplotlib.pyplot as plt 
import numpy as np


#Multiline plots
x = np.arange(1, 5)
plt.plot(x, [xi*1.5 for xi in x])
plt.plot(x, [xi*3.0 for xi in x])
plt.plot(x, [xi/3.0 for xi in x])
plt.show()


#same thing but one line
plt.plot(x, [xi*1.5 for xi in x], x, [xi*3.0 for xi in x], x, [xi/3.0 for xi in x])
plt.show()

#same thing with numpy arange
plt.plot(x, x*1.5, x, x*3.0, x, x/3.0)
plt.show()

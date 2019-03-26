from matplotlib import pyplot
from matplotlib import style

style.use('ggplot')


x = [22,43,5,76]
y = [3,42,41,56]

k = [2,3,5,6]
l = [3,2,4,6]

pyplot.grid(True,color='k')
pyplot.plot(x,y,'green',linewidth=5,label = 'line One')
pyplot.plot(k,l,'yellow',linewidth=3,label = 'line two')

pyplot.title('my Chart')
pyplot.ylabel('Y axis')
pyplot.xlabel('X axis')
pyplot.legend()
pyplot.show()


"""
pyplot.scatter(x,y,'green',linewidth=5,label = 'line One')
pyplot.scatter(k,l,'yellow',linewidth=3,label = 'line two')
pyplot.bar(x,y,'g')
pyplot.bar(k,l,'y')
"""


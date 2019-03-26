from matplotlib import pyplot as plt
import numpy as np 

#Components of a Matplolib Plot
#matplotlib figure hierarchy : 
#figure >> axes >> lines,markers,legends,ticks,title,colorbars

#plot method is more for large datasets
#scatter method is more for small datasets


#Our datas 
x = [4,9,16,25,36,49]
y = [8,27,64,125,343,512]

#we can add more data
# for end of list
x1 = x + [64,81] 
y1 = y + [643, 765]

#for head of list
x = [1,2] + x 
y = [2,4] + y


#just a simple graph
#plt.plot(x,y)
#plt.show()

#lets put some color on the graph
#plt.plot(x,y,color='red') # or plt.plot(x,y,'red')
#color='red' / c = 'r' /'red'/'r' all are the same thing
#plt.show()


#we can change the graph style
#plt.plot(x,y,color='green',linestyle='dashed')
#plt.show()

#lets put marker on the x and y
#plt.plot(x,y,color='green',linestyle='dashed',marker='o',markersize=10,markerfacecolor='yellow')
#plt.show()


#if you dont want line and just the x an y
#plt.plot(x,y,'*') # o,*,+,v,<,>,1,2,3,4,:,-
#plt.show()


#lets explain what are x and y with title
#plt.plot(x,y,color='green',marker='o',linestyle='dashed')
#plt.xlabel("money")
#plt.ylabel('days')
#plt.title("saving account")

#lets change milestones of y
plt.yticks([0,200,300,500,800],
			['0','2K','3K','5K','8K'])
#plt.show()


#what about a bar chart
#plt.bar(x,y,color='g') #g stands for color green
#plt.xlabel("money")
#plt.ylabel('days')
#plt.title("saving account")
#plt.show()

#lets rotate it 
#plt.barh(x,y,color='g') #h means horizontal
#plt.xlabel("money")
#plt.ylabel('days')
#plt.title("saving account")
#plt.show()


#what about histograms
#rpm = [80,81,76,77,79,68,93,92,89,87,76,75,77,77,77,83]
#plt.hist(rpm,color='green')
#plt.show()

#dont forget pie chart
#money = [200,350,456,120]
#spend = ['rent','fun','school','food']
#plt.pie(money,labels=spend,radius= 1,shadow=True,startangle=45)
#plt.savefig("piechart.png") # let save the chart
#plt.show()




#set up for figure
plt.rcParams['figure.figsize'] = (4,3)
plt.rcParams['figure.dpi'] = 150



#lets create datas with numpy
#Xvalues = np.arange(0,10,0.1)
#markevery means mark every 1 data of 7. 
# ms or markersize means size of marker
#'r.' -- red
#plt.plot(Xvalues, np.sin(Xvalues),'r.',marker = '>',ms=2,markevery=7) 
#plt.show()

#different line styles
#idx = 0 
#for marker in ('<','*',':','--','-.'):
#	plt.plot(Xvalues,np.sin(Xvalues) + idx, ''.join(('k',marker)))
#	idx += 1



#  r'$ special characters $'
#plt.xlabel(r'$Sigma$')
#plt.ylabel("YYY")
#plt.title("ZZZ")
#plt.show()


#spesific marker
#plt.plot(x,y,color ='m',linestyle='none',marker=r'$sammas$',markersize=20)
#plt.show()


# with linewidth we can change the size of line
#plt.plot(x,y,color ='m',linewidth=2,marker=r'$sammas$',markersize=20)
#plt.show()


#We can decide the order
plt.plot(x,y,label='first',color ='m',linewidth=2,marker='*',zorder=0)
plt.plot(x1,y1,label='second',color ='g',linewidth=2,marker='D',zorder=1)
#plt.plot(x,y,color ='b',linewidth=2,marker='<',zorder=3)
#plt.plot(x,y,color ='y',linewidth=2,marker='o',zorder=2)
plt.legend()
plt.show()

#transparency with "alpha"
#plt.plot(x,y,color ='g',linewidth=2,marker='o',alpha=0.5)
#plt.plot(y,x,color ='g',linewidth=2,marker='o',alpha=1)
#plt.show()





#with scatter method you can get rid of line
# scatter uses markers

#plt.scatter(x,y) # for individual graphs.without line


# with rainbow marker
# c-->color 
#cmap is colormap
#edgecolor let us see color of marker .it is useful with small markers.
# s--> size
#plt.scatter(y,x,c=np.cos(x),cmap='Accent',s=np.power(x,2),edgecolor='none') 
#plt.colorbar() #means of color
#plt.show()




x1 = x +y 
y1 = x + x

#bar charts
plt.bar(x,y,label='Bars1',color='#D151CC')
plt.bar(x1,y1,label='Bars2',color = 'green')
plt.legend()
plt.show()


#histograms

population = [21,27,34,38,35,42,48,49,49,56]

#we dont wanna put datas because we can generate them
ID = [x for x in range(len(population))]

plt.bar(ID,population)
plt.show()







x = np.arange(1, 5)
plt.plot(x, x*1.5, label='Legend1')
plt.plot(x, x*3.0, label='Legend2')
plt.plot(x, x/3.0,label='Legend3')
#Adding a grid
plt.grid(True) 



#Handling axes
plt.axis()	# shows the current axis limits (1.0, 4.0, 0.0, 12.0)
plt.axis([0, 5, -1, 13])	# set new axes limits


#We can also control the limits for each axis separately using xlim() and ylim() functions
#Also for xlim() and ylim(), we can pass a list of two values (for example,
#xlim([xmin, xmax])), or use the keyword arguments.


plt.xlim() #(1.0, 4.0)
plt.ylim() #(0.0, 12.0)



plt.legend()
#Alternatively, we could specify the labels of the lines (as mentioned in their respective label arguments), as a list of strings to the legend() call.
#plt.legend(['Normal', 'Fast', 'Slow'])

#for legend posiiton
plt.legend(loc='upper center')

"""
String	Code
best	0
upper right	1
upper left	2
lower left	3
lower right	4
right	5
center left	6
center right	7
lower center	8
upper center	9
center	10
"""


#Saving plots to a file as svg,png or pdf
plt.savefig('plot123.png')
plt.savefig('plot123_2.pdf', dpi=200) 
# dpi = dot per inch. 200= 1600 x 1200 // 100 DPI results in an 800x600




plt.show()













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






x = np.arange(1, 5)
plt.plot(x, x*1.5, 'purple')
plt.plot(x, x/1.5, 'cyan')



#Handling X and Y ticks
#Executing with no arguments, the tick function returns the current ticks' locations and the labels corresponding to each of them:
#locs, labels = plt.xticks()
#The arguments (in the form of lists) that we can pass to the function are:
#Locations of the ticks
#Labels to draw at these locations (if necessary)
plt.xticks(range(len(x)), ['a', 'b', 'c', 'd', 'e', 'f']);
plt.yticks(range(1, 8, 2));



plt.show()


"""
Finer control with keyword arguments
plot() is a really rich function, and there are some keyword arguments to configure colors, markers, and line styles:

Keyword argument	Description
color   or c		Sets the color of the line; accepts any Matplotlib color format.
linestyle			Sets the line style; accepts the line styles seen previously.
linewidth			Sets the line width; accepts a float value in points.
marker				Sets the line marker style.
markeredgecolor		Sets the marker edge color; accepts any Matplotlib color format.
markeredgewidth		Sets the marker edge width; accepts float value in points.
markerfacecolor		Sets the marker face color; accepts any Matplotlib color format.
markersize			Sets the marker size in points; accepts float values.


plt.plot(y, color='blue', linestyle='dashdot', linewidth=4, marker='o', markerfacecolor='red', markeredgecolor='black', markeredgewidth=3, markersize=12)

"""


# Histogram charts

"""Histogram charts are a graphical display of frequencies, represented as bars. 
They show what portion of the dataset falls into each category, usually specified 
as non-overlapping intervals. Matplotlib calls those categories bins.

Histogram plots group up values into bins of values. By default, hist() uses a bin
value of 10 (so only ten categories, or bars, are computed), but we can customize  it, 
either by passing an additional parameter, for example, in hist(y, <bins>), 
or using the bin keyword argument as hist(y, bin=<bins>)."""

y = np.random.randn(1000)
plt.hist(y,25);
plt.title(" Histogram chart")
plt.show()





#Error bar charts
"""
In experimental sciences, we know that all the measurements that we take lack perfect precision. 
This leads to repeating the measurements, which results in obtaining a set of values. 
The expected result is that all those measures group up around the true value that we want to measure.
The representation of this distribution of data values is done by plotting a single data point, 
(commonly) the mean value of dataset, and an error bar to represent the overall distribution of data. 
This helps us to get a general idea of how accurate a measurement is (or how far the reported value could be from the error-free value).

"""
x = np.arange(0, 4, 0.2)
y = np.exp(-x)
e1 = 0.1 * np.abs(np.random.randn(len(y)))
e2 = 0.1 * np.abs(np.random.randn(len(y)))
plt.errorbar(x, y, yerr=e1, xerr=e2, ecolor='green', fmt='.-', capsize=0)
plt.title(" Error Bar chart")
plt.show()



#Bar charts
#The function expects two lists of values: the X coordinates that are the positions of the bar's left margin and the heights of the bars:
plt.bar([1, 2, 3], [3, 2, 5]);
plt.title("Bar chart")
plt.show()





#Pie charts

"""
Pie charts are circular representations, divided into sectors (also called wedges). 
Wedges are created proportionally, so that each value x of array X generates a wedge proportional to x/sum(X).
if sum(X) is less than 1, then the pie is drawn using X values directly and no normalization is done, resulting in a pie with discontinuity.
Pie charts look best if the figure and axes are in a square format (if not, with the common rectangular figure, they look like ellipses).

explode: If specified, it's an array of the same length as that of X. Each of its values specify the radius 
fraction with which to offset the wedge from the center of the pie.
colors: This is a list of Matplotlib colors, 
labels, labeldistance: This is a list of labels, one for each of the X values.
labeldistance is the radial distance at which the labels are drawn.
autopct, pctdistance: This formatting string or function is used to label wedges with their numeric values. 
pctdstance is the ratio between the center of the pie and the start of the text.
shadow: This draws a shadow for wedges or pie.

"""

plt.figure(figsize=(5,5));
x = [4, 9, 21, 55, 30, 18]
labels = ['Swiss', 'Austria', 'Spain', 'Italy', 'France', 'Benelux']
explode = [0.2, 0.1, 0, 0, 0.1, 0]
plt.pie(x, labels=labels, explode=explode, autopct='%1.1f%%'); 
plt.title("Pie chart")
plt.show()






#Scatter plots
"""
Scatter plots display values for two sets of data. 
a collection of points not connected by lines. 
Each of them has its coordinates
A scatter plot is often used to identify potential association between two variables, and it's often drawn before working on a fitting regression function. 
It gives a good visual picture of the correlation, in particular for nonlinear relationships.


"""

x = np.random.randn(1000) 
y = np.random.randn(1000) 
size = 50*np.random.randn(1000) 
colors = np.random.rand(1000)
plt.scatter(x, y, s=size, c=colors)
plt.title("Scatter plot")
plt.show()







#Polar charts
"""
Polar plots use a completely different coordinate system, so we have dedicated a separate section to them.
A polar system is a two-dimensional coordinate system, where the position of a point is expressed in terms of a radius and an angle. 
This system is used where the relationship between two points is better expressed using those information.
The angular coordinate can be expressed either in radians or in degrees. Though, Matplotlib uses degrees.
The polar() Matplotlib function plots polar charts. Its parameters are two lists (of the same length)
theta for the angular coordinates and r for the radial coordinates. It's the corresponding function of plot() for polar charts, 
so it can take multiple theta and r, along with the formatting strings.
"""
theta = np.arange(0., 2., 1./180.)*np.pi  # we define theta to be an array of 360 values, equally spaced between 0 and 2pi.
plt.polar(3*theta, theta/5); #we draw a spiral.
plt.polar(theta, np.cos(4*theta)) #we draw a polar rose, a pretty function that resembles a flower.
plt.polar(theta, [1.4]*len(theta)) #we draw a circular line. In a polar system, to draw a circle we just need to keep r constant
r = np.abs(np.sin(5*theta) - 2.*np.cos(theta))
plt.polar(theta, r);
plt.thetagrids(range(45, 360, 90));
plt.rgrids(np.arange(0.2, 3.1, .7), angle=0);

plt.title("Polar chart")
plt.show()





#########  Text inside figure, annotations, and arrows

x = np.arange(0, 2*np.pi, .01) 
y = np.sin(x)
plt.plot(x, y);
plt.text(0.1, -0.04, 'sin(0)=0');

plt.show()

y = [13, 11, 13, 12, 13, 10, 30, 12, 11, 13, 12, 12, 12, 11,12]
plt.plot(y);
plt.ylim(ymax=35);
plt.annotate('this spot must really\nmean something', xy=(6, 30), xytext=(8, 31.5), arrowprops=dict(facecolor='black', shrink=0.05));
plt.show()



plt.axis([0, 10, 0, 20]);
arrstyles = ['-', '->', '-[', '<-', '<->', 'fancy', 'simple', 'wedge']
for i, style in enumerate(arrstyles):

	plt.annotate(style, xytext=(1, 2+2*i), xy=(4, 1+2*i), arrowprops=dict(arrowstyle=style))
connstyles=["arc", "arc,angleA=10,armA=30,rad=15", "arc3,rad=.2", "arc3,rad=-.2", "angle", "angle3"]
for i, style in enumerate(connstyles):
	plt.annotate("", xytext=(6, 2+2*i), xy=(8, 1+2*i), arrowprops=dict(arrowstyle='->', connectionstyle=style))

plt.show()
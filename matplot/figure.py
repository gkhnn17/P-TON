import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(-10,9,20)
y= x**3
z = x**2

"""

figure = plt.figure()
#add axes
axes_cube =figure.add_axes([0.2,0.1,0.8,0.8])##x,y,xsize,ysize
axes_cube.plot(x,y,"b")#draw color blue
axes_cube.set_xlabel("X")
axes_cube.set_ylabel("Y")
axes_cube.set_title("Cube")

axes_square = figure.add_axes([0.45,0.4,0.3,0.3])
axes_square.plot(x,y,"r")#draw color blue
axes_square.set_xlabel("X")
axes_square.set_ylabel("Y")
axes_square.set_title("square")
"""

"""figure = plt.figure()

axes = figure.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
axes.legend(loc=1)#labels chart"""

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(4,4))

axes[0].plot(x,z)
axes[0].set_title("Square")

axes[1].plot(x,y)
axes[1].set_title("Cube")
#obstructing titles are overlapping
plt.tight_layout()
fig.savefig("figure1.png")
plt.show()
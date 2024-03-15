import sys
sys.path.insert(0, "/home/aryan/GVV/Q1.1.5/codes/CoordGeo")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#given points
A=np.array([1, -1])
B=np.array([-4, 6])
C=np.array([-3, -5])

#getting the equation of line
omat = np.array([[0,1],[-1,0]])
m = B-A   #direction vector
n = omat@m    #normal vector
c = n@A
eqn = f"{n}x = {c}"
print("The equation of line AB is",eqn)

#plotting the line AB
x_AB = line_gen(A, B)
A = A.reshape(-1,1)
B = B.reshape(-1,1)
tri_coords = np.block([A,B])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
vert_labels=['A','B']     #for labelling points A and B 
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.savefig('/home/aryan/GVV/Q1.1.5/figs/figure1.png')




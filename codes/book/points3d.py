#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Point Vectors


import sys                                          #for path to external scripts
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if

k = -10/7
#Given points
B = np.array(([1, 2,3])).reshape(-1,1) 
m1= np.array(([-3, 2*k,2])).reshape(-1,1) 
m2= np.array(([3*k, 1,-5])).reshape(-1,1) 
C = np.array(([1,1,6])).reshape(-1,1)  
#C = np.array(([-4,-2, 3])).reshape(-1,1)  



# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

#Generating all lines
k1 = -0.5
k2 = 2
x_B = line_dir_pt(m1,B,k1,k2)
k1 = -1
k2 = 2
x_C = line_dir_pt(m2,C,k1,k2)
#x_BC = line_gen(B,C)


#Plotting all lines
ax.plot(x_B[0,:],x_B[1,:], x_B[2,:],label='$B$')
ax.plot(x_C[0,:],x_C[1,:], x_C[2,:],label='$C$')

# Scatter plot
colors = np.arange(1, 3)  # Example colors
tri_coords = np.block([B, C])  # Stack A, B, C vertically
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c=colors)
vert_labels = ['B', 'C']

for i, txt in enumerate(vert_labels):
    # Annotate each point with its label and coordinates
    ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i], f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f}, {tri_coords[2, i]:.0f})',
             fontsize=12, ha='center', va='bottom')

ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
# Set limits and aspect ratio to magnify the plane
ax.set_xlim(-4, 4)  # Adjust limits based on your data
ax.set_ylim(-4, 4)  # Adjust limits based on your data
ax.set_zlim(-4, 4)  # Adjust limits based on your data
ax.set_box_aspect([1,1,1])  # Equal aspect ratio for x, y, and z axes

# Label the axes
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.set_zlabel('$Z$')

'''
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
'''
plt.grid() # minor
plt.axis('equal')
# Rotate the plot
ax.view_init(elev=90, azim=30)  # Set the elevation and azimuth angles

#if using termux
plt.savefig('chapters/12/11/4/6/figs/fig.pdf')
subprocess.run(shlex.split("termux-open chapters/12/11/4/6/figs/fig.pdf"))
#else
#plt.show()

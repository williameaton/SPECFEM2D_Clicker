import numpy as np
import matplotlib.pyplot as plt


# Define dimensions: e.g. from 0 to 28 km in x direction and 0 to 10 in y direction
x_min = 0
x_max = 9*np.pi
y_min = 0
y_max = -10
nx    = 100 # Number of points in x
ny    = 50  # Number of points in y

# Define x,y arrays:
x = np.linspace(x_min, x_max, nx)
y = np.linspace(y_min, y_max, ny)

# print top side (sinusoid)
sin_array = np.sin(x)
for i in range(nx):
    print(f"create vertex {x[-i]} {sin_array[-i]} 0 color brown")

# print right side bottom:
print(f"create vertex {x_max} {y_max} 0 color brown")

# print left side bottom:
#print(f"create vertex {x_min} {y_max} 0 color brown")


# print v top side left:
print(f"create vertex {x_min} -10 0 color brown")
print(f"create vertex {x_max} -10 0 color brown")


# Print command to create surface from vertices:
s = "create surface vertex "
for i in range(105, 500):
    s += f"{i+1} "

print(s)
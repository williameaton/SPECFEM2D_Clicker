import numpy as np
import matplotlib.pyplot as plt

coords = []
image = plt.imread("example.png")

print()


fig, ax = plt.subplots(figsize=(12,7))

ax.imshow(image)


def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    #print(f'x = {ix}, y = {iy}')
    print(f'create vertex {ix} {iy} 0')

    #global coords
    coords.append((ix, iy))

    #if len(coords) == 2:
    #    fig.canvas.mpl_disconnect(cid)

    return coords


cid = fig.canvas.mpl_connect('button_press_event', onclick)

#plt.show()
s = "create surface vertex "
for i in range(400):
    s += f"{i+1} "

print(s)
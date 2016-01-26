import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D

DATA = np.load("../frames10/SIMULATION_SPEC.npy")
if "masses" in DATA:
    #print DATA[np.where(DATA == "masses")[0][0]+1]
    masses = int(DATA[np.where(DATA == "masses")[0][0]+1])
if "total_time" in DATA:
    total_time = float(DATA[np.where(DATA == "total_time")[0][0]+1])
if "dtime" in DATA:
    dtime = float(DATA[np.where(DATA == "dtime")[0][0]+1])
if "size" in DATA:
    size = float(DATA[np.where(DATA == "size")[0][0]+1])
#times = []
# fig = plt.figure(figsize=(6,6))
# ax=fig.add_subplot(1, 1, 1, projection='3d')
# ax.view_init(elev = 45, azim = 45)#(t%2)*5+45)
# ax.set_xlabel('X-Axis')

namex = '../frames10/' + 'x' + '0'*(4-len(str(0))) + str(0) + '.npy'
namey = '../frames10/' + 'y' + '0'*(4-len(str(0))) + str(0) + '.npy'
namez = '../frames10/' + 'z' + '0'*(4-len(str(0))) + str(0) + '.npy'

x = np.load(namex)
y = np.load(namey)
z = np.load(namez)

#plt.ion()
fig = plt.figure(figsize=(6,6))
ax=fig.add_subplot(1, 1, 1, projection='3d')
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
ax.set_xlim3d(-size,size);
ax.set_ylim3d(-size,size);
ax.set_zlim3d(-size,size);
sc = ax.scatter(x,y,z)
fig.canvas.draw()

for t in range(int(total_time/dtime+1)/10):
    namex = '../frames10/' + 'x' + '0'*(4-len(str(t))) + str(t) + '.npy'
    namey = '../frames10/' + 'y' + '0'*(4-len(str(t))) + str(t) + '.npy'
    namez = '../frames10/' + 'z' + '0'*(4-len(str(t))) + str(t) + '.npy'

    x = np.load(namex)
    y = np.load(namey)
    z = np.load(namez)
    sc.remove()
    sc = ax.scatter(x, y, z,'ro')
    #fig.canvas.refresh()
    #

    name = '../frames11/' + '0'*(4-len(str(t))) + str(t) + '.png'
    plt.savefig(name)
    print name
plt.close()
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D

class plotter(object):
    def __init__(self):
        self.loaddata()
        self.initplot()

    def loaddata(self):
        DATA = np.load("../frames10/SIMULATION_SPEC.npy")
        if "masses" in DATA:
            #print DATA[np.where(DATA == "masses")[0][0]+1]
            self.masses = int(DATA[np.where(DATA == "masses")[0][0]+1])
        if "total_time" in DATA:
            self.total_time = float(DATA[np.where(DATA == "total_time")[0][0]+1])
        if "dtime" in DATA:
            self.dtime = float(DATA[np.where(DATA == "dtime")[0][0]+1])
        if "size" in DATA:
            self.size = float(DATA[np.where(DATA == "size")[0][0]+1])
    #times = []
    # fig = plt.figure(figsize=(6,6))
    # ax=fig.add_subplot(1, 1, 1, projection='3d')
    # ax.view_init(elev = 45, azim = 45)#(t%2)*5+45)
    # ax.set_xlabel('X-Axis')

    def initplot(self):
        namex = '../frames10/' + 'x' + '0'*(4-len(str(0))) + str(0) + '.npy'
        namey = '../frames10/' + 'y' + '0'*(4-len(str(0))) + str(0) + '.npy'
        namez = '../frames10/' + 'z' + '0'*(4-len(str(0))) + str(0) + '.npy'

        x = np.load(namex)
        y = np.load(namey)
        z = np.load(namez)

        #plt.ion()
        fig = plt.figure(figsize=(6,6))
        self.ax=fig.add_subplot(1, 1, 1, projection='3d')
        self.ax.set_xlabel('X-Axis')
        self.ax.set_ylabel('Y-Axis')
        self.ax.set_zlabel('Z-Axis')
        self.ax.set_xlim3d(-self.size,self.size);
        self.ax.set_ylim3d(-self.size,self.size);
        self.ax.set_zlim3d(-self.size,self.size);
        self.sc = self.ax.scatter(x,y,z)
        fig.canvas.draw()

    def plotdata(self,t):
        namex = '../frames10/' + 'x' + '0'*(4-len(str(t))) + str(t) + '.npy'
        namey = '../frames10/' + 'y' + '0'*(4-len(str(t))) + str(t) + '.npy'
        namez = '../frames10/' + 'z' + '0'*(4-len(str(t))) + str(t) + '.npy'

        x = np.load(namex)
        y = np.load(namey)
        z = np.load(namez)
        self.sc.remove()
        self.sc = self.ax.scatter(x, y, z,'ro')

        name = '../frames11/' + '0'*(4-len(str(t))) + str(t) + '.png'
        plt.savefig(name)
        print name

    def loopplot(self):
        for t in range(int(self.total_time/self.dtime+1)/10):
            self.plotdata(t)
        plt.close()

def main():
    plott = plotter()
    plott.loopplot()


if __name__ == "__main__":
    main()






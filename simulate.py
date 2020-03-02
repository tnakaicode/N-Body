from pointmassSim7 import Mass
from plotdata import plotter
import random as rand
import numpy as np


class simulator(object):
    def __init__(self):
        # Constants
        self.masses = 30  # number of masses
        rand.seed(86)  # make results somewhat consistant
        self.dtime = 0.2  # resolution for time interval
        self.total_time = 1000.0  # "length of time" simulaiton will run for
        # number of cycles checked
        self.iterations = int(self.total_time / self.dtime)
        self.size = 1000
        # Generate objects
        self.objlist = [Mass(i, self.masses) for i in range(
            self.masses)]  # Create a list of point masses

    def set_masses(self, new_masses):
        self.mass = new_masses
        self.objlist = [Mass(i, self.masses) for i in range(self.masses)]

    def set_dtime(self, new_dtime):
        self.dtime = new_dtime
        # number of cycles checked
        self.iterations = int(self.total_time / self.dtime)

    def set_total_time(self, new_total_time):
        self.total_time = new_total_time
        # number of cycles checked
        self.iterations = int(self.total_time / self.dtime)

    def set_size(self, new_size):
        self.size = new_size

    def gen_config_file(self):
        DATA = np.array(["masses", self.masses, "total_time",
                         self.total_time, "dtime", self.dtime, "size", self.size])
        DATA_FILE = './tmp/SIMULATION_SPEC.npy'
        np.save(DATA_FILE, DATA)

    def initalize_vectors(self):
        # Use objects
        for i in range(self.masses):  # Give initial conditions
            # Calculate initial Acceleration
            self.objlist[i].CalcAccel(self.objlist)
            self.objlist[i].InitVelo()  # Calculate initial Velocity

    def run_calcs(self):
        #fig = plt.figure(figsize=(12,6))
        x = np.zeros(self.masses)
        y = np.zeros(self.masses)
        z = np.zeros(self.masses)
        times = []
        for t in range(self.iterations):
            KEsum = 0
            UEsum = 0

            for i in range(self.masses):  # find Caracteristics for each particle
                self.objlist[i].CalcPos(self.dtime)  # calculate position
                # calculate acceleration
                self.objlist[i].CalcAccel(self.objlist)
                self.objlist[i].CalcVelo(self.dtime)  # calculate velocity

                # Add position values to array
                if t % 10 == 0:
                    x[i] = self.objlist[i].position[0]  # update x position
                    y[i] = self.objlist[i].position[1]  # update y position
                    z[i] = self.objlist[i].position[2]  # update z position

            # saving each data point
            if t % 10 == 0:
                namex = './tmp/' + 'x' + '0' * \
                    (4 - len(str(t / 10))) + str(t / 10) + '.npy'
                namey = './tmp/' + 'y' + '0' * \
                    (4 - len(str(t / 10))) + str(t / 10) + '.npy'
                namez = './tmp/' + 'z' + '0' * \
                    (4 - len(str(t / 10))) + str(t / 10) + '.npy'
                np.save(namex, x)
                np.save(namey, y)
                np.save(namez, z)

    def plot(self):
        plott = plotter()
        plott.setdata(self.masses, self.total_time, self.dtime, self.size)
        plott.loopplot()


def main():
    sim = simulator()
    sim.gen_config_file()
    sim.initalize_vectors()
    sim.run_calcs()
    sim.plot()


if __name__ == "__main__":
    main()

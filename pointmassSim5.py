print(' ')
import random as rand
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy

# Class MASS framework


class Mass(object):  # Mass template object
    def __init__(self):
        # SET MASS
        # generate mass; random number between 0,10
        self.mass = rand.uniform(1, 10)
        # SET POSITION
        posit = 150
        # generate X position; random number between 0,1
        self.Xposition = rand.uniform(-posit, posit)
        # generate Y position; random number between 0,1
        self.Yposition = rand.uniform(-posit, posit)
        # generate Z position; random number between 0,1
        self.Zposition = rand.uniform(-posit, posit)

    def CalcAccel(self):  # CALCULATE ACCERATION DUE TO OTHER OBJECTS
        self.Xacceleration = 0
        self.Yacceleration = 0
        self.Zacceleration = 0
        self.UE = 0
        # go through each objec to find accel from that object
        for massindex in range(masses):
            self.totalaccel = 0
            nam = objlist[massindex]  # find object
            if nam.mass != self.mass:
                # find the difference in the X positions
                Xdiff = nam.Xposition - self.Xposition
                # find the difference in the Y positions
                Ydiff = nam.Yposition - self.Yposition
                Zdiff = nam.Zposition - self.Zposition
                # find the radial distance to other particle
                radius = math.sqrt((Xdiff)**2 + (Ydiff)**2 + (Zdiff)**2)
                if radius > .7:
                    # find the total amount of acceleration
                    self.totalaccel = nam.mass / (radius**2)
                self.Xacceleration += self.totalaccel * Xdiff / \
                    (radius)  # Calculate acceleration in x-direction
                self.Yacceleration += self.totalaccel * Ydiff / \
                    (radius)  # Calculate acceleration in y-direction
                self.Zacceleration += self.totalaccel * Zdiff / \
                    (radius)  # Calculate acceleration in z-direction

                self.UE = self.UE - self.totalaccel * radius * self.mass

    def InitVelo(self):
        # calculate the distance away from center if in xy plane
        xyrad = math.sqrt(self.Xposition**2 + self.Yposition**2)
        if self.Yacceleration > 0:
            # calculate the direction of the velocity vector if perp to the radial vector in xy plane
            vdirect = -(self.Xacceleration / self.Yacceleration)
        else:
            vdirect = 0
        # calculate velocity needed given radius and acceleration (v**2/r = a)
        totalvelocity = math.sqrt(xyrad * self.totalaccel)

        # SET VELOCITY
        # velo in x direction given by total velo/ (slope^2+1)
        self.Xvelocity = totalvelocity / (math.sqrt(vdirect**2 + 1))
        # use slope to calculate velo in y direction
        self.Yvelocity = self.Xvelocity * vdirect
        # give a random z componenet (gaussian distribution)
        self.Zvelocity = rand.gauss(0, .05)
        # SET ACCELERATION

    def CalcVelo(self, Xaccel, Yaccel, Zaccel):  # CALCULATE CHANGE IN VELOCITY
        Xac = Xaccel
        Yac = Yaccel
        Zac = Zaccel
        self.Xvelocity = self.Xvelocity + Xac * dtime  # vf = vi + At
        self.Yvelocity = self.Yvelocity + Yac * dtime
        self.Zvelocity = self.Zvelocity + Zac * dtime

    # CALCULATE CHANGE IN POSITION
    def CalcPos(self, Xvelocity, Yvelocity, Zvelocity, Xacceleration, Yacceleration, Zacceleration):
        Xac = Xacceleration
        Yac = Yacceleration
        Zac = Zacceleration
        Xvelo = Xvelocity
        Yvelo = Yvelocity
        Zvelo = Zvelocity
        self.Xposition = self.Xposition + Xvelo * dtime + \
            (dtime**2) * (Xac) / 2  # Xf = Xi + Vt + .5at^2
        self.Yposition = self.Yposition + \
            Yvelo * dtime + (dtime**2) * (Yac) / 2
        self.Zposition = self.Zposition + \
            Zvelo * dtime + (dtime**2) * (Zac) / 2

    # reverse velocity if position exceeds boundries
    def CheckBoundries(self, Xposition, Yposition, Zposition):
        if Xposition > 12 or Xposition < -12:
            self.Xvelocity = -self.Xvelocity
        if Yposition > 12 or Yposition < -12:
            self.Yvelocity = -self.Yvelocity
        if Zposition > 12 or Zposition < -12:
            self.Zvelocity = -self.Zvelocity

    def calcKE(self):
        v = (self.Xvelocity**2) + (self.Yvelocity**2) + (self.Zvelocity**2)
        KE = .5 * self.mass * v
        return KE


# Constants
masses = 200  # number of masses
rand.seed(9871)  # make results somewhat consistant
dtime = .2  # resolution for time interval
total_time = 1000.0  # "length of time" simulaiton will run for
iterations = int(total_time / dtime)  # number of cycles checked

# Generate objects
objlist = [Mass() for i in range(masses)]  # Create a list of point masses

# Use objects
for i in range(masses):  # Give initial conditions
    objlist[i].CalcAccel()  # Calculate initial Acceleration
    objlist[i].InitVelo()  # Calculate initial Velocity

fig = plt.figure(figsize=(12, 6))
KE = []
UE = []
for t in range(iterations):
    x = []
    y = []
    z = []
    KEsum = 0
    UEsum = 0

    for i in range(masses):  # find Caracteristics for each particle
        objlist[i].CalcPos(objlist[i].Xvelocity, objlist[i].Yvelocity, objlist[i].Zvelocity,
                           objlist[i].Xacceleration, objlist[i].Yacceleration, objlist[i].Zacceleration)  # calculate position
        objlist[i].CalcAccel()  # calculate acceleration

        objlist[i].CalcVelo(objlist[i].Xacceleration, objlist[i].Yacceleration,
                            objlist[i].Zacceleration)  # calculate velocity
#        objlist[i].CheckBoundries(objlist[i].Xposition,objlist[i].Yposition,objlist[i].Zposition)

        # Add position values to array
        x.append(objlist[i].Xposition)  # update x position
        y.append(objlist[i].Yposition)  # update y position
        z.append(objlist[i].Zposition)  # update z position
        if t % 10 == 0:
            KEsum = KEsum + objlist[i].calcKE()
            UEsum = UEsum + objlist[i].UE

    # plotting each data point
    if t % 10 == 0:
        KE.append(KEsum)
        print(KEsum)
        UE.append(UEsum / 2)
        times = range(0, t + 1, 10)
        # print(len(times))
        # print(KE)

        #fig = plt.figure(figsize=(6,6))
        ax = fig.add_subplot(1, 2, 1, projection='3d')
        ax.scatter(x, y, z, 'ro')
        ax.view_init(elev=45, azim=(t % 2) * 5 + 45)
        ax.set_xlabel('X-Axis')
        ax.set_ylabel('Y-Axis')
        ax.set_zlabel('Z-Axis')
        size = 1000
        ax.set_xlim3d(-size, size)
        ax.set_ylim3d(-size, size)
        ax.set_zlim3d(-size, size)

        ax1 = fig.add_subplot(1, 2, 2)
        line = ax1.plot(times, KE, 'r-', times, UE, 'b-', times,
                        [x + y for x, y in zip(KE, UE)], 'g-')
        # ax1.axis([0,iterations,0,1000])
        # ax1.plot()

        name = 'frames7/' + '0' * (4 - len(str(t / 10))) + str(t / 10) + '.png'
        plt.savefig(name)
        # plt.show()

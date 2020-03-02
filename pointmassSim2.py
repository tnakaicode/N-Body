print(' ')
import random as rand
import matplotlib.pyplot as plt
import math
masses = 20  # number of masses
rand.seed(215)
dtime = .2
total_time = 100.0
iterations = int(total_time / dtime)

# Class MASS framework


class Mass(object):  # Mass template object
    def __init__(self, name):
        self.name = name  # give name to object (index)
        # generate X position random number between 0,1
        self.Xposition = rand.uniform(-10, 10)
        # generate Y position random number between 0,1
        self.Yposition = rand.uniform(-10, 10)
        # generate mass random number between 0,1
        self.mass = rand.uniform(1, 10)
        self.Xvelocity = 0.0
        self.Yvelocity = 0.0
        self.Xacceleration = 0.0
        self.Yacceleration = 0.0

    def CalcAccel(self):  # calculate accel on object
        # go through each objec to find accel from that object
        for massindex in range(masses):
            Xdirect = 1  # direction starts at 1 (positive direction)
            Ydirect = 1
            nam = objlist[massindex]  # find object
            Xdiff = nam.Xposition - self.Xposition
            Ydiff = nam.Yposition - self.Yposition
            # find the distance to the other particle
            radius = math.sqrt((Xdiff)**2 + (Ydiff)**2)
            if radius != 0:  # only continue if there is a difference in radius
                totalaccel = nam.mass / (radius**2)
                self.Xacceleration = totalaccel * Xdiff / \
                    (radius)  # create Xacceleration
                self.Yacceleration = totalaccel * Ydiff / \
                    (radius)  # create Xacceleration

    def CalcVelo(self, Xaccel, Yaccel):
        Xac = Xaccel
        Yac = Yaccel
        self.Xvelocity = self.Xvelocity + Xac * dtime
        self.Yvelocity = self.Yvelocity + Yac * dtime

    def CalcPos(self, Xvelocity, Yvelocity, Xacceleration, Yacceleration):
        Xac = Xacceleration
        Yac = Yacceleration
        Xvelo = Xvelocity
        Yvelo = Yvelocity
        self.Xposition = self.Xposition + Xvelo * dtime + dtime * (Xac**2) / 2
        self.Yposition = self.Yposition + Yvelo * dtime + dtime * (Yac**2) / 2

# Generate objects


objlist = [Mass(i) for i in range(masses)]  # Create a list of point masses

# Use objects
for t in range(iterations):
    x = []
    y = []
    for i in range(masses):  # find Caracteristics for each particle
        #		print ' '
        #		print 'name index:' + str(objlist[i].name)  #print out index name of

        objlist[i].CalcAccel()  # calculate acceleration
#		print 'accel:' + str(objlist[i].acceleration)

#		objlist[i].position #display old position
#		print 'oldpos' + str(objlist[i].position)

        objlist[i].CalcPos(objlist[i].Xvelocity, objlist[i].Yvelocity,
                           objlist[i].Xacceleration, objlist[i].Yacceleration)  # calculate position
#		print 'newpos:' + str(objlist[i].position)

        objlist[i].CalcVelo(objlist[i].Xacceleration,
                            objlist[i].Yacceleration)  # calculate velocity
#		print 'velo:' + str(objlist[i].velocity)
        x.append(objlist[i].Xposition)
        y.append(objlist[i].Yposition)

    plt.figure(t + 1)
    plt.plot(x, y, 'ro')
    plt.axis([-12, 12, -12, 12])
    name = 'zsimimage' + str(t) + '.png'
    plt.savefig(name)
#	plt.show()

print(' ')
import random as rand
import math
import numpy as np

## Class MASS framework
class Mass(object): #Mass template object
    def __init__(self, i, masses, dtime):
        self.numb_masses = masses
        self.id = i
        self.dtime = dtime
        # SET MASS
        if (i==0):
            self.mass = 100#rand.uniform(100,1000) #generate mass; random number between 0,10
        elif (i==1):
            self.mass = 50
        elif (i==2):
            self.mass = 1
        else:
            self.mass = rand.uniform(100,1000)

        # SET POSITION
        posit = 400 #range of possible r0
        self.position = np.random.uniform(-posit,posit,3)  #generate X position; random number between 0,1

    def CalcAccel(self, objlist):   #CALCULATE ACCERATION DUE TO OTHER OBJECTS
        self.acceleration = np.array([0.,0.,0.])
        self.UE = 0
        for massindex in range(self.numb_masses):  #go through each objec to find accel from that object
            self.totalaccel = 0
            nam = objlist[massindex]  #find object
            if nam.id != self.id:
                diff = nam.position - self.position
                radius = np.linalg.norm(diff) #find the difference in the X positions
                preradius = radius**2
                epsilon = 1.2 #softening factor
                self.totalaccel = nam.mass/(preradius + epsilon) #find the total amount of acceleration
                self.acceleration +=  self.totalaccel*diff/radius # Calculate acceleration in x-direction
                self.UE = self.UE - self.totalaccel*radius*self.mass       

    def InitVelo(self):
        xyrad = math.sqrt(self.position[0]**2 + self.position[1]**2) #calculate the distance away from center if in xy plane
        totalvelocity = math.sqrt(xyrad*self.totalaccel) #calculate velocity needed given radius and acceleration (v**2/r = a)
        self.velocity = np.array([rand.uniform(0,1),rand.uniform(0,1), rand.gauss(0,.05)])#totalvelocity*self.Yposition/(xyrad) #velo in x direction given by total velo/ (slope^2+1)

    def CalcVelo(self): #CALCULATE CHANGE IN VELOCITY
        self.velocity = self.velocity + self.acceleration*self.dtime # vf = vi + At

    def CalcPos(self): #CALCULATE CHANGE IN POSITION
        self.position = self.position + self.velocity*self.dtime + (self.dtime**2)*(self.acceleration)/2 #Xf = Xi + Vt + .5at^2

    def calcKE(self):
        v = np.linalg.norm(self.velocity)
        KE = .5*self.mass*v
        return KE
print(' ')
import random as rand
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d.axes3d import Axes3D

masses = 200  #number of masses
rand.seed(3242)
dtime = .2
total_time = 1000.0
iterations = int(total_time/dtime)

## Class MASS framework
class Mass(object): #Mass template object
    def __init__(self, name):
        self.name = name         #give name to object (index)

        # SET MASS
        self.mass = rand.uniform(1,10) #generate mass random number between 0,1
    def SumMass(self):
        totalMass = 0
        for obj in range(masses):
            nam = objlist[obj]
            totalMass = totalMass + nam.mass
    def GetData(self):
        # SET POSITION
        self.Xposition = rand.uniform(-100,100)  #generate X position random number between 0,1
        self.Yposition = rand.uniform(-100,100)  #generate Y position random number between 0,1
        self.Zposition = rand.uniform(-100,100)  #generate Z position random number between 0,1

        xyrad = math.sqrt(self.Xposition**2 + self.Yposition**2)
        vdirect = -(self.Xposition/self.Yposition)
        # SET VELOCITY
        self.Xvelocity = rand.gauss(0,.1) + (self.Yposition/10)**2
        self.Yvelocity = rand.gauss(0,.1) + (self.Xposition/10)**2
        self.Zvelocity = rand.gauss(0,.1)
        # SET ACCELERATION
        self.Xacceleration =0.0
        self.Yacceleration =0.0
        self.Zacceleration =0.0

    def CalcAccel(self):   #CALCULATE ACCERATION DUE TO OTHER OBJECTS
        for massindex in range(masses):  #go through each objec to find accel from that object
            nam = objlist[massindex]  #find object
            Xdiff = nam.Xposition - self.Xposition #find the difference in the X positions
            Ydiff = nam.Yposition - self.Yposition #find the difference in the Y positions
            Zdiff = nam.Zposition - self.Zposition
            radius = math.sqrt((Xdiff)**2 + (Ydiff)**2 + (Zdiff)**2)  #find the radial distance to other particle
            if radius > .7:        #only continue if there is a difference in radius
                totalaccel = nam.mass/(radius**2) #find the total amount of acceleration
                self.Xacceleration =  totalaccel*Xdiff/(radius) # Calculate acceleration in x-direction
                self.Yacceleration =  totalaccel*Ydiff/(radius) # Calculate acceleration in y-direction
                self.Zacceleration =  totalaccel*Zdiff/(radius) # Calculate acceleration in z-direction

    def CalcVelo(self,Xaccel,Yaccel,Zaccel): #CALCULATE CHANGE IN VELOCITY
        Xac = Xaccel
        Yac = Yaccel
        Zac = Zaccel
        self.Xvelocity = self.Xvelocity + Xac*dtime
        self.Yvelocity = self.Yvelocity + Yac*dtime
        self.Zvelocity = self.Zvelocity + Zac*dtime

    def CalcPos(self,Xvelocity,Yvelocity,Zvelocity,Xacceleration,Yacceleration,Zacceleration): #CALCULATE CHANGE IN POSITION
        Xac = Xacceleration
        Yac = Yacceleration
        Zac = Zacceleration
        Xvelo = Xvelocity
        Yvelo = Yvelocity
        Zvelo = Zvelocity
        self.Xposition = self.Xposition + Xvelo*dtime + (dtime**2)*(Xac)/2
        self.Yposition = self.Yposition + Yvelo*dtime + (dtime**2)*(Yac)/2
        self.Zposition = self.Zposition + Zvelo*dtime + (dtime**2)*(Zac)/2
    def CheckBoundries(self, Xposition,Yposition,Zposition):
        if Xposition > 12 or Xposition <-12:
            self.Xvelocity = -self.Xvelocity
        if Yposition > 12 or Yposition <-12:
            self.Yvelocity = -self.Yvelocity            
        if Zposition > 12 or Zposition <-12:
            self.Zvelocity = -self.Zvelocity

## Generate objects

objlist = [Mass(i) for i in range(masses)] # Create a list of point masses

## Use objects
t = 0
for t in range(iterations):
    x = []
    y = []
    z = []
    for i in range(masses):   #find Caracteristics for each particle
        objlist[i].CalcAccel()  #calculate acceleration
        objlist[i].CalcPos(objlist[i].Xvelocity,objlist[i].Yvelocity, objlist[i].Zvelocity, objlist[i].Xacceleration, objlist[i].Yacceleration, objlist[i].Zacceleration)  #calculate position
        objlist[i].CalcVelo(objlist[i].Xacceleration,objlist[i].Yacceleration,objlist[i].Zacceleration) #calculate velocity
#        objlist[i].CheckBoundries(objlist[i].Xposition,objlist[i].Yposition,objlist[i].Zposition)
        x.append(objlist[i].Xposition) #update x position
        y.append(objlist[i].Yposition) #update y position
        z.append(objlist[i].Zposition) #update z position
    if t%10 == 0:
        fig = plt.figure(figsize=(6,6))
        ax=fig.add_subplot(1, 1, 1, projection='3d')
        plt.plot(x, y, z,'ro')
#    plt.axis([-12,12,-12,12])
        ax.set_xlim3d(-100,100);
        ax.set_ylim3d(-100,100);
        ax.set_zlim3d(-100,100);
        name = '200circSim' + str(t) + '.png'
        plt.savefig(name)



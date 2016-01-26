from pointmassSim7 import Mass
from plotdata import plotter
import random as rand
import numpy as np

#Constants
masses = 30  #number of masses
rand.seed(86) #make results somewhat consistant
dtime = .2 #resolution for time interval
total_time = 1000.0 # "length of time" simulaiton will run for
iterations = int(total_time/dtime) #number of cycles checked
size = 1000
DATA = np.array(["masses", masses, "total_time", total_time,"dtime",dtime,"size",size])
DATA_FILE = '../frames10/SIMULATION_SPEC.npy'
np.save(DATA_FILE,DATA)

## Generate objects
objlist = [Mass(i,masses,dtime) for i in range(masses)] # Create a list of point masses

## Use objects
for i in range(masses): #Give initial conditions
    objlist[i].CalcAccel(objlist) #Calculate initial Acceleration
    objlist[i].InitVelo() #Calculate initial Velocity

#fig = plt.figure(figsize=(12,6))
x = np.zeros(masses)
y = np.zeros(masses)
z = np.zeros(masses)
times = []
for t in range(iterations):

    KEsum = 0
    UEsum = 0

    for i in range(masses):   #find Caracteristics for each particle
        objlist[i].CalcPos()  #calculate position
        objlist[i].CalcAccel(objlist)  #calculate acceleration
        objlist[i].CalcVelo() #calculate velocity

        # Add position values to array
        if t%10 == 0:
            x[i] = objlist[i].position[0] #update x position
            y[i] = objlist[i].position[1] #update y position
            z[i] = objlist[i].position[2] #update z position

    #saving each data point
    if t%10 == 0:
        namex = '../frames10/' + 'x' + '0'*(4-len(str(t/10))) + str(t/10) + '.npy'
        namey = '../frames10/' + 'y' + '0'*(4-len(str(t/10))) + str(t/10) + '.npy'
        namez = '../frames10/' + 'z' + '0'*(4-len(str(t/10))) + str(t/10) + '.npy'
        np.save(namex, x)
        np.save(namey, y)
        np.save(namez, z)

plott = plotter()
plott.setdata(masses,total_time,dtime,size)
plott.loopplot()

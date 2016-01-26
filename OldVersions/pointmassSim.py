print(' ')
import random as rand
import matplotlib.pyplot as plt
masses = 20  #number of masses
rand.seed(215)
dtime = .2
total_time = 20.0
iterations = int(total_time/dtime)

## Class MASS framework
class Mass(object): #Mass template object
    def __init__(self, name):
    	self.name = name         #give name to object (index)
    	self.position = rand.uniform(-10,10)  #generate position random number between 0,1
    	self.mass = rand.uniform(1,10) #generate mass random number between 0,1
    	self.velocity = 0.0
    	self.acceleration =0.0
    def CalcAccel(self): #calculate accel on object
    	for massindex in range(masses):  #go through each objec to find accel from that object
    		direct = 1        #direction starts at 1 (positive direction)
    		nam = objlist[massindex]  #find object
    		radius = nam.position - self.position  #find the distance to the other particle
    		if radius != 0:        #only continue if there is a difference in radius
	    		if radius < 0:     #assign appropriate direction
    				direct = -1    #negitive dirction
    			elif radius >0:    #if positive
    				direct = 1     #positive direction
    			self.acceleration = direct*nam.mass/(radius**2)  #add new accel vector to previous sum of accels
    	self.acceleration = self.acceleration/10           #finally return the total accel
    def CalcVelo(self,accel):
    	ac = accel
    	self.velocity = self.velocity + ac*dtime
    def CalcPos(self,velocity,acceleration):
    	ac = acceleration
    	velo = velocity
    	firstpos = self.position
    	self.position = self.position + velo*dtime + dtime*(ac**2)/2

## Generate objects

objlist = [Mass(i) for i in range(masses)] # Create a list of point masses

## Use objects
for t in range(iterations):
	x = []
	y = []
	for i in range(masses):   #find Caracteristics for each particle
#		print ' '
#		print 'name index:' + str(objlist[i].name)  #print out index name of 

		objlist[i].CalcAccel()  #calculate acceleration
#		print 'accel:' + str(objlist[i].acceleration)

		objlist[i].position #display old position
#		print 'oldpos' + str(objlist[i].position)

		objlist[i].CalcPos(objlist[i].velocity,objlist[i].acceleration)  #calculate position
#		print 'newpos:' + str(objlist[i].position)

		objlist[i].CalcVelo(objlist[i].acceleration) #calculate velocity
#		print 'velo:' + str(objlist[i].velocity)
		x.append(objlist[i].position)
		y.append(0)

	plt.figure(t+1)
	plt.plot(x, y, 'ro')
	plt.axis([-12,12,-1,1])
	name = 'zsimimage' + str(t) + '.png'
	plt.savefig(name)
#	plt.show()











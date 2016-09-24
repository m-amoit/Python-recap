from swampy.TurtleWorld import *
import math

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)

'''RE FACTORING: Rearranging a program to improve 
function interfaces and facilitate code reuse'''

def polyline(t, n, length, angle):
	'''Generalizing polygon to take an angle as a 
	third argument'''
	for i in range(n):
		fd(t, length)
		lt(t, angle) 
		t.delay = 0.001

def polygon(t, n, length):
	'''Re writing polygon to use polyline'''
	angle = 360.0 / n
	polyline(t, n, length, angle)

def arc(t, r, angle):
	'''Re writing arc to use polyline'''
	arc_length = 2 * math.pi * r * angle/360
	n = int(arc_length / 3) + 1
	step_length = arc_length/n
	step_angle = float(angle)/n
	polyline(t, n, step_length, step_angle)

def circle(t, r):
	'''Re writing circle to use arc'''
	arc(t, r, angle=360)

# if __name__=='__main__':
# 	'''Checks whether we are running as a 
# 	script, in which case we run the test 
# 	code, or being imported, in which case 
# 	we don't'''
	
# 	world = TurtleWorld()

# 	bob = Turtle()
# 	bob.delay = 0.001

# 	radius = 100
# 	pu(bob)
# 	fd(bob, radius)
# 	lt(bob)
# 	pd(bob)
# 	circle(bob, radius)

# 	wait_for_user()
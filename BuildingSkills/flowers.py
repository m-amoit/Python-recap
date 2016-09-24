from swampy.TurtleWorld import *
from mypolygon import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001

def petal(t, r, angle):
	'''
	draw a single petal using 2 arcs
	t: turtle 
	r: radius of arc
	angle: angle that subtends the arc
	'''
	for i in range(2):
		arc(t, r, angle)
		lt(t, 180-angle)

def flower(t, n, r, angle):
	'''
	draw a flower with n petals
	'''
	for i in range(n): 
		petal(t, r, angle)
		lt(t, 360/n)

def move(t, length):
	'''
	Define movement of turtle without leaving trail.
	t: turtle
	length: distance the turtle moves
	pu: pen up (inactive)
	pd: pen down (active)
	'''
	pu(t)
	fd(t, length)
	pd(t)

move(bob, -100)
flower(bob, 10, 140, 45)

move(bob, 200)
flower(bob, 24, 140, 45)

move(bob, 200)
flower(bob, 21, 180, 27)

die(bob)

wait_for_user()

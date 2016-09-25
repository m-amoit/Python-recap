from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def koch(t, x):
	'''
	Takes turtle and length (x) as parameters and 
	uses the turtle to draw a koch curve with the 
	given length
	'''
	if x<3:
		fd(t, x)
		return
	angle = 60
	m = x/3
	fd(t, m)
	lt(t, angle)
	koch(t, m)
	rt(t, 2*angle)
	koch(t, m)
	lt(t, angle)
	koch(t, m)

def snowflake(t, x):
	'''
	Draws three koch curves to make the outline of
	a snowflake
	'''
	angle = 120
	for i in range(3):
		koch(t, x)
		rt(t, angle)

snowflake(bob, 600)
die(bob)

wait_for_user()

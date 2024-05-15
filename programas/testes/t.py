
import turtle
import math

bob = turtle.Turtle()

'''
def square(t,lenght):
	print(t)
	for _ in range(4):
		t.fd(lenght)
		t.lt(90)
		turtle.mainloop


def polygon(t,lenght,sides):
	print(t)
	for _ in range(sides):
		angle = 360/sides
		t.fd(lenght)
		t.lt(angle)
		turtle.mainloop

def circle(t,ratio,arc):
	print(t)
	sides=1100 #troquei sides por 1100
	angle=360/sides
	for _ in range(round(arc/angle)):  	
		t.fd(2*ratio*( (1-math.cos(angle)) / (1+math.cos(angle)) )**(0.5))
		t.lt(angle)
		turtle.mainloop

#circle(bob,0.8,720)
'''

def parametric(x):
	print(x)
	t0 = 0
	tf = 1000
	dt = 0.0001
	t = t0
	while t <= tf:
		t += dt
		
		distance = dt*(9 * math.sin(t)**2 + 4 * math.cos(t)**2)**(0.5)
		radianos = math.atan( (2*math.cos(t)) / (-3*math.sin(t)) ) - math.atan(( (-2)*math.sin(t) + dt*(2*math.cos(t)) )/( (-3)*math.cos(t) + dt*(-3)*math.sin(t) ) )
		angle = radianos*(180) / (math.pi)

		x.fd(distance)
		
		if angle >= 0:
			x.rt(angle)
		else:
			x.lt(angle)


parametric(bob)


turtle.Terminator


'''
	t0 =
	tf =
	dt =
	for t in range(t0,tf+1,dt):
'''
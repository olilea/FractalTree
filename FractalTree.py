import turtle
import math
import random

class FractalTree():

	def __init__(self):
		self.setup()
		window.exitonclick()
	
	def setup(self):
		self.drawTree(5, 100, 0, -200, 0)
		
	def drawTree(self, n, length, x, y, prevAngle):
		if n == 0:
			return
		if (n > 0) and (james.pensize() >= 1):
			james.pensize(james.pensize() - 0.5)
		
		
		james.setpos(x, y)
		
		james.pd()
		
		angle1 = prevAngle + random.randrange(20, 40)
		angle2 = prevAngle - random.randrange(20, 40)
		
		james.setheading(angle1)
		
		james.forward(length)
		x1 = james.pos()[0]
		y1 = james.pos()[1]
		
		if n == 1:
			james.dot(5, "green")
		
		james.backward(length)
		james.setheading(angle2)
		
		james.forward(length)
		x2 = james.pos()[0]
		y2 = james.pos()[1]
		
		if n == 1:
			james.dot(5, "green")
		
		james.pu()
		self.drawTree(n - 1, random.uniform(0.75,0.9)*length, x1, y1, angle1)
		self.drawTree(n - 1, random.uniform(0.75,0.9)*length, x2, y2, angle2)
		
    
window = turtle.Screen()

james = turtle.Turtle()

turtle.mode("logo")

james.speed(10)
james.color("blue")
james.pensize(6)

james.pu()
james.backward(300)
james.pd()
james.forward(100)
james.pu()

tree = FractalTree()
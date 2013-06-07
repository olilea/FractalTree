import turtle
import math
import random

class FractalTree():

	def __init__(self):
		self.setup()
		window.exitonclick()
	
	def setup(self):
		self.drawTree(2, 65.0, 0, 0, 30)
		self.drawTree(5, 65.0, 0, 0, 30)
		
	def drawTree(self, n, length, x, y, prevAngle):
		if n == 0:
			return
		
		james.setpos(x, y)
		
		james.pd()
		
		angle1 = prevAngle + 30
		angle2 = prevAngle - 30
		
		james.setheading(angle1)
		
		james.forward(length)
		x1 = james.pos()[0]
		y1 = james.pos()[1]
		
		james.backward(length)
		james.setheading(angle2)
		
		james.forward(length)
		x2 = james.pos()[0]
		y2 = james.pos()[1]
		
		james.pu()
		self.drawTree(n - 1, length * 0.65, x1, y1, angle1)
		self.drawTree(n - 1, length * 0.65, x2, y2, angle2)
		
    
window = turtle.Screen()

james = turtle.Turtle()

turtle.mode("logo")

james.speed(10)
james.color("blue")

james.pu()
james.backward(100)
james.pd()
james.forward(100)
james.pu()


tree = FractalTree()
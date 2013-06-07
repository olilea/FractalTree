import turtle
import math
import random

class FractalTree():

	def __init__(self):
		self.setup()
		window.exitonclick()
	
	def setup(self):
		james.pu()
		alice.pu()
		james.speed(10)
		alice.speed(10)
		james.pencolor("blue")
		alice.pencolor("blue")
		james.setpos(0, -100)
		james.pd()
		james.setpos(0, 0)
		james.pu()
		self.drawTree(6, 65.0, 0, 0)
		self.drawTree(6, 65.0, 0, 0)
		
	def drawTree(self, n, length, x, y):
		if n == 0:
			return
		
		angle1 = 15
		
		james.setpos(x, y)
		alice.setpos(x, y)
		
		james.pd()
		alice.pd()
		
		james.left(2* angle1)
		james.forward(length)
		alice.right(2* angle1)
		alice.forward(length)
		
		james.pu()
		alice.pu()
		
		length *= 0.65
		n -= 1
		
		x1 = james.pos()[0]
		y1 = james.pos()[1]
		x2 = alice.pos()[0]
		y2 = alice.pos()[1]
		
		self.drawTree(n, length, x1, y1)
		self.drawTree(n, length, x2, y2)
    

#james is the name of the turtle
james = turtle.Turtle()
alice = turtle.Turtle()
window = turtle.Screen()

tree = FractalTree()
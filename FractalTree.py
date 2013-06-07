import turtle
import math
import random

class FractalTree():

	def __init__(self, n):
		turtle.mode("logo")
		james.speed(10)
		james.color("blue")
		james.pensize(10)
		james.pu()
		james.backward(300)
		james.pd()
		james.forward(100)
		james.pu()
		self.drawTree(n, 60, 0, -200, 0, 10)
		window.exitonclick()
		
	def drawTree(self, n, length, x, y, prevAngle, sizeOfPen):
		if n == 0:
			return
		
		james.setpos(x, y)
		james.pensize(sizeOfPen)
		
		if sizeOfPen == 1:
			newPenSize = 1
		else:
			newPenSize = sizeOfPen - 1
		
		james.pd()
		
		angle1 = prevAngle + random.randrange(20, 40)
		angle2 = prevAngle - random.randrange(20, 30)
		
		james.setheading(angle1)
		
		james.forward(length)
		x1 = james.pos()[0]
		y1 = james.pos()[1]
		
		if n == 1:
			james.dot(3, james.pencolor())
			
#		if random.random() <= 0.49:
#			james.color("red")
#		else:
#			james.color("blue")
		
		james.backward(length)
		james.setheading(angle2)
		
		james.forward(length)
		x2 = james.pos()[0]
		y2 = james.pos()[1]
		
		if n == 1:
			james.dot(3, james.pencolor())
		
		james.pu()
		
		self.drawTree(n - 1, random.uniform(0.70, 0.90) * length, x1, y1, angle1, newPenSize)
		self.drawTree(n - 1, random.uniform(0.70, 0.95) * length, x2, y2, angle2, newPenSize)
		
    
window = turtle.Screen()

james = turtle.Turtle()

tree = FractalTree(12)
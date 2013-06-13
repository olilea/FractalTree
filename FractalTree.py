'''
This script recursively creates a tree from the given number of iterations,
using randomisation to produce a more natural looking tree.

Many features of the tree are randomised, such as early termination of the
branch one iteration before the given n iterations, the angle of the branch
in proportion to the context of the angle of the new branch's parent, and
the length of the branch.

When asked, give 14 as the number of iterations to provide an optimal result.
'''

import turtle
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
		james.tracer(200)
		self.drawTree(n, 60, 0, -200, 0, 10)
		window.exitonclick()
		
		
	def drawTree(self, n, length, x, y, prevAngle, sizeOfPen):
	
		if n == 0:						#If the counter is now zero, terminate the branch
			return
		
		james.setpos(x, y)				#Put James at x,y
		james.pensize(sizeOfPen)		#Set the pensize to the new pensize specified by previous recursive call
		
		if sizeOfPen == 1:				
			newPenSize = 1
		else:
			newPenSize = sizeOfPen - 1	#If pensize isn't 1, decrease the pensize
		
		james.pd()
		
		angle1 = prevAngle + random.randrange(20, 40)		#Forms the left branch
		angle2 = prevAngle - random.randrange(20, 40)		#Forms the right branch
		
		james.setheading(angle1)		#Points James in this direction
		
		james.forward(length)
		x1 = james.pos()[0]				#x1 is James's current x coordinate
		y1 = james.pos()[1]				#y1 is James's current y coordinate
		
		if n == 1:
			james.dot(4, "green")		#Each leaf has a green dot as a leaf on the tree
		
		if n == 2:							#50% chance the branch will terminate when n = 2
			if random.random() <= 0.49:
				james.dot(2, "green")
				james.pu()
				return
		
		james.backward(length)			#Repeat the entire process with angle2
		james.setheading(angle2)
		
		james.forward(length)
		x2 = james.pos()[0]
		y2 = james.pos()[1]
		
		if n == 1:
			james.dot(2, "green")
		
		james.pu()
		
		
		#The recursive calls, which also set the new length of the branch randomly
		self.drawTree(n - 1, random.uniform(0.70, 0.95) * length, x1, y1, angle1, newPenSize)
		self.drawTree(n - 1, random.uniform(0.70, 0.95) * length, x2, y2, angle2, newPenSize)
		
    
window = turtle.Screen()

james = turtle.Turtle()

n = input("Please enter the number of iterations? 14 is optimal: ")

tree = FractalTree(n)
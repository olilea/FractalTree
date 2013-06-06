import turtle
import math
import random

class FractalTree():

	def __init__(self, james, window):
		self.setup()
		window.exitonclick()
	
	def setup(self):
		james.left(90)
		james.color("blue")
		james.penup()
		james.backward(150)
		james.pendown()
		self.drawTree(5)
		
	def drawTree(self, n):
		return
    

#james is the name of the turtle
james = turtle.Turtle()
window = turtle.Screen()

tree = FractalTree(james, window)
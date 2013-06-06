import turtle

class FractalTree():

	def __init__(self, james, window):
		self.james = james
		self.window = window
		
		self.setup()
		
		self.drawTree(5)
	
		window.exitonclick()
	
	def setup(self):
		self.getJames().left(90)
		self.getJames().color("blue")
		self.getJames().penup()
		self.getJames().backward(150)
		self.getJames().pendown()
		self.getJames().forward(100)
	
	def getJames(self):
		return self.james
    
	def getWindow(self):
		return self.window
		
	def drawTree(self, n):
		return
    

#james is the name of the turtle
james = turtle.Turtle()
window = turtle.Screen()

tree = FractalTree(james, window)
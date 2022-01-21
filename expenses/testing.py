
class Robot(object)
	"""docstring for ClassName"""
	def __init__(self, d,e,f):
		self.name = d
		self.weight = e
		self.height = f

	def introduce_self():
		print("my name is " self.name )
		print("i'm " self.height " tall and " self.weight fat)

r1 = Robot("tom" 50, 35)
r2 = Robot("jerry", 40, 30)
		




class Person(object):
	"""docstring for ClassName"""
	def __init__(self, a,b,c):
		self.name = a
		self.personality = b
		self.is_sitting = c


	def sit_down(self):
		self.is_sitting = True 
	def stand_up(self):
		self.is_sitting = False 


p1 = Person("tope", "oreoluwa", False)
p2 = Person("femi", "fool", True)

p1.Robot_owned = r2
p2.Robot_owned = r1
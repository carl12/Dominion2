from set import Set

class Card:
	cost = 0
	draw = 0
	action = 0
	buy = 0
	money = 0
	points = 0
	is_action = False
	is_vp = False
	is_treasure= False

	def __init__(self,name):
		self.name=name
		self.game = []
		self.owner=[]
		self.opponents=[]

	def __repr__(self):
		return self.name

	def play(self):
		pass
		#add all respective stuff to owner


class ActionCard(Card):
	is_action = True

class VictoryCard(Card):
	is_vp = True

class Village(ActionCard):
	cost = 3
	draw = 1
	action = 2

class Gardens(VictoryCard):
	cost = 4
	@property
	def cost(self):
		print('calculate garden value')



class Example(object):
     def __init__(self, value):
         self.x = value
     @property
     def x(self):
         print( "I'm the x value!")
         return self._x  # see below
     @x.setter
     def x(self, value):
         if value < 0:
             raise ValueError('x must not be negative')
         self._x = value






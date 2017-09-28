# from set import Set

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
	name = "generic card"

	def __init__(self):
		self.game = []
		self.owner=[]
		self.opponents=[]

	def __repr__(self):
		return self.name

	def play(self):
		print('asdf')
		#add all respective stuff to owner


class ActionCard(Card):
	is_action = True

class VictoryCard(Card):
	is_vp = True

class Village(ActionCard):
	cost = 3
	draw = 1
	action = 2

class Smithy(ActionCard):
	cost = 4
	draw = 3

class Festival(ActionCard):
	cost = 5
	action = 2
	buy = 1
	money = 2

class Laboratory(ActionCard):
	cost = 5
	draw = 2
	action = 1

class Market(ActionCard):
	cost = 5
	draw = 1
	action = 1
	buy = 1
	money = 1

class Woodcutter(ActionCard):
	cost = 3
	actino = 1
	money = 2

class Gardens(VictoryCard):
	cost = 4
	@property
	def cost(self):
		print('calculate garden value')



def attribute_test():
	card = Card()
	smithy = Smithy()
	village = Village()

	print(smithy.action)
	print(smithy.draw)
	print(smithy.money)


# attribute_test()

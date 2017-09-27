from random import shuffle
import copy
class Set:

	def __init__(self, deck=[]):

		self.hand=[]
		self.deck=deck
		self.all=copy.copy(deck)
		self.discard=[]
		self.pending=[]
		self.in_play=[]
		# self.places={'hand':self.hand,'deck':self.deck,'discard':self.discard,'pending':self.pending,'all':self.all}
		self.trash_list = []
		self.token_points=0
		self.shuffle_deck()


	def draw(self, num=1):
		for _ in range(num):
			self.hand.append(self.getTop())

	def getTop(self):
		if len(self.deck) > 0:
			return self.deck.pop()
		else:
			self.reshuffle_discard()
			return self.deck.pop()

	def reshuffle_discard(self):
		self.deck.extend(self.discard)
		self.discard=[]
		self.shuffle_deck()

	def shuffle_deck(self):
		shuffle(self.deck)


	def play_card(self, loc):
		card = hand.pop(loc)
		in_play.append(card)
		# card.play()

	def play_type(card_type):
		for i,card in hand:
			if typeof(card,card_type):
				self.play_card(i)

	def end_turn(self):
		self.discard.extend(self.hand)
		self.discard.extend(self.in_play)
		self.hand=[]
		self.in_play=[]
		self.draw(5)

	def gain(self,card):
		self.discard.append(card)
		self.all.append(card)

	def add_to_hand(self, card):
		self.hand.append(card)
		self.all.append(card)

	def trash(self, place, position):
		var = self.__dict__.get(place)
		if var and type(var) is list and var is not self.trash_list:
			card = var.pop(position)
			self.all.remove(card)
			self.trash_list.append(card)


	def discard(self, loc):
		card = self.hand.pop(loc)
		discard.append(card)

	def calc_points(self):
		sum1 = 0
		sum2 = sum(card.points for card in self.all)
		for card in self.all:
			sum1 +=card.points
		return sum2



def set_test():

	class FakeCard:
		def __init__(self,name):
			self.points = 0
			self.name=name
			self.game = []
			self.owner=[]
			self.opponents=[]

		def __repr__(self):
			return self.name

	c1 = FakeCard("card1")
	c2 = FakeCard("card2")
	c3 = FakeCard("card3")
	c4 = FakeCard("card4")
	c5 = FakeCard("card5")
	c6 = FakeCard("card6")
	c7 = FakeCard("card7")
	c8 = FakeCard("card8")
	c9 = FakeCard("card9")
	c10 = FakeCard("card10")

	start_deck = [c1,c2,c3,c4,c5,c6,c7,c8,c9]

	s = Set(start_deck)
	print(s.__dict__.keys())
	print("Deck after shuffle: ")
	print(s.deck)
	print(s.all)
	s.end_turn()
	print("Hand:")
	print(s.hand)
	print(s.all)
	s.end_turn()
	print("Hand:")
	print(s.hand)
	print(s.all)
	print("----------------------")
	s.end_turn()
	print("Hand:")
	print(s.hand)
	print(s.all)
	s.end_turn()
	print("Hand:")
	print(s.hand)
	print(s.all)
	s.trash('hand',0)
	print(s.hand)
	print(s.all)
	print(s.calc_points())


set_test()

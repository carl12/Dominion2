from playerSet import Set
from card import *
# from manager import *

class Player:

	def __init__(self, manager,store):
		self.manager = []
		self.set = Set()
		self.set.end_turn()
		self.manager = manager
		self.store = store
		self.actions = 0
		self.buys = 0
		self.money = 0
		self.turns = 0

	def do_turn(self):
		self.start_turn()
		self.do_actions()
		self.play_treasures()
		self.buy_cards()
		self.cleanup()	

	def start_turn(self):
		self.actions = 1
		self.buys = 1
		self.money = 0
		self.turns +=1

	def do_actions(self):
		self.manager.do_actions()
		

	def play_treasures(self):
		for card in reversed(self.set.hand):
			if card.is_treasure:
				self.money += card.money
				self.set.play(card.name)

	def buy_cards(self):
		self.manager.buy_cards()
		

	def buy(self,card_type):
		if self.buys > 0:
			cost = card_dict[card_type].cost
			if cost <= self.money:
				card = self.store.take(card_type)
				if card:
					self.money -= cost
					self.buys -= 1
					self.set.gain(card)

					return True




	def cleanup(self):
		self.set.end_turn()
		self.actions = 0
		self.buys = 0
		self.money = 0

	def get_hand(self):
		return self.set.hand

	def get_points(self):
		return self.set.calc_points()

	def play(self, name):
		return self.set.play(name)

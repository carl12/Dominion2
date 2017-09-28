from playerSet import Set
from card import *
class Player:

	def __init__(self):
		self.manager = []
		self.set = Set()
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
		# self.manager.do_actions()
		pass

	def play_treasures(self):
		for i,card in set.hand:
			if card is TreasureCard:
				self.money += card.money
				self.set.play(card)

	def buy_cards(self):
		# self.manager.buy_cars()
		pass

	def buy(card_type):
		if self.buys > 0 and card_type.cost < money:
			if store.take(card_type):
				self.money -= card_type.cost
				self.buys -= 1
				return self.buys

	def cleanup(self):
		self.set.end_turn()
		self.actions = 0
		self.buys = 0
		self.money = 0

	def get_points(self):
		return self.set.calc_points()


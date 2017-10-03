from card import *
class Store:

	def __init__(self, num_players=2):
		if num_players > 2:
			VPnum = 12
		else:
			VPnum = 8
		self.kingdom_cards = {'Smithy','Village','Festival',
		'Laboratory','Market','Woodcutter'}
		self.baseVPs = {'Curse','Estate','Duchy','Province'}
		self.baseTreasure = {'Copper','Silver','Gold'}
		self.remain = {card:10 for card in self.kingdom_cards}
		self.remain.update({card:VPnum for card in self.baseVPs})
		self.remain.update({card:100 for card in self.baseTreasure})
		self.empty_piles = 0

	def take(self, str):
		print('trying to take ',str)
		cards_left = self.remain.get(str)
		if cards_left and cards_left > 0:
			self.remain[str]-= 1
			if self.remain[str] == 0:
				self.empty_piles += 1
			card = globals()[str]()
			print(globals()[str])
			print(card)
			return card

	def is_game_over(self):
		return self.empty_piles >= 3 or self.remain['Province']== 0




def store_test():
	s = Store()
	print(s.take("Smithy"))
	print(s.remain)

# store_test()



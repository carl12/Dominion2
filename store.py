from card import *
class Store:
	super_classes = ('Card','ActionCard','VictoryCard')
	g = globals().copy()
	available_cards = []
	for key, vals in g.items():
		if type(vals) is type and key not in super_classes:
			available_cards.append(key)
	# print(available_cards)


	def __init__(self):
		self.kingdom_cards = {'Smithy','Village','Festival',
		'Laboratory','Market','Woodcutter'}
		self.baseVPs = {'Curse','Estate','Duchy','Province'}
		self.baseTreasure = {'Copper','Silver','Gold'}
		self.remain = {card:10 for card in self.kingdom_cards}
		self.remain.update({card:8 for card in self.baseVPs})
		self.remain.update({card:100 for card in self.baseTreasure})

	def take(self, str):
		cards_left = self.remain.get(str)
		if cards_left and cards_left > 0:
			self.remain[str]-= 1
			return globals()[str]


def store_test():
	s = Store()
	print(s.take("Smithy"))
	print(s.remain)

# store_test()


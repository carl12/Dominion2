from store import Store
from manager import *
class Game:
	
	def __init__(self, managers):
		self.managers = managers
		self.store = Store(len(managers))
		for m in managers:
			m.set_store(self.store)


	def play_turn(self, num=1):
		for _ in range(num):
			for manager in self.managers:
				manager.take_turn()
				if self.store.is_game_over():
					return self.get_winner()
		return False


	def get_winner(self):
		maxP = -1000
		turns = 1000
		winners = []
		for p in managers:
			if p.get_points() > maxP:
				winners = [p]
				maxP = p.get_points()
				turns = p.turns
			elif p.get_points == maxP:
				if p.turns < turns:
					winners = [p]
				elif p.turns == turns:
					winner.append(p)
		return winners


g = Game([DumbMoney(),DumbMoney()])
g.play_turn()




'''
-check end game
-
'''
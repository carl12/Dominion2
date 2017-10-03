from store import Store
from manager import *
class Game:
	
	def __init__(self, managers, store):
		self.managers = managers
		self.store = store



	def play_turn(self, num=1):
		for _ in range(num):
			for manager in self.managers:
				manager.take_turn()
				if self.store.is_game_over():
					return self.get_winner()
		return False


	def get_winner(self):
		maxM = -1000
		turns = 1000
		winners = []
		for m in self.managers:
			if m.get_points() > maxM:
				winners = [m]
				maxM = m.get_points()
				turns = m.turns
			elif m.get_points == maxM:
				if m.turns < turns:
					winners = [m]
				elif m.turns == turns:
					winner.append(m)
		return winners

def make_game():
	store = Store(2)
	p1 = DumbMoney(store,1)
	p2 = DumbMoney(store,2)
	return Game([p1,p2],store)


g = make_game()
g.play_turn(100)
print(g.managers[0].player.set.all)



'''
-check end game
-
'''
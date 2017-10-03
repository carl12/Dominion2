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
		for i,m in enumerate(self.managers):
			if m.get_points() > maxM:
				winners = [i]
				maxM = m.get_points()
				turns = m.turns
			elif m.get_points == maxM:
				if m.turns < turns:
					winners = [i]
				elif m.turns == turns:
					winner.append(i)
		return winners

def make_game():
	store = Store(2)
	p1 = DumbMoney(store)
	p2 = DumbMoneyV3(store)
	return Game([p1,p2],store)

def play_game():
	g = make_game()
	g.play_turn(100)
	winner = g.get_winner()
	if len(winner) == 1:
		return winner[0]
	
def play_100():
	win = [0,0]
	for _ in range(1000):
		winner = play_game()
		win[winner]+=1
		print(winner)
	print(win)
		



play_100()
# g = make_game()
# g.play_turn(100)
# print(g.managers[0].player.set.all)
# print(g.managers[0].get_points())
# print(g.managers[1].player.set.all)
# print(g.managers[1].get_points())
# print(g.get_winner())



'''
-check end game
-
'''
from store import Store
from manager import *
import random
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
			points = m.get_points()
			if points > maxM:
				winners = [i]
				maxM = points
				turns = m.turns
			elif points == maxM:
				if m.turns < turns:
					winners = [i]
				elif m.turns == turns:
					winners.append(i)
		return winners

	def get_stats(self):
		stats = {}
		stats['winner'] = self.get_winner()
		stats['points'] = [m.get_points() for m in self.managers]
		stats['turns'] = [m.turns for m in self.managers]
		stats['cardList'] = self.get_all()
		return stats


	def get_all(self):
		a = [m.get_all() for m in self.managers]
		c = sum([1 if card.name == 'Province' else 0  for card in a[0]])
		d = sum([1 if card.name == 'Province' else 0  for card in a[1]])
		cardList = [[card.name for card in player] for player in a]
		return cardList

	def count_vp(self):
		pass
		

def make_game_rand_ord():
	store = Store(2)
	p1 = DumbMoneyV3(store)
	p2 = DumbMoneyV2(store)
	if random.choice([True, False]):
		return (Game([p1,p2],store),True)
	else:
		return (Game([p2,p1],store),False)
	

def play_game():
	g,order = make_game_rand_ord()
	g.play_turn(100)
	stats = g.get_stats()
	winner = stats['winner']
	if len(winner) == 1:
		if order:
			return winner[0]
		else:
			return 0 if winner[0] else 1
	
def play_100():
	win = [0,0]
	for i in range(10000):
		if (i+1)%1000==0:
			print(i+1,'games')
		winner = play_game()
		if winner is not None:
			win[winner]+=1
	print(win)
		

play_100()


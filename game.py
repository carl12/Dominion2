from store import Store

class Game:
	
	def __init__(self):
		self.players = []
		self.store = Store()


	def play_turn(self, num=1):
		for _ in range(num):
			for player in players:
				print('Starting ',player,' turn')
				player.take_turn()
				if store.is_game_over():
					return self.get_winner()
		return False


	def get_winner(self):
		maxP = -1000
		turns = 1000
		winners = []
		for p in players:
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


	



'''
-check end game
-
'''
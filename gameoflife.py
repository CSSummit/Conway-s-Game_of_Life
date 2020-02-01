import random
import itertools
import os, time

clear = lambda: os.system('cls')

class GameOfLife(object):
	
	def __init__(self, rows, columns):
		
		self.rows = rows
		self.columns = columns
		
		life_queue = lambda: [random.randint(0, 1) for n in range(self.columns)]
		self.game = [life_queue() for n in range(self.rows)]
	
	def __str__(self):
		
		game = ''
		
		for row in self.game:
			for cell in row:
				game += '* ' if cell else '  '
			game += '\n'
		return game
	
	def neighbors(self, nf, nc):
		
		distance_neighbors = list(
			set(itertools.permutations([-1, -1, 1, 1, 0], 2))
			)
		
		out_of_the_game = lambda x, y: not (x in range(self.rows) and y in range(self.columns))
		
		neighbors = 0
		
		for dist_row, dist_column in distance_neighbors:
			if not out_of_the_game(nf + dist_row, nc + dist_column):
				neighbors += 1 if self.game[nf + dist_row][nc + dist_column] else 0
		
		return neighbors
	
	def travel(self):
		
		for nf in range(self.rows):
			for nc in range(self.columns):
				neighbors = self.neighbors(nf, nc)
				
				if neighbors < 2 or neighbors > 3:
					self.game[nf][nc] = 0
				elif neighbors == 3:
					self.game[nf][nc] = 1

def main():
	clear()
	rows, columns = int(input("Rows -- ")), int(input("Columns -- "))
	
	game = GameOfLife(rows, columns)
	
	while True:
		clear()
		print(game)
		game.travel()
		time.sleep(0.5)

if __name__ == '__main__':
	main()

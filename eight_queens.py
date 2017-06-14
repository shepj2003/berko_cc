"""
  solve the eight queens problem
  this solution is brute strength ...
  ... just find all permutations of 1..n and check the diagonals
  permutations of 1..n automatically satisfy the condition 
  that no 2 queens are on the same row or col
"""

from itertools import permutations


n=8

def eight_queens(n) : 
	r = range(n)
	for x in permutations(r) :
		diag1 = [x[i] + i for i in r] 
		diag2 = [x[i] - i for i in r]
		if n == len(set(diag1))  and n == len(set(diag2)) :
			display_chess_board( x )

def display_chess_board(solution) :
	n = len(solution)
	board = []
	for i in range(n) :
		row = list( '-'*n)
		row[solution[i]] = 'x'
		row = ''.join(row)
		board.append(row)
	print ("\n".join(board))
	print ("\n"*5)


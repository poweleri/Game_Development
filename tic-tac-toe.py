def display (board):
	for i in board:
		print '|'.join(board[i])
		if i == 2 or i == 5
			print '\n'
			
def interact (board, player):
	replace = int(input())
	board[replace] = player
	
def logic (board, player):
	vert = [0, 3, 6]
	hori = [0, 1, 2]
	
	win = [player, player, player]
	
	for x in range (0, 3)
		if [board[vert[0]], board[vert[1]], board[vert[2]]] == win
			return t
		if [board[hori[0]], board[hori[1]], board[hori[2]]] == win
			return t
			
		vert[0]+=1
		vert[1]+=1
		vert[2]+=1
		
		hori[0]+=1
		hori[1]+=1
		hori[2]+=1
		
	if [board[0], board[4], board[8]] == win
		return t
	elif [board[2] board[4], board[6]] == win
		return true
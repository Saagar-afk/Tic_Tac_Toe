###-----------Global Valiable-----------
gameon = True
turn = "X"
changeturn = True

board = ["-" , "-" ,"-" ,
			"-" , "-" , "-" ,
			"-" , "-" , "-"]

def display_board():
	print( board[0]+ " + " + board[1]+ " + " + board[2] )
	print( board[3]+ " + " + board[4]+ " + " + board[5] )
	print( board[6]+ " + " + board[7]+ " + " + board[8] )	

def clear_board():
	for x in range(9):
		board[x] = "-"

def user():
	global user1 ,user2
	user1 = input("Enter the user for 'X' 's user:")
	user2 = input("Enter the user for 'O' 's user:")
	print()
	print(user1 + " : X ")
	print(user2 + " : O ")
	print()	
	print("Let the game Begin:")
	print("-"*50)
	

def check_turn():
	global turn, changeturn
	if changeturn == True:
		if turn =="X":
			turn = "O"
			return turn
		elif turn == "O":
			turn = "X"
			return turn
	

def check_rows():
	#Check for X
	if board[0] == board[1] == board[2] == "X":
		return 'X'
	elif board[3] == board[4] == board[5] == "X":
		return 'X'
	elif board[6] == board[7] == board[8] == "X":
		return 'X'
	else:
		pass
	#Check for O
	if board[0] == board[1] == board[2] == "O":
		return 'O'
	elif board[3] == board[4] == board[5] == "O":
		return 'O'
	elif board[6] == board[7] == board[8] == "O":
		return 'O'
	else:
		pass
def check_columns():
	#Check for "X"
	if board[0] == board[3] == board[6] == "X":
		return 'X'
	elif board[1] == board[4] == board[7] == "X":
		return 'X'
	elif board[2] == board[5] == board[8] == "X":
		return 'X'

	#Check for "O"
	if board[0] == board[3] == board[6] == "O":
		return 'O'
	elif board[1] == board[4] == board[7] == "O":
		return 'O'
	elif board[2] == board[5] == board[8] == "O":
		return 'O'

def check_diagonals():
	#Check diagonals for "X"
	if board[0] == board[4] == board[8] == "X":
		return 'X'
	elif board[2] == board[4] == board[6] == "X":
		return 'X'
	#Check diagonals for "O"
	if board[0] == board[4] == board[8] == "O":
		return 'O'
	elif board[2] == board[4] == board[6] == "O":
		return 'O'

def playagainfn():
	global gameon
	playagain = input("Do you want to play again? [Y|N] :")
	if playagain == "Y" or playagain == "y":
		main()
	elif playagain =="N" or playagain == "n":
		print("Thank you for playing...")
		gameon = False
	else:
		print("Invalid input")
		playagainfn()

def check_gameover():

	if check_rows() == 'X' or check_columns() =="X" or check_diagonals() == "X":
		print(user1+" won.")

		playagainfn()
		

	elif check_rows() == "O" or check_columns() =="O" or check_diagonals() == "O":
		print(user2 +" won.")

		playagainfn()

def valid_move(position, turn):
	global changeturn
	if board[position] == "X" or board[position] == "O":
		print("Invalid move")
		changeturn = False
	else:
		board[position] = turn
		changeturn = True


def main():
	user()
	clear_board()
	display_board()

	while gameon:
		if turn == "X":
			print(user1 + "'s turn.(X)")
		elif turn == "O":
			print(user2 + "'s turn.(O)")

		try:
			position = input("Enter the position form [1-9]: ")
			position = int(position) - 1
			if turn == "X":	
				valid_move(position, turn)
				display_board()
				check_gameover()
				check_turn()

			elif turn =="O":
				valid_move(position, turn)
				display_board()
				check_gameover()
				check_turn()
		except:
			print("Invalid input")
			display_board()
		
		








main()
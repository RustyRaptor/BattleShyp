
from random import randint
board = []

#prompt player to set difficulty
difficulty = input("Set difficulty. Must be 1, 2, or 3:")

#check to make sure difficulty is valid
if difficulty < 1 or difficulty > 3:
	difficulty = input("that number is too big or too small please enter a number 1, 2, or 3")
#here it appends the grid to the array "board" depending on the difficulty.
#I am working on a better way to do this as this is a bit messy and not very modular
elif difficulty == 1 :
	for x in range(3):
    		board.append(["O"] * 3)
	a = 3
elif difficulty == 2:
	for x in range(5):
		board.append(["0"] * 5)
	a = 5
elif difficulty == 3:
	for x in range(7):
		board.append(["0"] * 7)
	a = 7

#this function will let you print the board at any part of the program.
def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

#This function will allow us to generate a random coordinate for the ship's location
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#prompts the user to guess where the ship it on the grid
for turn in range(9):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Collumn:"))
	#if the player hits it...
    if guess_row == ship_row and guess_col == ship_col:
        print "Target Neutralized"
		#we turn the "0" into a "+" when the player hits the ship
        board[guess_row][guess_col] = "+"
        break

    else:
	#if the player picks a location off the grid...
        if (guess_row < 0 or guess_row > a) or (guess_col < 0 or guess_col > a):
            print "Coordinates undefined"
        elif(board[guess_row][guess_col] == "X"):
			print "coordinates already struck"
			print_board(board)
	#if the player misses the ship
        else:
            print "Target Missed"
		#we turn the "0" into an "X" when it is hit and misses
            board[guess_row][guess_col] = "X"
	#This is the turn system.
        print "Turn", turn + 1
if turn == 8:
	print "Defeat"
	print "the target location was", str(ship_row), " , ", str(ship_col)
print_board(board)

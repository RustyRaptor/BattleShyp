# import the randint function to generate random numbers for the grid
from random import randint
# create an ampty array to use for the grid. This way it is modular
board = []

# for loop to make a 5*5 grid by default
# you can set this to whatever you want as long as 
# you change the rest to fit.
# I plan to make this set by difficulty 
# that can be selected in-game
difficulty = input("Set difficulty. Must be 1, 2, or 3:")
if difficulty < 1 or difficulty > 3:
	difficulty = input("that number is too big or too small please enter a number 1, 2, or 3")
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
def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(9):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Collumn:"))
    if guess_row == ship_row and guess_col == ship_col:
        print "Target Neutralized"
        board[guess_row][guess_col] = "+"
        break

    else:
        if (guess_row < 0 or guess_row > a) or (guess_col < 0 or guess_col > a):
            print "Coordinates undefined"
        elif(board[guess_row][guess_col] == "X"):
			print "coordinates already struck"
			print_board(board)
        else:
            print "Target Missed"
            board[guess_row][guess_col] = "X"
        print "Turn", turn + 1
if turn == 8:
	print "Defeat"
	print "the target location was", str(ship_row), " , ", str(ship_col)
print_board(board)

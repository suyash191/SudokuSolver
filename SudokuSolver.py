'''The following program is a Sudoku solver program. It takes a 9X9 sudoku and solves it using a special method called BACKTRACKING.
   Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally,
   one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time'''



board = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]



#function to solve the board using backtracking(implemented through recurssion)
def solve(bo):
	find=find_empty(bo)
	if not find:
		return True
	else:
		row, col=find

	for i in range(1, 10):
		if valid(bo, i, (row, col)):
			bo[row][col]=i

#keep moving fwd if function returns true
			if solve(bo):
				return True
#change current value to 0 and backtrack
			bo[row][col]=0

	return False



#function to check if the board with the value inserted is valid or not
def valid(bo, num, pos):
#num is the number that is inserted at position pos(i, j)

#check row
	for i in range(9):
		if bo[pos[0]][i]==num and i!=pos[1]:
			return False
	#check column
	for i in range(9):
		if bo[i][pos[1]]==num and i!=pos[0]:
			return False
	#check box
	box_x=pos[1]//3
	box_y=pos[0]//3
	for i in range(box_y*3, box_y*3+3):
		for j in range(box_x*3, box_x*3+3):
			if bo[i][j]==num and (i,j)!=pos:
				return False
	#if none of the if conditions are true, this means the board is correct, return true
	return True



def print_board(bo):

	for i in range(9):
		if i%3==0 and i!=0:
			print("------------------------------------")

		for j in range(9):
			if j%3==0:
				print(" | ", end="")
			if j==8:
				print(bo[i][j], "|")
			else:
				print(str(bo[i][j])+" ", end="")



def find_empty(bo):

	for i in range(9):
		for j in range(9):
			if bo[i][j]==0:
				return (i,j) #tuple to return index

	return None #returns none if no empty index found



print_board(board)
print("xxxxxxxxxxxxxxx\"The solution is\"xxxxxxxxxxxxxxxxxxxxxx")
solve(board)
print_board(board)
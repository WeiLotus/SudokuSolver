# This is a text version of the famous sudoku solver
# Given an 2-d array of size 9x9 sudoku board, with some digits filled up and others filled with 0
# Then the program would do a backtrack depth-first search (DFS) and fill up all 0s with 1-9 satisfying the board
# Or if the board is unsolvable, throw an error. 
# Made in collaboration of Johnson Chen and Lotus Wei

# create a sudoku board
board = [[0,0,0,0,0,0,3,9,0],[8,7,0,0,3,2,0,5,0],[0,3,0,0,0,4,1,0,2],
         [7,1,0,0,2,9,0,0,8],[0,2,4,0,0,0,9,7,0],[6,0,0,3,4,0,0,1,5],
         [5,0,7,4,0,0,0,2,0],[0,6,0,8,7,0,0,4,9],[0,4,8,0,0,0,0,0,0]]

#print(board)

def solver(bo):

    # find empty cells
    def empty_find(bo):
        for row in range(9):
            for col in range(9):
                if bo[row][col] == 0:
                   emp = (row,col)
                   return emp
                    #print(row,col)
    
    cell = empty_find(bo)
    if cell:
        r,c = (cell[0],cell[1])
    else:
        return True
        
    for i in range(1,10):    
        if valid(bo, emp, i):
          bo[r][c] = i  
              
          if solver(bo):
              return True
          
          bo[r][c] = 0
    
    return False
    


# end of solver method
 
solver(board)

# Effects: returns if the attempted input number on the corresponding position is valid
# Param:
#   board: 2-d array of ints
#   pos: (row,col) as (int,int)
#   input: int
#   return: bool
def valid(board,pos,input):
    for i in range(9):
        if board[pos[0]][i] == input and i != pos[1]:
            return False
        if board[i][pos[1]] == input and i != pos[0]:
            return False
        
    xPos = pos[0]/3
    yPos = pos[1]/3
    
    for m in range (xPos * 3, xPos * 3 + 3):
        for n in range(yPos * 3, yPos * 3 + 3):
            if board[m][n] == input and (xPos,yPos) != pos:
                return False
    return True

# Effects: prints the current board
# Param:
#   board: 2-d array of ints
def show_board(board):
    for i in range(9):
        if i % 3  == 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|",end=str(board[i][j]) + " ")
            elif j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]), end = " ")
    print("- - - - - - - - - - -")

grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

#show_board(grid)
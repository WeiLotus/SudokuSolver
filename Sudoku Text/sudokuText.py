# This is a text version of the famous sudoku solver
# Given an 2-d array of size 9x9 sudoku board, with some digits filled up and others filled with 0
# Then the program would do a backtrack depth-first search (DFS) and fill up all 0s with 1-9 satisfying the board
# Or if the board is unsolvable, throw an error. 
# Made in collaboration of Johnson Chen and Lotus Wei


# Effects: returns if the attempted input number on the corresponding position is valid
# Param:
#   board: 2-d array of ints
#   pos: (row,col) as (int,int)
#   input: int
def valid(board,pos,input):
    for i in range(0,8):
        if(board[pos[0]][i] == input and i != pos[1]):
            return False
        if(board[i][pos[1]] == input and i != pos[0]):
            return False
        
    return True
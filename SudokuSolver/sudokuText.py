#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 23:20:34 2022

@author: lotus.wei
"""

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
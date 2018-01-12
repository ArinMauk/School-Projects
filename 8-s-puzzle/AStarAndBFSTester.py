"""
Call A* class
Call BFS class

"""
import random
import sys

from AStar8puzzle import *
from BFS8puzzle import *
def randomBoard():
    board = []
    numbers = [None, 1,2,3,4,5,6,7,8]
    for row in range(0, 3):                                          
        tempBoard = []                                                 
        for col in range(0,3):
            number = random.randrange(0,len(numbers))
            tempBoard.append(numbers[number])
            del (numbers[number])
        board.append(tempBoard)                  
    return board
def main():
    for i in range(0, 3):

    	board = randomBoard()
    	print("BOARD: ")
    	print(board)
	try:
    		solveAStar = AStar(board)
	    	solveBFS = BFS(board)
        except:
		print("Solution Not Found")

main()
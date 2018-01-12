import copy
class BFS(object):
    def __init__(self, board):
        self.goalState = [[None, 1, 2], [3,4,5,], [6,7,8]]
        self.board = board
        self.closedList = [] #Already explored nodes 
        self.openList = [] #fringe, nodes to yet be explored
        self.rootNode = 0
        self.solve = Tree(self.rootNode, self.board, self.openList, self.closedList, self.goalState)

class Node:
    def __init__(self, board):
        self.cur_state = board
        self.parent = None
        self.action = None
        self.depth = None
        self.heurEstim = None

class Tree:

    def __init__(self, rootNode, initState, openList, closedList, goalState):
        self.solutionFound = False
        self.node = Node(initState)
        self.node.parent = rootNode
        self.node.action = None
        self.node.depth = 0
        self.node.heurEstim = self.calcHeur(initState, 0)
        
        openList.append(self.node)
	while(not (self.solutionFound)):
		if(not (len(openList))):
			print("Failed")
			print(len(openList))
			self.solutionFound = True
		else:
			bestHeur = openList[0].heurEstim
			bestNode = openList[0]
			for notExplored in openList:
				if(notExplored.heurEstim == 0):
					self.solutionFound = True
					self.solution(notExplored)
				elif(notExplored.heurEstim < bestHeur):
					bestHeur = notExplored.heurEstim
					bestNode = notExplored
			if(self.solutionFound == False):
				#print("Best node heuristic: " + str(bestNode.heurEstim))
				#print("Best node Board: " + str(bestNode.cur_state))
				#cont = str(raw_input("continue"))
				openList.remove(bestNode)
				closedList.append(bestNode)
				#print("Closed List length:" + str(len(closedList)))
				self.successor = self.expand(bestNode, closedList)
				for s in self.successor:
					openList.append(s)
			print("===============================================")
			
	
    def expand(self, node, closedList):
        
        #print("closedList Length in expand: " + str(len(closedList)))
        self.actions = ["up", "down", "right", "left"]
        self.successors = []
        #self.childNode = Node(n.cur_state)
        for action in self.actions:
	    
            if(self.legalMove(action, node.cur_state, closedList) == True):
		
     		self.cNode = self.createNode(copy.deepcopy(node.cur_state), node.parent, action, copy.deepcopy(node.depth))
      		self.cNode.cur_state = self.prefActions(self.cNode.cur_state, self.cNode.action, self.spotLoc(self.cNode.cur_state))
		self.cNode.heurEstim = self.calcHeur(self.cNode.cur_state, self.cNode.depth)
		print("Child state: " + str(self.cNode.cur_state) + " Hueristic Value: " + str(self.cNode.heurEstim) + " Depth: " + str(self.cNode.depth))
		self.successors.append(self.cNode)
        return self.successors

    def createNode(self, par_board, parentNode, action, depth):
        
        self.node = Node(par_board)
        self.node.parent = parentNode
        self.node.depth = depth + 1
        self.node.action = action
        print("Child Done")
        return self.node

    def spotLoc(self, board):
        self.coords = []
        for i in range(0, 3):
            for j in range(0, 3):
                if(board[i][j] == None):
                    self.coords.append(i)
                    self.coords.append(j)
        return self.coords

    def prefActions(self, board, action, openSpotLoc):
        """openSpotLoc[0] = row
           openSpotLoc[1] = col
        """
        
        if(action == "up"):
            if(openSpotLoc[0] != 0):
                return self.swap(openSpotLoc, [(openSpotLoc[0]-1), openSpotLoc[1]], board)
        elif(action == "down"):
            if(openSpotLoc[0] != 2):
                return self.swap(openSpotLoc, [(openSpotLoc[0]+1), openSpotLoc[1]], board)
        elif(action == "right"):
            if(openSpotLoc[1] != 2):
                return self.swap(openSpotLoc, [openSpotLoc[0], (openSpotLoc[1]+1)], board)
        elif(action == "left"):
            if(openSpotLoc[1] != 0):
                return self.swap(openSpotLoc, [openSpotLoc[0], (openSpotLoc[1]-1)], board)

    def legalMove(self, action, board, closedList):
        openSpot = self.spotLoc(board)
        potentialSpot = None
        self.testBoard = copy.deepcopy(board)
        """Due to Python's pass by object, this effectively creates a clone without altering original"""

        if(action == "up"):
            if(openSpot[0] != 0):
                potentialSpot = self.swap(openSpot, [(openSpot[0]-1), openSpot[1]], self.testBoard)
            else:
                return False
        elif(action == "down"):
            if(openSpot[0] != 2):
                potentialSpot = self.swap(openSpot, [(openSpot[0]+1), openSpot[1]], self.testBoard)
            else:
                return False
        elif(action == "right"):
            if(openSpot[1] != 2):
                potentialSpot = self.swap(openSpot, [openSpot[0], (openSpot[1]+1)], self.testBoard)
            else:
                return False
        elif(action == "left"):
            if(openSpot[1] != 0):
                potentialSpot = self.swap(openSpot, [openSpot[0], (openSpot[1]-1)], self.testBoard)
            else:
                return False
            
        for explored in closedList:
            #print("Potential spot: " + str(potentialSpot) + " explored.cur_state: " + str(explored.cur_state))
            if(potentialSpot == explored.cur_state):
                return False
            
        return True

    def swap(self, a, b, par_board):
        self.node_board = par_board
        temp = self.node_board[a[0]][a[1]]
        self.node_board[a[0]][a[1]] = self.node_board[b[0]][b[1]]
        self.node_board[b[0]][b[1]] = temp
        
        return self.node_board

    def calcHeur(self, board, depth):
        order = 0
        amtNotOrdered = 9
        
        for i in range(0, 3):
            for j in range(0, 3):
                if(not board[i][j]):
			if(i == 0 and j == 0):
		    		order += 0
                    		amtNotOrdered -= 1   
                elif(board[i][j] == order):
                    amtNotOrdered -= 1
                order += 1
        if(amtNotOrdered == 0):
            return 0
        
        return (depth + 1)

    def solution(self, node):
        print("SOLUTION FOUND: ")
        print("Depth/Path length: " + str(node.depth))
        print("Board: " + str(node.cur_state))

    if(__name__ == "__main__"):
        main()
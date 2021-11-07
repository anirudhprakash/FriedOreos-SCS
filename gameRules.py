
import random

def isExterior(x, y, dimensions):
    #Is the cell a border cell?
    if x == 0 or y == 0:
        return True
    
    if x == dimensions - 1 or y == dimensions - 1:
        return True
    
    return False

    


def generateMap(dimensions):
    
    board = [
        ['grass' for i in range(dimensions)] for j in range(dimensions)
    ]

    #Name region

    baseName = 'Base'
    grassName = 'Grass'
    mountainName = 'Mountain'
    oceanNmae = 'Ocean'

    kosbieName = 'Kosbie'
    taylorName = 'Taylor'
    outpostName = 'Outpost'
    farmName = 'Farm'

    kosbieOutpostName = outpostName + kosbieName
    taylorOutpostName = outpostName + taylorName

    kosbieFarmName = farmName + kosbieName
    taylorFarmName = farmName + taylorName

    #Probability Region
    probOutpostInterior = 0.3                      #We favour placing outposts near the middle for fairness.
    probOutpostExterior = 0.1                      

    probFarmInterior = 0.2                         #We favour placing farms along the edges.
    probFarmExterior = 0.4

    probOcean = 0.05                               #Oceans occupy multiple squares, so their probability is cumulative over their area.
    probMountain = 0.1                             #Mountains are one square types, so their probabilities are not cumulative.

    for x in range(dimensions):
        for y in range(dimensions):
            cell = board[x][y]
            if cell != grassName:                  #Taken, typically by an ocean as oceans exist as blocks.
                continue
            
            randVal = random.randint(0, 100) / 100 #A random integer to decide the position of the square.
            isBorder = isExterior(x, y, dimensions)    

            if isBorder == True:
                probOutpost = probOutpostInterior

# Source: https://www.geeksforgeeks.org/breadth-first-traversal-bfs-on-a-2d-array/
# Python3 program for the above approach
from collections import deque as queue

# Direction vectors
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]

# Function to check if a cell
# is be visited or not
def isValid(vis, row, col):

	# If cell lies out of bounds
	if (row < 0 or col < 0 or row >= len(board) or col >= len(board)):
		return False

	# If cell is already visited
	if (vis[row][col]):
		return False

	# Otherwise
	return True

# Function to perform the BFS traversal
def BFS1(grid, vis, row, col):

	# Stores indices of the matrix cells
	q = queue()

	# Mark the starting cell as visited
	# and push it into the queue
	q.append(( row, col ))
	vis[row][col] = True

	# Iterate while the queue
	# is not empty
	while (len(q) > 0):
		cell = q.popleft()
		x = cell[0]
		y = cell[1]
		print(grid[x][y], end = " ")

		#q.pop()

		# Go to the adjacent cells
		for i in range(4):
			adjx = x + dRow[i]
			adjy = y + dCol[i]
			if (isValid(vis, adjx, adjy)):
				q.append((adjx, adjy))
				vis[adjx][adjy] = True


vis = [[ False for i in range(8)] for i in range(8)]
BFS1(board,vis,0,0)

# This code is contributed by mohit kumar 29.






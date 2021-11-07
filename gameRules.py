import random
from collections import deque
def isExterior(x, y, dimensions):
    #Is the cell a border cell?
    if x == 0 or y == 0:
        return True
    
    if x == dimensions - 1 or y == dimensions - 1:
        return True
    
    return False

from collections import deque


def checkMap(board):
    badSquares = ['Ocean', 'Mountain']
    matrix = []
    validSquares = []
    for i in range(len(board)):
        matrix.append([])
        for j in range(len(board)):
            if board[i][j] in badSquares:
                matrix[i].append(120)
            else:
                matrix[i].append(1)
                validSquares.append((i, j))
    
    for i in range(len(validSquares)):
        for j in range(i, len(validSquares)):
            start = validSquares[i]
            end = validSquares[j]
            if BFS(start, end, matrix) == -1:
                return False
    return True


def BFS(start, end, graph):
    queue = [[start]]
    seen = set([start])
    while queue:
        path = queue.pop(0)
        if len(path) > 20:
            return False
        x, y = path[-1]
        if x == end[0] and y == end[1]:
            return True
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < len(graph) and 0 <= y2 < len(graph) and graph[x2][y2] != 120 and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))



def generateMap(dimensions):
    
    board = [
        ['Grass' for i in range(dimensions)] for j in range(dimensions)
    ]
    board[0][0] = 'BaseKosbie'
    board[-1][-1] = 'BaseTaylor'

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
    probOutpostInterior = 0.02                      #We favour placing outposts near the middle for fairness.
    probOutpostExterior = 0.05                      

    probFarmInterior = 0.05                         #We favour placing farms along the edges.
    probFarmExterior = 0.02

    probOcean = 0.15                              #Oceans occupy multiple squares, so their probability is cumulative over their area.
    probMountain = 0.2                             #Mountains are one square types, so their probabilities are not cumulative.

    while True:
        for x in range(dimensions):
            for y in range(dimensions):
                cell = board[x][y]
                if cell != grassName:                  #Taken, typically by an ocean as oceans exist as blocks.
                    continue
                randVal = random.randint(0, 100) / 100 #A random integer to decide the position of the square.

                isBorder = isExterior(x, y, dimensions)    

                if isBorder == True:
                    probOutpost = probOutpostInterior
                    probFarm = probFarmInterior
                
                else:
                    probOutpost = probOutpostExterior
                    probFarm = probFarmExterior
                
                if randVal < probOcean:
                    board[x][y] = 'Ocean'
                    continue
                
                elif randVal < probMountain:
                    board[x][y] = 'Mountain'
                    continue
                
                elif randVal < probOutpost + (probOcean + probMountain):
                    board[x][y] = 'Outpost'
                    continue
                
                elif randVal < probFarm + (probOcean + probMountain):
                    board[x][y] = 'Farm'
                continue
        
        if checkMap(board):
            return board
        board = [
            ['grass' for i in range(dimensions)] for j in range(dimensions)
        ]
    
    
for i in generateMap(6):
    print(*i)

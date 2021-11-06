
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







class Piece(object):
    def __init__(self,x,y,attackDamage,movesAllowed,owner,health):
        self.x = x
        self.y = y
        self.attackDamage = attackDamage
        self.movesAllowed = movesAllowed
        self.health = health
        self.owner = owner
    
    def attack (self, other):
        other.health -= self.attack

    def getX (self):
        return self.x
    
    def getY (self):
        return self.y

    def generateMovesAllowed(self,board,characters):
        generatedMovesAllowed = []
        for dx in range((-1*self.movesAllowed), (self.movesAllowed)+1):
            for dy in range((-1*self.movesAllowed), (self.movesAllowed)+1):
                if dx == 0 and dy == 0:
                    continue
                if board[self.x+dx][self.y+dy] not in ["Ocean", "Mountain"]:
                    generatedMovesAllowed.append((self.x+dx,self.y+dy))

        #Check if player is in the generatedMovesAllowed: 
        charactersOnBoardCords = []
        for character in characters:
            charactersOnBoardCords.append((character.x, character.y))
        for cord in generatedMovesAllowed:
            if cord in charactersOnBoardCords:
                generatedMovesAllowed.remove(cord)
        return generatedMovesAllowed

class Soldier(Piece):
    def __init__(self,x,y,owner):
        super().__init__(self,x,y,25,1,owner,50)

class Knight(Piece):
    def __init__(self,x,y,owner):
        super().__init__(self,x,y,40,2,owner,75)

class Archer(Piece):
    def __init__(self,x,y,owner):
        super().__init__(self,x,y,30,1,owner,40)

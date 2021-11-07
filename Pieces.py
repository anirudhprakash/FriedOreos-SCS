class Piece(object):
    def __init__(self,x,y,attackDamage,movesAllowed,owner,health):
        self.x = x
        self.y = y
        self.attackDamage = attackDamage
        self.movesAllowed = movesAllowed
        self.health = health
        self.owner = owner
    
    def attack (self, other):
        other.health -= self.attackDamage

    def getX (self):
        return self.x
    
    def getY (self):
        return self.y

    def getCords(self):
        return (self.x,self.y)

    def getPieceInCell(self,row,col,app):
        for otherCharacter in app.characters:
                if otherCharacter.getCords() == (col,row):
                    return otherCharacter
        return None

    def generateMovesAllowed(self,app):
        generatedMovesAllowed = []
        for dx in range((-1*self.movesAllowed), (self.movesAllowed)+1):
            for dy in range((-1*self.movesAllowed), (self.movesAllowed)+1):
                if dx == 0 and dy == 0:
                    continue
                newX = self.x + dx
                newY = self.y + dy

                if newX < 0 or newX >= len(app.board) or newY < 0 or newY >= len(app.board):
                    continue

                if app.board[self.y+dy][self.x + dx] not in ["Ocean", "Mountain"]:
                    generatedMovesAllowed.append((self.y+dy,self.x+dx))
    
        return generatedMovesAllowed
    
    def move(self,app,targetRow,targetCol):
        
        enemyPiece = self.getPieceInCell(targetRow,targetCol,app)          #if enemy in targetRow, targetCol -> attack:
        print(enemyPiece)
        if enemyPiece != None:
            self.attack(enemyPiece)
            if enemyPiece.health <= 0:
                app.characters.remove(enemyPiece)

            
        if self.getPieceInCell(targetRow,targetCol,app) == None: 
            self.x = targetCol
            self.y = targetRow
        
        if enemyPiece == None: 
            if 'outpost' in app.board[targetRow][targetCol].lower():
                app.board[targetRow][targetCol] = "Outpost" + self.owner

            if 'farm' in app.board[targetRow][targetCol].lower():
                app.board[targetRow][targetCol] = "Farm" + self.owner

            self.x = targetCol
            self.y = targetRow

        
        for dx in range(-1,2):                                                  #UPDATE THIS TO CODE
            for dy in range(-1,2):
                newX = self.x + dx
                newY = self.y + dy

                if newX < 0 or newX >= len(app.board) or newY < 0 or newY >= len(app.board):
                    continue
                if app.visibility[self.y+dy][self.x+dx] == 0:
                    app.visibility[self.y+dy][self.x+dx] = 1
                if app.visibility[self.y+dy][self.x+dx] == 2:
                    app.visibility[self.y+dy][self.x+dx] = 3

class Soldier(Piece):
    def __init__(self,x,y,owner):
        super().__init__(x,y,25,1,owner,50)

class Knight(Piece):
    def __init__(self,x,y,owner):
        super().__init__(x,y,40,2,owner,1)

class Archer(Piece):
    def __init__(self,x,y,owner):
        super().__init__(x,y,30,1,owner,40)

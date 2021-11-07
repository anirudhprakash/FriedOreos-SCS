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
    
class Soldier(Piece):
    def __init__(self,x,y,owner):
        self.x = x
        self.y = y
        self.attackDamage = 25
        self.movesAllowed = 1
        self.health = 50
        self.owner = owner

class Knight(Piece):
    def __init__(self,x,y,owner):
        self.x = x
        self.y = y
        self.attackDamage = 40
        self.movesAllowed = 3
        self.health = 75
        self.owner = owner

class Archer(Piece):
    def __init__(self,x,y,owner):
        self.x = x
        self.y = y
        self.attackDamage = 30
        self.movesAllowed = 1
        self.health = 40
        self.owner = owner
        self.range = 1

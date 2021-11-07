from Pieces import *
from gameRules import *
import random
import copy

class Game(object):
    def __init__(self, app, me, opponent):
        self.board = copy.deepcopy(app.board)
        self.pieces = copy.deepcopy(app.characters)
        self.moves = []
        self.me = me
        self.opp = opponent
        self.turn = me
    
    def generateMoves(self):
        for piece in self.pieces:
            self.moves.append(piece.generateMovesAllowed)
    
    def pickMove(self):
        self.generateMoves()
        return random.choice(random.choice(self.moves))




def getMove(app):
    me = 'Taylor'
    game = Game(app, me, 'Kosbie')
    return game.pickMove()

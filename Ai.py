from Pieces import *
from gameRules import *
import random
import copy

class test(object):
    def __init__(self, app):
        self.board = copy.deepcopy(app.board)
        self.gold0 = app.gold0
        self.gold1 = app.gold1
        self.characters = copy.deepcopy(app.characters)
        self.visibility = copy.deepcopy(app.visibility)


class Game(object):
    def __init__(self, app, me, opponent):
        self.app = test(app)
        self.board = copy.deepcopy(app.board)
        self.allPieces = copy.deepcopy(app.characters)

        self.gold = app.gold1
        
        self.moves = []
        self.me = me
        self.opp = opponent
        self.turn = me

        self.pieces = []
        for piece in self.allPieces:
            if piece.owner == self.me:
                self.pieces.append(piece)
    
    def generateMoves(self, player):

        myOutposts = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if 'Outpost' in self.board[j][i] and player in self.board[j][i]:
                    myOutposts.append((i, j))
                if 'Base' in self.board[j][i] and player in self.board[j][i]:
                    myOutposts.append((i, j))
        canCreate = []
        gold = self.app.gold1
        if player == self.opp:
            gold = self.app.gold0
        if self.gold >= 4:
            canCreate.append('Soldier')
        if self.gold >= 6:
            canCreate.append('Archer')
        if self.gold >= 9:
            canCreate.append('Knight')
        createMoves = []
        for i in canCreate:
            for j in myOutposts:
                if self.app.characters[0].getPieceInCell(j[1], j[0], self.app) == None:
                    createMoves.append(['create', [i, j]])


        self.moves = createMoves
        for piece in self.pieces:
            self.moves.append(['move', piece, piece.generateMovesAllowed(self.app)])
        
        return self.moves

    
    def pickMove(self):
        self.generateMoves()
        if len(self.moves) == 0:
            return 0
        return random.choice(self.moves)
    
    
    
def minimax(game, depth, isMax):
    score = evaluate(game)
    if depth == 0:
        return score
    if isMax:
        player = 'Taylor'
    else:
        player = 'Kosbie'
    
    moves = game.generateMoves(player)
    if len(moves) == 0:
        return score
    

    

    
    if isMax:
        best = -1000
        for move in moves:
            if move == 0:
                return -3
            if move[0] == 'move':
                piece = move[1]
                targRow, targCol = random.choice(move[2])

                piece.move(game.app, targRow, targCol)
            
            elif move[0] == 'create':
                loc = move[1][1]
                piece = move[1][0]
                if piece == 'Soldier':
                    game.app.gold1 -= 4
                    game.app.characters.append(Soldier(loc[1],loc[0],player))
                
                elif piece == 'Archer':
                    game.app.gold1 -= 6
                    game.app.characters.append(Archer(loc[1],loc[0],player))
                
                elif piece == 'Knight':
                    game.app.gold1 -= 9
                    game.app.characters.append(Knight(loc[1],loc[0],player))
            
            best = max( best, minimax(game,
                                            depth - 1,
                                            not isMax) )
        return best
    if not isMax:
        best = 1000
        for move in moves:
            if move == 0:
                return -3
            if move[0] == 'move':
                piece = move[1]
                targRow, targCol = random.choice(move[2])

                piece.move(game.app, targRow, targCol)
            
            elif move[0] == 'create':
                loc = move[1][1]
                piece = move[1][0]
                if piece == 'Soldier':
                    game.app.gold0 -= 4
                    game.app.characters.append(Soldier(loc[1],loc[0],player))
                
                elif piece == 'Archer':
                    game.app.gold0 -= 6
                    game.app.characters.append(Archer(loc[1],loc[0],player))
                
                elif piece == 'Knight':
                    game.app.gold0 -= 9
                    game.app.characters.append(Knight(loc[1],loc[0],player))
            
            best = min( best, minimax(game,
                                            depth - 1,
                                            not isMax) )
        return best





def evaluate(game):
    return game.gold * 2 + len(game.pieces) * 5


def getMove(app):
    me = 'Taylor'
    game = Game(app, me, 'Kosbie')

    bestVal = -1000
    bestMove = None
    moves = game.generateMoves('Taylor')
    if type(moves) != list or len(moves) == 0:
        return
    
    for move in moves:
        if move[0] == 'move':
            piece = app.characters[0].getPieceInCell(move[1].x, move[1].y, app)
            targRow, targCol = random.choice(move[2])
            piece.move(game.app, targRow, targCol)

            
        elif move[0] == 'create':
            loc = move[1][1]
            piece = move[1][0]
            if piece == 'Soldier':
                game.app.gold1 -= 4
                game.app.characters.append(Soldier(loc[1],loc[0],'Taylor'))
            
            elif piece == 'Archer':
                game.app.gold1 -= 6
                game.app.characters.append(Archer(loc[1],loc[0],'Taylor'))
            
            elif piece == 'Knight':
                game.app.gold1 -= 9
                game.app.characters.append(Knight(loc[1],loc[0],'Taylor'))
        moveVal = minimax(game, 1, True)
        if moveVal > bestVal:
            bestVal = moveVal
            bestMove = move





    move = bestMove
    if move == 0:
        return
    if move[0] == 'move':
        piece = move[1]
        targRow, targCol = random.choice(move[2])

        piece.move(app, targRow, targCol)
    
    elif move[0] == 'create':
        loc = move[1][1]
        piece = move[1][0]
        if piece == 'Soldier':
            app.gold1 -= 4
            app.characters.append(Soldier(loc[1],loc[0],'Taylor'))
        
        elif piece == 'Archer':
            app.gold1 -= 6
            app.characters.append(Archer(loc[1],loc[0],'Taylor'))
        
        elif piece == 'Knight':
            app.gold1 -= 9
            app.characters.append(Knight(loc[1],loc[0],'Taylor'))

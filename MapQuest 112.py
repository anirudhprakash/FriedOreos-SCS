from cmu_112_graphics import *
from gameRules import *
from Pieces import *

def appStarted(app):

    app.gold = 5
    app.turn = 0

    #board
    app.board = generateMap(6)
    app.visibility = [([0] * 6) for i in range(6)]
    app.visibility[0][0] = 1
    app.visibility[0][1] = 1
    app.visibility[1][0] = 1
    app.visibility[1][1] = 1

    
    app.characters = []
    app.selected = None
    app.createable = 0
    app.moveable = []

    app.mode = 'titleScreen'
    app.border = 30
    app.squareLength = (app.height - 2 * app.border) // 6 #len(app.board)
    app.rows = 6 #len(app.board)
    app.cols = 6 #len(app.board[0])

    #loading images
    app.cloudBackground = app.loadImage('Images/tiles/fog/fog_tile.png')
    app.cloudBackground = app.scaleImage(app.cloudBackground, app.squareLength/100)
    app.grassBackground = app.loadImage('Images/tiles/grassland/grassland_tile.png')
    app.grassBackground = app.scaleImage(app.grassBackground, app.squareLength/100)
    app.waterBackground = app.loadImage('Images/tiles/ocean/water_tile.png')
    app.waterBackground = app.scaleImage(app.waterBackground, app.squareLength/100)
    app.mountainBackground = app.loadImage('Images/tiles/mountains/mountain_tile.png')
    app.mountainBackground = app.scaleImage(app.mountainBackground, app.squareLength/100)
    app.baseK = app.loadImage('Images/tiles/bases/baseK.png')
    app.baseK = app.scaleImage(app.baseK, app.squareLength/100)
    app.baseT = app.loadImage('Images/tiles/bases/baseT.png')
    app.baseT = app.scaleImage(app.baseT, app.squareLength/100)
    app.outpostK = app.loadImage('Images/tiles/outposts/kosbie_outpost.png')
    app.outpostK = app.scaleImage(app.outpostK, app.squareLength/100)
    app.outpostT = app.loadImage('Images/tiles/outposts/taylor_outpost.png')
    app.outpostT = app.scaleImage(app.outpostT, app.squareLength/100)
    app.outpost = app.loadImage('Images/tiles/outposts/outpost.png')
    app.outpost = app.scaleImage(app.outpost, app.squareLength/100)
    app.farmK = app.loadImage('Images/tiles/farm/kosbie_farm.png')
    app.farmK = app.scaleImage(app.farmK, app.squareLength/100)
    app.farmT = app.loadImage('Images/tiles/farm/taylor_farm.png')
    app.farmT = app.scaleImage(app.farmT, app.squareLength/100)
    app.farm = app.loadImage('Images/tiles/farm/farm.png')
    app.farm = app.scaleImage(app.farm, app.squareLength/100)

    app.archerK = app.loadImage('Images/TA sprites/archers/alex_archer.png')
    app.archerK = app.scaleImage(app.archerK, app.squareLength/100)
    app.archerT = app.loadImage('Images/TA sprites/archers/asad_archer.png')
    app.archerT = app.scaleImage(app.archerT, app.squareLength/100)
    app.knightK = app.loadImage('Images/TA sprites/horseriders/zhara_horserider.png')
    app.knightK = app.scaleImage(app.knightK, app.squareLength/100)
    app.knightT = app.loadImage('Images/TA sprites/horseriders/kian_horserider.png')
    app.knightT = app.scaleImage(app.knightT, app.squareLength/100)
    app.warriorK = app.loadImage('Images/TA sprites/warriors/anitawarrior.png')
    app.warriorK = app.scaleImage(app.warriorK, app.squareLength/100)
    app.warriorT = app.loadImage('Images/TA sprites/warriors/warriorben.png')
    app.warriorT = app.scaleImage(app.warriorT, app.squareLength/100)

    app.game_background = app.loadImage('Images/game_background.png')
    app.game_background = app.scaleImage(app.game_background, 1/3)

    app.game_lore = app.loadImage('Images/game_lore.png')

    
def gameMode_mousePressed(app,event):
    row = getDim(app,event.y)
    col = getDim(app,event.x)
    
    if app.turn == 0:
        if (row >= 0 and row < len(app.board) and
            col >= 0 and col < len(app.board)):

            #check if there is a piece selected
            if app.selected != None and type(app.selected) != tuple:
                if (row,col) in app.moveable:
                    app.selected.move(app,row,col)
                
                clearSelection(app)

            #if nothing is selected, then tries to select a piece or structure
            else:
                #check if piece there
                soldier = soldierSelected(app,row,col)
                print(row,col)
                if soldier != None:
                    app.selected = soldier
                    app.moveable = soldier.generateMovesAllowed(app)
                
                #check is structure there
                elif app.board[row][col] == 'OutpostKosbie' or app.board[row][col] == 'BaseKosbie':
                    app.selected = (row,col)
                    app.createable = generateCreateable(app)

        #the click is outside of the game board
        else:
            options_center = (2 * app.border +  app.squareLength * len(app.board))
            options_center = options_center + (app.width - options_center) // 2 
            #creating a character
            if type(app.selected) == tuple:
                if (event.x > options_center - 150 and event.x < options_center + 150 and
                    event.y > 280 and event.y < 340 and app.createable > 2):
                    app.characters.append(Knight(app.selected[1],app.selected[0],'Kosbie'))
        
                if (event.x > options_center - 150 and event.x < options_center + 150 and
                    event.y > 200 and event.y < 260 and app.createable > 1):
                    app.characters.append(Archer(app.selected[1],app.selected[0],'Kosbie'))
                
                if (event.x > options_center - 150 and event.x < options_center + 150 and
                    event.y > 120 and event.y < 180 and app.createable > 0):
                    app.characters.append(Soldier(app.selected[1],app.selected[0],'Kosbie'))
            
            clearSelection(app)

def clearSelection(app):
    app.selected = None
    app.moveable = []
    app.createable = 0

def generateCreateable(app):
    if app.gold >= 5:
        return 3
    elif app.gold >= 3:
        return 2
    elif app.gold >= 2:
        return 1 
    else:
        return 0



        '''if app.selected != None:
            if {row,col} in app.moveable:
                move(app,row,col)

        elif 'Outpost' in app.board[row][col] or 'Base' in app.board[row][col]:
            app.selected = {row,col}
            generateCreatable(app,row,col)
        
        soldier = soldierSelected(app,row,col)
        if soldier != None:
            app.selected = soldier
            generateMoves(app,row,col)'''

def getDim(app,dim):
    return (dim - app.border) // app.squareLength

def soldierSelected(app,row,col):
    for character in app.characters:
        if character.x == col and character.y == row:
            return character
    return None

        
    
def gameMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,800,800, fill = 'blue')
    drawBoard(app,canvas)
    drawCharacters(app,canvas)
    drawCreateOptions(app,canvas)
    drawMovesAllowed(app,canvas)
    drawFog(app, canvas)

def drawFog(app, canvas):
    for row in range(len(app.visibility)):
        for col in range(len(app.visibility)):
            if app.visibility[col][row] % 2 != 1:
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.cloudBackground))


def drawMovesAllowed(app,canvas):
    for (row,col) in app.moveable:
        circleCenterX = col * app.squareLength + app.border + app.squareLength // 2
        circleCenterY = row * app.squareLength + app.border + app.squareLength //2

        canvas.create_oval(circleCenterX - 10, circleCenterY - 10, circleCenterX + 10,
                           circleCenterY + 10, fill = 'brown')


def drawCreateOptions(app,canvas):
    options_center = (2 * app.border +  app.squareLength * len(app.board))
    options_center = options_center + (app.width - options_center) // 2 

    canvas.create_text(options_center, 50, text = "Create Menu", font = 'Arial 40 underline')

    if app.createable > 2:
        canvas.create_rectangle(options_center - 150, 280, options_center + 150, 340)
        canvas.create_text(options_center, 310, text = 'Knight\t\t5G', font = 'Arial 20')
    
    if app.createable > 1:
        canvas.create_rectangle(options_center - 150, 200, options_center + 150, 260)
        canvas.create_text(options_center, 230, text = 'Archer\t\t3G', font = 'Arial 20')
    
    if app.createable > 0:
        canvas.create_rectangle(options_center - 150, 120, options_center + 150, 180)
        canvas.create_text(options_center, 150, text = 'Soldier\t\t2G', font = 'Arial 20')


        

def drawCharacters(app,canvas):
    for character in app.characters:
        if type(character) == Archer:
            if character.owner == 'Kosbie':
                canvas.create_image(character.x * app.squareLength + app.border + app.squareLength // 2,
                                    character.y * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.archerK))
            else:
                canvas.create_image(character.x * app.squareLength + app.border + app.squareLength // 2,
                                    character.y * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.archerT))
        
        if type(character) == Soldier:
            if character.owner == 'Kosbie':
                canvas.create_image(character.x * app.squareLength + app.border + app.squareLength // 2,
                                    character.y * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.warriorK))
            else:
                canvas.create_image(character.x * app.squareLength + app.border + app.squareLength // 2,
                                    character.y * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.warriorT))

        if type(character) == Knight:
            if character.owner == 'Kosbie':
                canvas.create_image(character.x * app.squareLength + app.border + app.squareLength // 2,
                                    character.y * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.knightK))
            else:
                canvas.create_image(character.x * app.squareLength + app.border + app.squareLength // 2,
                                    character.y * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.knightT))


#draws images for each terrain
def drawBoard(app,canvas):
    for row in range(len(app.board)):
        for col in range(len(app.board)):
            if app.board[col][row] == 'Grass':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))
            
            elif app.board[col][row] == 'Ocean':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.waterBackground))

            elif app.board[col][row] == 'Mountain':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.mountainBackground))

            elif app.board[col][row] == 'Outpost':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.outpost))
            
            elif app.board[col][row] == 'OutpostTaylor':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.outpostT))

            elif app.board[col][row] == 'OutpostKosbie':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.outpostK))
            
            elif app.board[col][row] == 'Farm':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.farm))

            elif app.board[col][row] == 'FarmTaylor':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.farmT))
            
            elif app.board[col][row] == 'FarmKosbie':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.farmK))
            
            elif app.board[col][row] == 'BaseTaylor':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.baseT))
            
            elif app.board[col][row] == 'BaseKosbie':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.baseK))
            
           






def titleScreen_redrawAll(app,canvas):
    canvas.create_image(app.width//2, app.height//2,
                        image=ImageTk.PhotoImage(app.game_background))

    canvas.create_rectangle(app.width // 2 - 100, app.height // 2 + 165, app.width // 2 + 100, 
                            app.height // 2 + 235, fill = 'red')
    canvas.create_text(app.width//2, app.height//2 + 200, text = "Start", font = 'Arial 40', fill = 'white')

    

    

def titleScreen_mousePressed(app,event):
    if (event.x > app.width // 2 - 100 and event.x < app.width // 2 + 100 and
        event.y > app.height // 2 + 165 and event.y < app.height // 2 + 235):
            app.mode = 'LoreScreen'


def LoreScreen_redrawAll(app,canvas):
    canvas.create_image(app.width//2, app.height//2 - 75,
                        image=ImageTk.PhotoImage(app.game_lore))
    
    canvas.create_rectangle(app.width // 2 - 100, app.height // 2 + 260, app.width // 2 + 100, 
                            app.height // 2 + 330, fill = 'gray')
    canvas.create_text(app.width//2, app.height//2 + 295, text = "Next", font = 'Arial 40', fill = 'white')

def LoreScreen_mousePressed(app,event):
    if (event.x > app.width // 2 - 100 and event.x < app.width // 2 + 100 and
        event.y > app.height // 2 + 260 and event.y < app.height // 2 + 330):
            app.mode = 'gameMode'


runApp(width = 1200, height = 800)

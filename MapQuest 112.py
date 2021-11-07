from cmu_112_graphics import *

def appStarted(app):

    #board
    app.board = [
                   ['BaseKosbie','Grass','OutpostKosbie','Grass','Grass','Ocean'],
                   ['Grass','Grass','Grass','Farm','Grass','Ocean'],
                   ['OutpostKosbie','Grass','Grass','Grass','Grass','Ocean'],
                   ['Grass','Grass','Farm','Grass','Outpost','Grass'],
                   ['Grass','Grass','Grass','Mountain','Grass','Grass'],
                   ['Grass','Grass','Grass','Mountain','Grass','BaseTaylor']
                ]
    
    app.characters = []

    app.mode = 'titleScreen'
    app.border = 30
    app.squareLength = (app.height - 2 * app.border) // 6 #len(app.board)
    app.rows = 6 #len(app.board)
    app.cols = 6 #len(app.board[0])

    #loading images
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

    app.archerK = app.loadImage('Images/tiles/TA sprites/archers/alex_archer.png')
    app.archerK = app.scaleImage(app.archerK, app.squareLength/100)
    app.archerT = app.loadImage('Images/tiles/TA sprites/archers/asad_archer.png')
    app.archerT = app.scaleImage(app.archerT, app.squareLength/100)
    app.knightK = app.loadImage('Images/tiles/TA sprites/horseriders/zhara_horserider.png')
    app.knightK = app.scaleImage(app.knightK, app.squareLength/100)
    
    #app.warriorBen = app.loadImage('warriorben.png')
    #app.warriorBen = app.scaleImage(app.warriorBen, app.squareLength/100)

def gameMode_redrawAll(app,canvas):
    drawBoard(app,canvas)
    drawCharacters(app,canvas)

def drawCharacters(app,canvas):
    for character in app.characters:
        if type(character) == Archer:
            if character.owner == 'Kosbie':
                canvas.create_image(character.x * app.squareLength + app.border + app.squareLength // 2,
                                    character.y * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))
            else:
                canvas.create_image(character.x * app.squareLength + app.border + app.squareLength // 2,
                                    character.y * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))
        
        if type(character) == Soldier:
            if character.owner == 'Kosbie':
                canvas.create_image(character.x * app.squareLength + app.border + app.squareLength // 2,
                                    character.y * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))
            else:
                canvas.create_image(character.x * app.squareLength + app.border + app.squareLength // 2,
                                    character.y * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))

        if type(character) == Knight:
            if character.owner == 'Kosbie':
                canvas.create_image(character.x * app.squareLength + app.border + app.squareLength // 2,
                                    character.y * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))
            else:
                canvas.create_image(character.x * app.squareLength + app.border + app.squareLength // 2,
                                    character.y * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))


#draws images for each terrain
def drawBoard(app,canvas):
    for row in range(6):
        for col in range(6):
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
    canvas.create_text(app.width//2, app.height//2 - 60, text = "112 MapQuest", font = 'Arial 100')

    canvas.create_rectangle(app.width // 2 - 100, app.height // 2 + 50, app.width // 2 + 100, 
                            app.height // 2 + 150)
    canvas.create_text(app.width//2, app.height//2 + 100, text = "Start", font = 'Arial 40')

def titleScreen_mousePressed(app,event):
    if (event.x > app.width // 2 - 100 and event.x < app.width // 2 + 100 and
        event.y > app.height // 2 + 50 and event.y < app.height // 2 + 150):
            app.mode = 'gameMode'
            
            

runApp(width = 1200, height = 800)
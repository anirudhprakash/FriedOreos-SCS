from cmu_112_graphics import *

def appStarted(app):

    #board
    app.board = [
                   ['BaseKosbie','Grass','OutpostKosbie','Grass','Grass','Grass','Ocean','Ocean'],
                   ['Grass','Grass','Grass','Farm','Grass','Farm','Grass','Ocean'],
                   ['OutpostKosbie','Grass','Grass','Grass','Grass','Grass','Outpost','Ocean'],
                   ['Grass','Grass','Farm','Grass','Outpost','Grass','Grass','Ocean'],
                   ['Grass','Grass','Grass','Mountain','Grass','Grass','Farm','Grass'],
                   ['Grass','Grass','Grass','Mountain','Grass','Grass','Farm','OutpostTaylor'],
                   ['Mountain','Outpost','Grass','Farm','Grass','Grass','Grass','Grass'],
                   ['Grass','Mountain','Grass','Grass','Grass','OutpostTaylor','Grass','BaseTaylor']
                ]
    
    app.mode = 'titleScreen'
    app.border = 30
    app.squareLength = (app.height - 2 * app.border) // 6 #len(app.board)
    app.rows = 6 #len(app.board)
    app.cols = 6 #len(app.board[0])

    #loading images
    app.grassBackground = app.loadImage('grass.png')
    app.grassBackground = app.scaleImage(app.grassBackground, app.squareLength/100)
    app.warriorBen = app.loadImage('warriorben.png')
    app.warriorBen = app.scaleImage(app.warriorBen, app.squareLength/100)

def gameMode_redrawAll(app,canvas):
    drawBoard(app,canvas)
    drawCharacters(app,canvas)

def drawCharacters(app,canvas):
    pass

#draws images for each terrain
def drawBoard(app,canvas):
    for row in range(6):
        for col in range(6):
            if app.board[row][col] == 'Grass':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))
            
            elif app.board[row][col] == 'Ocean':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))

            elif app.board[row][col] == 'Mountain':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))

            elif app.board[row][col] == 'Outpost':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))
            
            elif app.board[row][col] == 'OutpostTaylor':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))

            elif app.board[row][col] == 'OutPostKosbie':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))
            
            elif app.board[row][col] == 'Farm':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))

            elif app.board[row][col] == 'FarmTaylor':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))
            
            elif app.board[row][col] == 'FarmKosbie':
                canvas.create_image(row * app.squareLength + app.border + app.squareLength // 2,
                                    col * app.squareLength + app.border + app.squareLength //2,
                                    image=ImageTk.PhotoImage(app.grassBackground))






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
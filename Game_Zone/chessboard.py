import turtle 

def draw_box(t,x,y,size,fill_color):
    t.penup() # no drawing!
    t.goto(x,y) # move the pen to a different position
    t.pendown() # resume drawing
    t.speed(0)
    t.fillcolor(fill_color)
    t.begin_fill()  # Shape drawn after this will be filled with this color!

    for i in range(0,4):
        board.forward(size) # move forward
        board.right(90) # turn pen right 90 degrees
 
    t.end_fill() # Go ahead and fill the rectangle!
 
 
def draw_chess_board():
    square_color = "black" # first chess board square is black
    start_x = -400 # starting x position of the chess board
    start_y = -300 # starting y position of the chess board
    box_size = 100 # pixel size of each square in the chess board
    for i in range(0,8): # 8x8 chess board
        for j in range(0,8):
            draw_box(board,start_x+j*box_size,start_y+i*box_size,box_size,square_color)
            square_color = 'black' if square_color == 'white' else 'white' # toggle after a column
        square_color = 'black' if square_color == 'white' else 'white' # toggle after a row!
    turtle.penup()
    turtle.pencolor("grey")
    turtle.goto(-400,-400)
    turtle.pendown()
    turtle.write("♖ ♗ ♘♔♕♘ ♗♖",font=("aerial",65,"bold"))
    turtle.penup()
    turtle.goto(-400,-300)
    turtle.pendown()
    turtle.write("♙ ♙ ♙♙ ♙♙♙♙",font=("aerial",65,"bold"))
    turtle.penup()
    turtle.goto(-400,300)
    turtle.pendown()
    turtle.pencolor("brown")
    turtle.write("♜ ♝ ♞♚♛♞ ♝♜",font=("aerial",65,"bold"))
    turtle.penup()
    turtle.goto(-400,200)
    turtle.pendown()
    turtle.pencolor("brown")
    turtle.write("♟ ♟ ♟♟ ♟♟♟♟",font=("aerial",65,"bold"))

board = turtle.Turtle()

draw_chess_board()
turtle.done()
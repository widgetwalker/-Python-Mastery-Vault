import turtle
ts=turtle.Screen()
t=turtle.Turtle()
t.speed(1)
    
def drawshape(hello):
    for i in range(hello):
        t.backward(100)
        t.left(360/hello)
    drawshape(4)
    
def psu():
    t.pendown()
    t.forward(100)
    t.right(90)
    t.pendown()
    t.forward(100)
    t.right(90)
    t.pendown()
    t.forward(100)
    t.left(90)
    t.pendown()
    t.forward(100)
    t.pendown()
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.pendown()
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.fillcolor("blue")
    

def dwawx(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()
    for i in range(4):
        t.right(45)
        t.forward(50)
        t.backward(50)
        t.right(45)
        
def drawo (x,y):
        t.pu()
        t.goto(x-40,y)
        t.pd()
        t.circle(40)
Turn=1
def getTurn(x,y):
    global Turn
    if Turn:
        drawx(x,y)
        Turn=1
    
psu()
ts.listen()
ts.onclick(getTurn)
ts.mainloop 
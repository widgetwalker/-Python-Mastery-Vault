import turtle

screen = turtle.Screen()
screen.setup(5000,5000)
screen.tracer(0)
screen.addshape("turtle.gif")   # register the image with the screen as a shape

don = turtle.Turtle()
don.speed(0)
don.shape("turtle.gif")         # now set the turtle's shape to it

don.penup()
don.goto(-350, 0)

while True :
    screen.update()
    don.forward(0.01)
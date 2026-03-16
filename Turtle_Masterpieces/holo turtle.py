import turtle
t=turtle.Turtle()
colors=["red","blue","green","orange","violet","gold"]
turtle.speed(200)
for i in range(360):
    t.penup()
    turtle.pencolor(colors[i%6])
    turtle.bgcolor("black")
    turtle.width(i/100+2)
    turtle.circle(50)
    turtle.right(10)
    turtle.left(105)
    turtle.circle(120)
    turtle.right(120)   
    turtle.circle(170)
    turtle.circle(220)
    turtle.right(100)
    
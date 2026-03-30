import turtle
colors=["white","red","yellow"]
for x in range(360):
    turtle.hideturtle()
    turtle.bgcolor("black")
    turtle.pencolor(colors[x%3])
    turtle.width(x/100+1)
    turtle.backward(x)
    turtle.right(59)
    turtle.forward(20)
    turtle.right(90)
    turtle.speed(0)

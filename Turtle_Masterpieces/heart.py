import turtle as t
t.speed(0)
t.left(90)
def curve():
    for i in range(200):
        t.right(2)
        t.forward(2)

def heart():
    t.fillcolor("red")
    t.begin_fill()
    t.left(40)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()
def text():
    t.penup()
    t.setpos(-68,95)
    t.pendown()
    t.pencolor("green")
    t.write("HAPPY VALENTINES DAY",font=("lucida",30,"bold"))

heart()
text()
t.ht()
import random
import turtle

turtle.hideturtle()
turtle.speed("fastest")
turtle.color("blue")
turtle.tracer(0, 0)

points = [[-400, -300], [400, -300], [0, 292]]

def dot():
    turtle.forward(1)
    turtle.up()
    turtle.left(180)
    turtle.forward(1)
    turtle.left(180)
    turtle.down()

for x in range(0, 3):
    turtle.up()
    turtle.goto(points[0])
    del points[0]
    turtle.down()
    dot()

def newPoint():
    ran = random.randint(1, 3)

    if(ran == 1):
        point = [-400, -300]
    if(ran == 2):
        point = [400, -300]
    if(ran == 3):
        point = [0, 292]
    return point

def getMid(p1,p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def printAll():
    point = newPoint()
    print(getMid(point, turtle.pos()))

def draw():
    turtle.up()
    turtle.goto(getMid(newPoint(), turtle.pos()))
    turtle.down()
    dot()

for x in range(0, 10000):
    draw()
    print(x)

window = turtle.Screen()
window.setup(width=1.0, height=1.0)
window.exitonclick()

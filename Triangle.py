import random
import turtle
import time
import math

turtle.hideturtle()
turtle.speed(10)
turtle.color("blue")

points = [[0, 0], [100, 0], [50, 74]]

def dot():
    turtle.forward(1)

for x in range(0, 3):
    turtle.up()
    turtle.goto(points[0])
    del points[0]
    turtle.down()
    dot()

def newPoint():
    ran = random.randint(1, 3)

    if(ran == 1):
        point = [0, 0]
    if(ran == 2):
        point = [100, 0]
    else:
        point = [50, 74]
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

for x in range(0, 2000):
    draw()

window = turtle.Screen()
window.exitonclick()

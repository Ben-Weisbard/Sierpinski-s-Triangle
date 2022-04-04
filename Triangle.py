import turtle
import time

turtle.hideturtle()

points = [100, 100, 50, 0, 150, 0]

for x in range(0, 3):
    turtle.up()
    turtle.goto(points[x], points[x + 1])
    turtle.down()
    turtle.forward(1)
    x + 1

time.sleep(10)

from turtle import * 
from random import randint

pencil = Turtle()

for i in range(10):
    # coords
    x = randint(-200, 200)
    y = randint(-150, 150)

    color = (randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255)

    radius = randint(10, 110)

    pencil.up()
    pencil.goto(x, y)
    pencil.down()

    pencil.color(color)
    pencil.begin_fill()
    pencil.circle(radius)
    pencil.end_fill()


done()
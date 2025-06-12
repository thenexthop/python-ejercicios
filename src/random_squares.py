from turtle import *
from random import randint


pencil = Turtle()

pencil.speed(5)
pencil.pensize(5)

for i in range(4):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)    
    color = (r/255, g/255, b/255)
    #print("Color: ", color)
    pencil.color(color)

    pencil.forward(100)
    pencil.right(90)

done()
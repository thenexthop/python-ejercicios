import turtle as t

t1 = t.Turtle()
t1.speed(0)

side_length = 100
angle = 72

for _ in range(5):
    t1.forward(side_length)
    t1.left(angle)    

t.done()

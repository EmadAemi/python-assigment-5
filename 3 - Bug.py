import turtle

t = turtle.Pen()
t.speed(1)

def reset():
    t.penup()
    t.forward(5)
    t.pendown()


i = 3
while i <= 10:
    angle = 360 / i
    reset()
    for j in range(i):
        t.left(angle)
        t.forward(i*10)
    i += 1

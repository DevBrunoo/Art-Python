import turtle
import colorsys
t = turtle.Turtle()
turtle.Screen().bgcolor("DarkSlateGray")
t.pensize(2)
t.speed(0)
n = 37
h = 0
for i in range(90):
    c = colorsys.rgb_to_hsv(0.250, 0.235, 0.250)
    h+=1/n
    t.pencolor(c)
    for j in range(5):
        t.forward(i-3)
        t.right(9*5)
        t.left(8)
    t.right(115)
turtle.done()



import turtle
import colorsys
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.pensize(2)
t.speed(0)
n = 36
h = 0
for i in range(90):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    t.pencolor(c)
    for j in range(5):
        t.forward(i-3)
        t.right(9*5)
        t.left(8)
    t.right(115)
turtle.done()

''' 
Colorys e uma biblioteca que converte cores bidimensionais em numeros
Turtle e a biblioteca responsavel por mondular as cores em formato de desenho ou seja criar o desenho
turtle.Screen().bgcolor("black") e usado para dar a cor preta no fundo
t.pensize(2) esse e um metodo utilizado para definir a largura da linha
t.spreed(0) e para definir o tempo
t.forward e responsavel por mover a tartaruga para frene
t.right e usado para dar movimento a tartaruga
pencolor e para mudar as cores
'''
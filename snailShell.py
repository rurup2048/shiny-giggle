import turtle

wn = turtle.Screen()
ru = turtle.Turtle()

sides = 17

for i in range(1,sides + 1):
    ru.forward(i * 25)
    ru.left(90)

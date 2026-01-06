import turtle

wn = turtle.Screen()
ru = turtle.Turtle()

shift = 1
sides = 1
for j in range(1,20):
    for i in range(1,shift + 1):
        shift = j // 360
        ru.forward(100)
        ru.left(shift)
    wn.clear()
    # wn = turtle.Screen()
    ru = turtle.Turtle()
wn.mainloop()

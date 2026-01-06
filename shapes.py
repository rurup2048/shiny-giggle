import turtle

wn = turtle.Screen()
ru = turtle.Turtle()

#sides = 9

def crazyShapes(sides):
    shift = 180 / sides - 180
    for i in range(1, sides + 1):
        
        ru.forward(200)
        ru.left(shift)
        print(shift)
        
    wn.mainloop()

crazyShapes(9)

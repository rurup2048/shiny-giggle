import turtle

ru = turtle.Turtle()
wn = turtle.Screen()
colors = ["yellow","blue","green"]

def square(size, turtle, color):
    '''draws a rhombus with 60-120-60-120 angles
    draws the acute angle first, moves counterclockwise
    ru: turtle
    side: side length
    '''
    #turtle.setheading(angle)

    for i in range(2):
        turtle.fillcolor(color)
        
        turtle.begin_fill()
        
        turtle.forward(size)
        turtle.left(120)
        
        turtle.forward(size)
        turtle.left(60)
        
        turtle.end_fill()

ru.setheading(30)
size = 100

for i in range(1,4):
     ru.right(120)
     square(size, ru, colors[i-1])
ru.hideturtle()

ru.penup()
ru.setheading(90)
ru.forward(size + 20)
ru.left(90)
ru.forward(70)
ru.write("AOPS", font=("Verdana",50, "normal"))

wn.mainloop()
ru.bye()

import turtle

wn = turtle.Screen()
ru = turtle.Turtle()

ru.left(90)

for i in range(1,13):
    ru.penup()
    ru.stamp()
    ru.right(30+75) 
    ru.forward(60)
    ru.left(75) 
    #print(turtle.pos())
#ru.right(105)
ru.setheading(-90)
ru.forward(115)
#print(turtle.pos())

ru.pendown()
ru.hideturtle()
ru.pensize(2.5)

hour = int(input("the hour -> "))
ru.setheading(hour * -30 + 90)
ru.forward(30)
ru.stamp()
ru.right(180)
ru.forward(30)

mins = int(input("the minute -> "))
ru.setheading(mins * -6 + 90)
ru.forward(70)
ru.stamp()
ru.right(180)
ru.forward(70)
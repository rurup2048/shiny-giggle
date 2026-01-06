import turtle

wn = turtle.Screen()
ru = turtle.Turtle()

sqLen = 40
numSq = 8

#for more felxabity
#sqLen = int(input("how long are squares"))
#numSq = int(input("how many squares"))

for i in range(1,numSq + 1):
    for i in range(1,5):
        ru.forward(sqLen)
        ru.right(90)
    ru.forward(sqLen)

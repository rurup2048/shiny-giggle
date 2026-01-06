qwerty = 1
factors = int(input("int -> "))
if factors > 0:
    for i in range(1,factors + 1):
        qwerty = qwerty * i
        print(str(i) + " -> " + str(qwerty))
    print("fin -> "+ str(qwerty))

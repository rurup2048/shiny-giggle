def move(x,y):
    global b
    global time
    b[x] -= 1
    b[y] += 1
    time += 1
    
def CanGoLeft():
    global b
    temp = False
    for i in range(len(b)-1):
        if b[i] > b[i+1]:
            temp = True
    return temp
def CanGoRight():
    global b
    temp = False
    for i in range(len(b)-1):
        if b[i] < b[i+1]:
            temp = True
    return temp
def maxLoc():
    global b
    maxscr = 0
    maxLox = -1
    for i in range(len(b)):
        if maxscr < b[i]:
            maxscr = b[i]
            maxLox = i
    return maxLox
n, x = list(map(int, input().split()))
b = list(map(int, input().split()))
time = 0
if x == 1:
    temp = True
    for i in range(len(b)-1):
        if b[i] <= b[i+1]:
            temp = False
    while CanGoLeft():
        for i in range(len(b)-1):
            if b[i] > b[i+1]:
                move(i, i+1)
                
    while CanGoRight():
        for i in range(len(b)-1):
            if b[i] < b[i+1]:
                move(i+1, i) 
else:
    while min(b) != max(b):
        endLoc = maxLoc()-1
        try:
            if b[maxLoc()-1] > b[maxLoc()+1]:
                endLoc = maxLoc()+1
        except:
            r = 'rizz'
        move(maxLoc(),endLoc)
print(time)

# s, n = list(map(int,input().split()))
# enemys = list(map(int,input().split()))
s, n = [100,5]
enemys = [125, 20, 250, 200, 150]
aura = 0
hp = s
def canFight(i):
    if hp > i:
        return True
    else:
        return False
def fight(i):
    global hp
    global aura
    hp = hp - i
    enemys.remove(i)
    aura += 1
def canRecruit(i):
    if aura <= 1:
        return True
    else:
        return False
def recruit(i):
    global hp
    global aura
    hp += i
    enemys.remove(i)
    aura -= 1

def risk(l):
    global hp
    elist = enemys
    elist.sort()
    amount = 0
    w = 0
    while amount + elist[w] < hp:
        amount = amount + elist[w]
        w += 1
    return w

if canFight(min(enemys)):
    fight(min(enemys))
    if canRecruit(max(enemys)):
        recruit(max(enemys))
        while risk(enemys) > 1:
            while canFight(min(enemys)):
                fight(min(enemys))
            if risk(enemys[:len(enemys)-1]) > 1:
                recruit(max(enemys))
        print(aura)
            
else:
    print('0')


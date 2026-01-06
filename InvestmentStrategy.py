money = 1
for i in range(1,int(input())+1):
    if i%10 == 8:
        money = money//2
    if i%3 == 0:
        money += i
    if i%2 == 0:
        money += money//10
print(money)
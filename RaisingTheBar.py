dice = [4,6,8,10,12,20]
lastRoll = 0
for r1 in range(1,5):
    for r2 in range(1,7):
        for r3 in range(1,9):
            for r4 in range(1,11):
                for r5 in range(1,13):
                    for r6 in range(1,21):
                        if r2 >= r1 and r3 >= r2 and r4 >= r3 and r5 >= r4 and r6 >= r5:
                            lastRoll += 1
                        
print(lastRoll)
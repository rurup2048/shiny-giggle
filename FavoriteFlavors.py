q = int(input())
# q =10
#  testCases = [['A','BESSIE','CHOCOLATE'],['A','JESSIE','VANILLA'],['A','ESSIE','CHOCOLATE'],['A','ESSIE','VANILLA'],['A','JESSIE','STRAWBERRY'],['B','ESSIE'],['C','VANILLA'],['D','VANILLA'],['B','ESSIE'],['C','VANILLA']]
testCases = []
for j in range(q):
    testCases.append(list(map(str,input().split())))

cowProfile = []
flavorProfile = []
for test in testCases:
    cmd = test[0]
    kf = test[1:] 
    if cmd == 'A':
        end = True
        # print(kf[0])
        # print(cowProfile)
        # print(kf[0] not in cowProfile)
        # print(kf[1])
        # print(flavorProfile)
        # print(kf[1] not in flavorProfile)
        for i in range(len(cowProfile)):
            if cowProfile[i] == kf[0] and cowProfile[i] == kf[1]:
                end = False
        if end:
            cowProfile.append(kf[0])
            flavorProfile.append(kf[1])
            # print(cowProfile)
            # print(flavorProfile)
            # print('-------------')
    elif cmd == 'B':
        print(cowProfile.count(kf[0]))
    elif cmd == 'C':
        print(flavorProfile.count(kf[0]))
    else:
        for i in range(len(flavorProfile)-flavorProfile.count(kf[0])):
            # print('__')
            # print(i)
            if flavorProfile[i] == kf[0]:
                flavorProfile.pop(i)
                cowProfile.pop(i)
    
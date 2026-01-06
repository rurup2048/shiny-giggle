def isNext(p1,p2):
    copyP1 = list(p1)
    copyP1[len(p1)-1] = chr((((ord(copyP1[len(p1)-1])-65)+1)%26)+65)
    if copyP1[len(p1)-1] == 'A':
        for c in range(len(p1)-2,-1,-1):
            copyP1[c] = chr((((ord(copyP1[c])-65)+1)%26)+65)
            if copyP1[c] != 'A':
                break
    if copyP1 == list(p2):
        return True
    else:
        return False
        
        
for i in range(int(input())):
    testCase = str(input())
    firstPart = testCase[:len(testCase)//2]
    secondPart = testCase[len(testCase)//2:]
    if isNext(firstPart,secondPart):
        print('YES')
    else:
        print('NO')
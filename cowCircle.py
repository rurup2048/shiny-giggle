
def find(thing, nlist):
    nlist = list(nlist)
    for i in nlist:
        if thing == i:
            return nlist.index(i)
    return -1
        
        

def solve(numCows,rounds,cowPos):
    cows = list(range(1,numCows+1))
    for r in range(rounds):
        if r % 2 == 1:
            for i in range(0,numCows,2):
                cows[i%numCows], cows[(i+1)%numCows] = cows[(i+1)%numCows], cows[i%numCows]
        else:
            for i in range(numCows,0,-2):
                cows[i%numCows], cows[(i-1)%numCows] = cows[(i-1)%numCows], cows[i%numCows]
    
    endCowPos = find(cowPos, cows)
    return str(cows[(endCowPos-1)%numCows])+' '+ str(cows[(endCowPos+1)%numCows])
# print(solve(8, 2, 3))
# text = list(input().strip().split())
text = list('5 78 3'.strip().split())
print(solve(int(text[0]), int(text[1]), int(text[2])))

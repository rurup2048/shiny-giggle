import itertools

n, s = list(map(str,input().split()))
n = int(n)
f = (n-(n%3))+2
maxCows = 'COW'*f
amount = 0
cs = list(itertools.permutations(maxCows))
cows = []
for i in cs:
    temp = i[0:n]
    if temp in cows:
        pass
    else:
        cows.append(temp)
print(cows)
r = ''
for cow in cows:
    print(r.join(list(s)))
    print(r.join(list(cow)))
    print(list(s) in list(cow))
    print('------------')
    if r.join(list(s)) in r.join(list(cow)):
        amount += 1

print(str(amount))
        
    
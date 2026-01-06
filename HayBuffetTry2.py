n  = int(input())
f = list(map(int,input().split()))
tf = f
tf.sort()
tf.reverse()
total = [tf[0]]
for i in range(1,len(f)):
    if abs(total[-1] - tf[i]) >= 10:
        total.append(tf[i])
print(sum(total))
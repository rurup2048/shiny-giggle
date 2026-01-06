n = int(input())
stacks = [n]
while max(stacks) > 2:
    t = max(stacks)
    stacks.remove(t)
    stacks.append(t//2)
    stacks.append(t-(t//2))
print(len(stacks))
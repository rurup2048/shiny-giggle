def fib(j1,j2,n):
    '''fib(n) -> int
    returns the nth Fibonacci number'''
    fibSec = [j1,j2]
    if n <= 1:  # base cases
        return n
    for i in range(1, n):
        newFibSec = fibSec[i] + fibSec[i - 1]
        fibSec.append(newFibSec)
    return fibSec[-1]
import random
i = [6,12,13,2]
# i = [random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,3)]
# i = input().strip().split()
fibSec = str(fib(int(i[0]), int(i[1]), int(i[2])))
end = fibSec[int(i[3])*-1:]
# print(str(end)+':'+str(fibSec))
print(str(int(end)))
def fib(n):
    '''fib(n) -> int
    returns the nth Fibonacci number
    '''
    fibSec = [1,1]
    
    if n <= 1:  # base cases
        return n
    
    for i in range(1 , n - 1):
        newFibSec = fibSec[i] + fibSec[i - 1]
        fibSec.append(newFibSec)
    return fibSec[-1]

# i = input().strip().split()
for i in range(1,10):
    print(fib(i))
#1,1,2,2,2
#1,1,2,2,3,3,4,5,5




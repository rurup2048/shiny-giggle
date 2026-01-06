def week1_Q2():
    numRound = 1
    theRange = 100
    while numRound < theRange:
        #n = int(input("number"))
        n = numRound # Step 1: Have the user input an integer -- call it $n$.
        n = n + 4 # Step 2: Add 4 to $n.$
        m = n * 3 # Step 3: Multiply the sum by 3.
        p = n + m # Step 4: Add $n$ to this product.
        q = p / 2 # Step 5: Divide this sum by 2.
        r = q + 4 # Step 6: Add 4 to this quotient.
        o = r / 2 # Step 7: Divide this new sum by 2.
        s = n - o # Step 8: Subtract $n$ from this new quotient.
        print("the anc = ",s) #Step 9: Output this difference.
        numRound+= 1
        
N = 6
n = 1
Sum = 0
while n > N:
    Sum = Sum + (n*2-1)
    n+=1
print(Sum)
 11+9+7+5+3+1
 n

 1:4
 2:3
 3:7
 4:2
 5:6
 6:1
 7:8
 8:5

def test1():
    def base10_to_base3(q):
        if q == 0:
            return "0"  
    
        result = ""
        while q > 0:
            remainder = q % 3
            result = str(remainder) + result
            q //= 3
    
        return result
    
    for i in range(28):
        t = base10_to_base3(i)
        print(str(i)+':\t\t'+ ((2 - len(t)) * '0') + t)
def test2():
    import itertools
    c = itertools.product([0, 1], repeat=3)
    print(c)
test2()
def sum_of_integers(n):
    '''returns the sum of the first n positive integers'''
    total = 0               # running total, initialize at 0

    for i in range(1, n+1): # current number to add, goes from 1 to n
        total += i          # add the current number to our total

    return total
    
    # output the answer
def strip_right_digit(num):
    """strip_right_digit(num) -> int
    Returns num with its rightmost digit removed
    num: a non-negative integer.
    """
    return num // 10

def get_place(num, place):
    """get_place(num, place) -> int
    Returns the digit in the decimal place corresponding to
    place-th position (from the right) in positive num.
    """
    for i in range(place):
        num = strip_right_digit(num)
        
    return num % 10   # return rightmost digit of num
  

number = int(input("int please -> "))
place = int(input("place please -> "))
    
print(get_place(number, place))  
#print(sum_of_integers(number))
#print(strip_right_digit(number))

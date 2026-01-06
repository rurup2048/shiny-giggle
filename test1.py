scores = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,
          'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,
          'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}

infile = open('wordlist.txt','r')
words = infile.read().split()
biggestWord = {'':0}
Sum = 0
for word in words:
    word.strip()
    for letter in word:
        Sum += scores[letter.upper()]
    #print(Sum)
    print(biggestWord)
    #print(int(list(biggestWord.values())[0]))
    if int(list(biggestWord.values())[0]) < Sum:
        if not 'Z' in word.upper():
            biggestWord.clear()
            biggestWord[word] = Sum
    Sum = 0
print(biggestWord)

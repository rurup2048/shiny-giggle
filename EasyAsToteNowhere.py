wordList = list(input())
endStr = []
for i in range(wordList.count('Z')):
    endStr.append('0')
    wordList.remove('Z')
    wordList.remove('E')
    wordList.remove('R')
    wordList.remove('O')
for i in range(wordList.count('w')):
    endStr.append('2')
    wordList.remove('T')
    wordList.remove('W')
    wordList.remove('O')
for i in range(wordList.count('F')):
    endStr.append('5')
    wordList.remove('F')
    wordList.remove('I')
    wordList.remove('V')
    wordList.remove('E')
for i in range(wordList.count('X')):
    endStr.append('6')
    wordList.remove('S')
    wordList.remove('I')
    wordList.remove('X')
for i in range(wordList.count('U')):
    endStr.append('4')
    wordList.remove('F')
    wordList.remove('O')
    wordList.remove('U')
    wordList.remove('R')
for i in range(wordList.count('G')):
    endStr.append('8')
    wordList.remove('E')
    wordList.remove('I')
    wordList.remove('G')
    wordList.remove('H')
    wordList.remove('T')
# phase 2
for i in range(wordList.count('V')):
    endStr.append('7')
    wordList.remove('S')
    wordList.remove('E')
    wordList.remove('V')
    wordList.remove('E')
    wordList.remove('N')
for i in range(wordList.count('R')):
    endStr.append('3')
    wordList.remove('T')
    wordList.remove('H')
    wordList.remove('R')
    wordList.remove('E')
    wordList.remove('E')
for i in range(wordList.count('O')):
    endStr.append('1')
    wordList.remove('O')
    wordList.remove('N')
    wordList.remove('E')
# phase 3
for i in range(wordList.count('I')):
    endStr.append('9')
    wordList.remove('N')
    wordList.remove('I')
    wordList.remove('N')
    wordList.remove('E')
    
endStr.sort()
end = ''
temp = 0
for i in range(len(endStr)):
    if endStr[i] != '0':
        end += endStr[i]
    else:
        temp += 1
end += '0' * temp
print(end)

    
MT = {'1': {'1': '1', 'i': 'i',  'j': 'j',  'k': 'k'},
       'i': {'1': 'i', 'i': '-1', 'j': 'k',  'k': '-j'},
       'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
       'k': {'1': 'k', 'i': 'j',  'j': '-i', 'k': '-1'}}
for r in range(int(input())):
    testCase = list(str(input()))[1:-4]
    for y in range(len(testCase)-1):
        t1 = testCase.pop(0)
        t2 = testCase.pop(0)
        testCase.insert(0, MT[t1[-1]][t2[-1]])
    if testCase[0] == '-1':
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
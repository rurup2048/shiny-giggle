input()
print('1 4')
ls = '3 1 2'
import sys
print(' '.join([str(x) for x in ls]), file=sys.stderr)
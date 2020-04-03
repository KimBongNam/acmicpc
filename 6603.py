import sys
from itertools import combinations

while True:
    lst = sys.stdin.readline().split()
    if lst[0] == '0':
        break
    else:
        a = list(combinations(lst[1:],6))
        for i in a:
            print(*i)
        print()
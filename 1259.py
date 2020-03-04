import sys
from collections import deque

val = 1

def pelindrome(lst):
    lst = deque(lst)
    if len(lst) < 2:
        return 'yes'
    else:
        if lst.popleft() == lst.pop():
            return pelindrome(lst)
        else:
            return 'no'

while val != 0:
    val = sys.stdin.readline().strip()
    if val=='0':
        break
    lst = [i for i in val]
    ans = pelindrome(lst)
    print(ans)
    
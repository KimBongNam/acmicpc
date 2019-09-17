import sys

inp = sys.stdin.readlines()
for i in inp:
    lst = list(map(int,i.split()))
    print(lst[0]+lst[1])
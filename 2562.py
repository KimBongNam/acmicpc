import sys

lst = list(map(int, sys.stdin.readlines()))
a = max(lst)
print(a)
print(lst.index(a)+1)
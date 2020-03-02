import sys
T = int(input())
lst = [sys.stdin.readline().split() for i in range(T)]

for i in lst:
    for j in i[1]:
        print(j*int(i[0]), end='')
    print()
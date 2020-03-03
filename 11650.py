import sys
N = int(input())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lst.sort()
for i in lst:
    print(i[0], end=' ')
    print(i[1])
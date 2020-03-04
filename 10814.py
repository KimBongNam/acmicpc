import sys
N = int(input())
lst = [sys.stdin.readline().split() for _ in range(N)]
ans = sorted(lst, key = lambda x: int(x[0]))
for i in ans:
    print(i[0], i[1])
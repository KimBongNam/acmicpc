import sys

N, M = map(int,input().split())
hear = [sys.stdin.readline().strip() for _ in range(N)]
see = [sys.stdin.readline().strip() for _ in range(M)]

ans = sorted(list(set(hear).intersection(set(see))))
print(len(ans))
for i in ans:
    print(i)
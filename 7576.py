import sys
M, N = map(int, input().split())
6 4

lst = [list(map(int, sys.stdin.readline.split())) for _ in range(N)]
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

fir = []
for i in range(M):
    fir.append(any(i))

if not any(fir):
    print(0)
else:
    for i in range(M):
        for j in range(N):
            
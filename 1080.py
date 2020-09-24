import sys

N, M = map(int, input().split())
lst = [list(sys.stdin.readline().strip()) for _ in range(N)]
res = [list(sys.stdin.readline().strip()) for _ in range(N)]

ans = 0
for i in range(N-2):
    for j in range(M-2):
        if lst[i][j] != res[i][j]:
            for a in range(3):
                for b in range(3):
                    if lst[i+a][j+b] == '1':
                        lst[i+a][j+b] = '0'
                    else:
                        lst[i+a][j+b] = '1'
            ans += 1

for i in range(N):
    for j in range(M):
        if lst[i][j] != res[i][j]:
            ans = -1
            break

print(ans)
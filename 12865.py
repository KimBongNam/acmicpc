import sys

N, K = map(int, input().split())

lst = [[0,0]]
for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    lst.append([W,V])

lst.sort(key = lambda x: x[1], reverse=True)
lst.sort()
dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,K+1):
        if j < lst[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-lst[i][0]]+lst[i][1], dp[i-1][j])

print(max(dp[-1]))
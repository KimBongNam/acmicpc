import sys

N, K = map(int, input().split())
4 7
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
6 13
4 8
3 6
5 12
dp = [[0,0]]
for i in range(N):
    a = lst[i]
    for j in range(i+1):
        if dp[j][0] + lst[i][0] <= K:
            if a[1] < dp[j][1] + lst[i][1] :
                a = [dp[j][0]+lst[i][0], dp[j][1]+lst[i][1]]
            elif a[1] == dp[j][1] + lst[i][1]:
                a = min(a, [dp[j][0]+lst[i][0], dp[j][1]+lst[i][1]])
    dp.append(a)

print(max(dp, key=lambda x: x[1]))
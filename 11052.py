N = int(input())
4
lst = list(map(int, input().split()))
1 5 6 7
dp = [0]
for i in range(N):
    dp.append(max(dp[i]+lst[0], lst[i]))
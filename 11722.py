num = int(input())
lst = list(map(int,input().split()))

dp = []
for i in range(num):
    dp.append(1)
    for k in range(i):
        if lst[i] < lst[k]:
            dp[i] = max(dp[k]+1, dp[i])


print(max(dp))
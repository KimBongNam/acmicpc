num = int(input())
lst = list(map(int,input().split()))

dp = []
for i in range(num):
    dp.append(lst[i])
    if dp[i-1] > 0 and i > 0:
        dp[i] = dp[i-1] + lst[i]
print(max(dp))
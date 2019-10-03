num = int(input())
lst = list(map(int,input().split()))

dp = []
for i in range(num):
    dp.append(lst[i])
    for k in range(i):
        if lst[i] > lst[k]:
            dp[i] = max(dp[k]+lst[i], dp[i])


print(max(dp))
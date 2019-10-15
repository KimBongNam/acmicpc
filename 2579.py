import sys

num = int(input())
lst = list(map(int, sys.stdin.readlines()))
dp = []
for i in range(num):
    if i == 0:
        dp.append(lst[i])
    elif i < 2:
        dp.append(lst[i])
        dp[i] = dp[i-1]+lst[i]
    elif i == 2:
        dp.append(lst[i])
        dp[i] = max(lst[0]+lst[2], lst[1]+lst[2])

    else:
        dp.append(lst[i])
        dp[i] = max(dp[i-2]+lst[i], dp[i-3]+lst[i-1]+lst[i])

print(dp[num-1])
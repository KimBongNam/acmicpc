import sys

inp = list(map(int,sys.stdin.readlines()))
num = inp[0]
wine = inp[1:]
dp = [0]
for i in range(num):
    if i < 2:
        dp.append(dp[i]+wine[i])
    elif i == 2:
        dp.append(max(wine[i-2]+wine[i], wine[i-1]+wine[i],dp[i]))
    else:
        dp.append(max(dp[i],dp[i-1] + wine[i],dp[i-2]+wine[i-1]+wine[i]))
    
print(dp[num])
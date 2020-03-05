from math import sqrt

num = int(input())
11339
dp = [0]
for i in range(1, num+1):
    cnt = 0
    while i != 0:
        i = i-pow(int(sqrt(i)),2)
        cnt += 1
    k = 1
    while i - (k**2) >0:
        cnt = min(cnt, dp[i-(k**2)]+1)
        k += 1
    dp.append(cnt)

print(dp[-1])
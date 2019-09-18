import sys

num = list(map(int,sys.stdin.readlines()))
num.pop(0)
dp = [0,1,2,4]
for i in range(4,max(num)+1):
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])

for j in num:
    print(dp[j])
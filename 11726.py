num = int(input())
dp = [0,1,2]
for i in range(3,num+1):
    dp.append(dp[i-1]+dp[i-2])

print(dp[num]%10007)
num = list(map(int,input().split()))
dp = [[_ for _ in range(1,201)] for i in range(1,201)]
for i in range(1,num[0]):
    for j in range(1,num[1]):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[num[0]-1][num[1]-1]%1000000000)
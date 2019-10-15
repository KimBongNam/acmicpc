num = int(input())
dp = [1] * 100000
for i in range(1,num):
    dp[i] = num
    for j in range(1,i):
        if j*j > i:
            break
        else:
            dp[i] = min(dp[i-j*j]+1, dp[i])


print(dp[num-1])
num = int(input())
dp = [0,0,3,0,11]
if num > 4:
    for i in range(5,num+1):
        if i % 2 == 1:
            dp.append(0)
        else:
            value = 0
            for j in range(4, i+1, 2):
                value += dp[i-j] * 2
            dp.append(dp[i-2] * 3 +value + 2)

print(dp[num])
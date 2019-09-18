num = int(input())
dp = [[0]*10]*101
for i in range(1,num+1):
    if i <= 1:
        dp[i] = [0,1,1,1,1,1,1,1,1,1]
    else:
        lst = []
        for j in range(10):
            if j ==0:
                lst.append(dp[i-1][1])
                
            elif j == 9:
                lst.append(dp[i-1][8])
            else:
                lst.append(dp[i-1][j-1]+dp[i-1][j+1])
        dp[i] = lst


sum = 0
for _ in dp[num]:
    sum += _
print(sum%1000000000)
print(dp[1])
print(dp[2])
print(dp[3])
print(dp[4])
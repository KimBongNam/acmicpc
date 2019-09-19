num = int(input())

dp = [[0],[0,1]]
for i in range(2,num+1):
    lst = [0,0]
    for j in range(2):
        if j == 0:
            lst[0] = dp[i-1][0] + dp[i-1][1]
        else:
            lst[1] = dp[i-1][0]
    dp.append(lst)
sum = 0
for _ in dp[num]:
    sum += _
print(sum)

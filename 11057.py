num = int(input())
dp = [[0],[1,1,1,1,1,1,1,1,1,1]]
for i in range(2,num+1):
    lst = []
    for j in range(10):
        s = 0
        for m in range(j+1):
            s += dp[i-1][m]
        lst.append(s)

    dp.append(lst)
sum = 0
for k in dp[num]:
    sum += k
print(sum%10007)
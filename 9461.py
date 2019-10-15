import sys
inp = list(map(int, sys.stdin.readlines()))
for i in range(inp[0]):
    dp = [1,1,1,2,2,3,4,5]

    for j in range(8,inp[i+1]):
        dp.append(dp[j-1]+dp[j-5])
    print(dp[inp[i+1]-1])

    # 2 9 10 -> 7 9
import sys

inp = sys.stdin.readlines()
num = int(inp[0])

for i in range(num):
    test_case = int(inp[3*i + 1])
    first = list(map(int, inp[3 * i + 2].split()))
    second = list(map(int, inp[3 * (i+1)].split()))
    lst = [first,second]

    dp = [[],[]]
    for j in range(test_case):
        if j > 1:
            dp[0].append(max(dp[1][j-1], dp[1][j-2]) + lst[0][j])
            dp[1].append(max(dp[0][j-1], dp[0][j-2]) + lst[1][j])
        elif j == 0:
            dp[0].append(lst[0][j])
            dp[1].append(lst[1][j])
        else:
            dp[0].append(dp[1][j-1] +lst[0][j])
            dp[1].append(dp[0][j-1] + lst[1][j])

    print(max(dp[0][test_case-1], dp[1][test_case-1]))
    print(dp)


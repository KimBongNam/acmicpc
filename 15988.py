import sys
T = int(input())

dp = [0,1,2,4]
for i in range(4,1000001):
        dp.append((dp[i-3]+dp[i-2]+dp[i-1])%1000000009)
    
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp[n])


"""
import sys
T = int(input())
for _ in range(T):
    a = 1
    b = 2
    c = 4
    n = int(sys.stdin.readline())
    for i in range(4,n+1):
        a,b,c = b,c,a+b+c
    print(c%1000000009)
"""
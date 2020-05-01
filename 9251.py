A = input()
ACAYKP
B = input()
CAPCAK
l= max(A,B, key=lambda x:len(x))
if l == A:
    s = B
else:
    s = A
dp = [[0] * (len(l)+1) for _ in range(len(s)+1)]
for row in range(1,len(s)+1):
    for col in range(1,len(l)+1):
        if s[row-1] == l[col-1]:
            dp[row][col] = dp[row-1][col-1]+1
        else:
            dp[row][col] = max(dp[row][col-1], dp[row-1][col])

print(max(dp[-1]))
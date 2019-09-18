num = int(input())
'''
dp = [0,1,3]
for i in range(3,num+1):
    dp.append(2*dp[i-2]+dp[i-1])

print(dp[num]%10007)
'''
tmp = 0
a = 1
b = 1
for i in range(2,num+1):
    tmp = a
    a = b
    b = 2*tmp+b
print(b%10007)
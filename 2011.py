num = input()
dp = [1,1]
lst = ['1','2','3','4','5','6']
if num[0] != '0':
    for i in range(len(num)):
        if num[i-1] == '1' or (num[i-1] == '2' and num[i] in lst):
            dp.append(dp[i]+dp[i+1])
            print('sss')
        else:
            dp.append(dp[i+1])
            print(dp)
   
    print(dp[-1]%1000000)
else:
    print(0)
print(dp)
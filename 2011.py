num = input()
dp = [1,1]
lst = ['1','2','3','4','5','6']
a = False
if num[0] != '0':
    for i in range(len(num)):
        if (num[i-1] == '1' and num[i] != '0') or (num[i-1] == '2' and num[i] in lst):
            dp.append(dp[i]+dp[i+1])
        else:
            dp.append(dp[i+1])
        if (num[i-1] == '0' and num[i] == '0') or (int(num[i-1])>2 and num[i]=='0'):
            a = True
            print(0)
            break
    if not a:
        print(dp[-1]%1000000)
else:
    print(0)
num = int(input())
lst = list(map(int,input().split()))

dp = []
plus = True
for i in range(num):
    dp.append(i+1)
    if plus:
        

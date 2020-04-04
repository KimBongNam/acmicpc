import sys
N = int(input())
lst = list(map(int, input().split()))
M = int(input())

dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    dp[i][i] = 1

for i in range(1, N):
    if lst[i-1] == lst[i]:
        dp[i][i+1]=1

for i in range(N-2, -1,-1):
    for j in range(N-1, i+1,-1):
        if lst[i] == lst[j] and dp[i+2][j] == 1:
            dp[i+1][j+1] = 1

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(dp[S][E])

'''
dp = [[0]]
for i in range(N):
    a = []
    for j in range(N-i):
        if i==j:
            a.append(1)
        else:
            al = deque(lst[i:j+1])
            s = len(al)//2
            t = 1
            for p in range(s):
                if al.pop() != al.popleft():
                    a.append(0)
                    t = 0
                    break
            if t:
                a.append(1)
    dp.append(a)

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(dp[S][E-S])'''

'''
for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    if S == E:
        print(1)
    else:    
        al = deque(lst[S-1:E])
        a = len(al)//2
        t = 1
        for i in range(a):
            if al.pop() != al.popleft():
                print(0)
                t = 0
                break
        if t:
            print(1)'''

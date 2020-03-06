N = int(input())
P = sorted(list(map(int, input().split())))
ans = 0

for i in range(N+1):
    for j in range(i):
        ans += P[j]

print(ans)


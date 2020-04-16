N, S = map(int, input().split())
lst = list(map(int, input().split()))
maximum = 2 ** N
ans = 0
for i in range(1,maximum):
    t = maximum + i
    w = str(bin(t))[3:]
    cnt = 0
    for id, val in enumerate(w):
        if val == '1':
            cnt += lst[id]
    if cnt == S:
        ans += 1

print(ans)
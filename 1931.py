import sys
N = int(input())

conv = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

conv.sort(key = lambda x : x[0])
conv.sort(key = lambda x : x[1])
now = conv[0]
ans = 1

for i in conv[1:]:
    if i[0] >= now[1]:
        ans += 1
        now = i

print(ans)
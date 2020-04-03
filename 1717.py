import sys

n, m = map(int, input().split())

lst = [{i} for i in range(n+1)]

for _ in range(m):
    z, a, b = map(int, sys.stdin.readline().split())
    if z == 0:
        val = lst[a].union(lst[b])
        lst[a] = val
        lst[b] = val
    else:
        print("YES" if a in lst[b] else "NO")
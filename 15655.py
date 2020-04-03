from itertools import combinations as c
N, M = map(int, input().split())
lst = list(map(int, input().split()))
ans = list(c(sorted(lst), M))
for i in ans:
    print(*i)
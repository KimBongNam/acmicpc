from itertools import combinations as c
N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = sorted(list(set(list(c(lst,M)))))
for i in ans:
    print(*i)
from itertools import permutations as p
N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = sorted(list(set(list(p(lst,M)))))
for i in ans:
    print(*i)
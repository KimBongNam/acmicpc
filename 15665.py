from itertools import product as p
N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = sorted(list(set(list(p(lst,repeat=M)))))
for i in ans:
    print(*i)
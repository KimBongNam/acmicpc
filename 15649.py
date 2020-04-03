from itertools import permutations as p
N, M = map(int, input().split())
lst = list(p(range(1,N+1),M))
for i in lst:
    print(*i)
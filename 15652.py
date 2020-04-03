from itertools import combinations_with_replacement as c
N, M = map(int, input().split())
lst = list(c(range(1,N+1),M))
for i in lst:
    print(*i)
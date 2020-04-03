from itertools import product
N, M = map(int, input().split())
lst = list(product(range(1,N+1),repeat=M))
for i in lst:
    print(*i)


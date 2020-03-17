from itertools import permutations

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = list(permutations(lst, M))
for i in ans:
    print(*i)


from itertools import combinations

N, K = map(int, input().split())
lst = [i for i in range(N)]
print(len(list(combinations(lst,K))))
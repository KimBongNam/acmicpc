from itertools import combinations
lst = [int(input()) for i in range(9)]
s = sum(lst) - 100

comb = list(combinations(lst, 2))
for i in comb:
    if sum(i) == s:
        lst.remove(i[0])
        lst.remove(i[1])
        lst.sort()
        for j in lst:
            print(j)
        break


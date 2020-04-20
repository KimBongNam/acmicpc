import bisect
N = int(input())
lst = list(map(int, input().split()))
s = sorted(list(set(lst)))
ans = []
for i in lst:
    ans.append(bisect.bisect_left(s, i))

print(*ans)